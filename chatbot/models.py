from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    lifestyle_score = models.FloatField()
    timestamp = models.DateTimeField()
    insurance_risk_score = models.FloatField(null=True)
    diabetes_risk_score = models.FloatField(null=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp}"

