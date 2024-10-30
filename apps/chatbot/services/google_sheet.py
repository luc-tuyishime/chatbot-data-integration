import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os

class GoogleSheetService:
    def __init__(self):
        self.SCOPES = [
            'https://www.googleapis.com/auth/spreadsheets.readonly',
            'https://www.googleapis.com/auth/drive.readonly'
        ]
        self.SHEET_ID = os.getenv('GOOGLE_SHEET_ID')
        
    def get_new_entries(self, last_timestamp=None):
        try:
            creds = Credentials.from_service_account_file(
                'service_account.json',
                scopes=self.SCOPES
            )
            
            client = gspread.authorize(creds)
            sheet = client.open_by_key(self.SHEET_ID).sheet1
            
            rows = sheet.get_all_values()[1:] 
            
            new_entries = []
            for row in rows:
                timestamp = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S')
                if not last_timestamp or timestamp > last_timestamp:
                    entry = {
                        'name': row[0],
                        'age': int(row[1]),
                        'gender': row[2],
                        'lifestyle_score': float(row[3]),
                        'timestamp': timestamp
                    }
                    new_entries.append(entry)
                    
            return new_entries
            
        except Exception as e:
            print(f"Error fetching sheet data: {str(e)}")
            return []