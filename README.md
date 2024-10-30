# Chatbot Data Integration Project

Chatbot data Integration.

## Fearures

- Google Sheets integration
- Mock risk score calculation (insurance & diabetes)
- REST API endpoints
- Data persistence

## Prerequisites

- Python 3.10+
- Google Sheets API access
- Service Account credentials

## Setup

## Google Cloud Setup

1. Create project in Google Cloud Console
2. Enable Google Sheets API
3. Create Service Account:
   - Go to "APIs & Services" > "Credentials"
   - Create Service Account
   - Download JSON key as 'service_account.json'
   - Place in project root

## Google Sheet Setup

1. Create sheet with headers:

```
name, age, gender, lifestyle_score, timestamp
```

2. Copy Sheet ID from URL
3. Share with service account email

## Project Setup

```
# Clone repository
git clone https://github.com/yourusername/chatbot-integration.git
cd chatbot-integration

# Virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dependencies
pip install -r requirements.txt

# Environment variables (.env)
DJANGO_SECRET_KEY=your-secret-key
GOOGLE_SHEET_ID=your-sheet-id

# Database
python manage.py migrate

# Run server
python manage.py runserver
```

## API Endpoints

### User Data

| Ressource URL                   | Methods | Description            |
| ------------------------------- | ------- | ---------------------- |
| /api/user-data/sync_sheet_data/ | POST    | Sync with Google Sheet |
| /api/user-data/                 | GET     | List all entries       |
| /api/user-data/`<id>`/          | GET     | Get single entry       |

### Data Format

```json
{
    "id": 101,
    "name": "James Davis",
    "age": 41,
    "gender": "male",
    "lifestyle_score": 2.0,
    "timestamp": "2024-10-28T02:59:39-05:00",
    "insurance_risk_score": 0.605,
    "diabetes_risk_score": 0.65625
},
```

## Project Structure

```
chatbot_project/
├── chatbot/              # Main app
├── config/               # Project settings
├── manage.py
└── requirements.txt
```
