from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from .models import UserData
from .serializers import UserDataSerializer
from .services.google_sheet import GoogleSheetService
from .services.risk_calculator import RiskCalculator
import logging

logger = logging.getLogger(__name__)

class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response(
                {"error": "Entry with this ID does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['post'])
    def sync_sheet_data(self, request):
        try:
            last_sync = UserData.objects.order_by('-timestamp').first()
            last_timestamp = last_sync.timestamp if last_sync else None

            sheet_service = GoogleSheetService()
            new_entries = sheet_service.get_new_entries(last_timestamp)

            risk_calculator = RiskCalculator()
            saved_entries = []

            for entry in new_entries:
                insurance_risk = risk_calculator.calculate_insurance_risk(
                    entry['age'], entry['lifestyle_score']
                )
                diabetes_risk = risk_calculator.calculate_diabetes_risk(
                    entry['age'], entry['lifestyle_score']
                )

                user_data = UserData.objects.create(
                    **entry,
                    insurance_risk_score=insurance_risk,
                    diabetes_risk_score=diabetes_risk
                )
                saved_entries.append(user_data)

            serializer = UserDataSerializer(saved_entries, many=True)
            return Response({
                'message': f'Successfully synced {len(saved_entries)} new entries',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error during sheet sync: {str(e)}")
            return Response({
                'error': 'Failed to sync sheet data',
                'detail': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)