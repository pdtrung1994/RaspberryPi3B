#pip install google-api-python-client
from googleapiclient.discovery import build # type: ignore
from google.oauth2 import service_account # type: ignore

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'rpi3b-428319-07ffe23acabf.json'
PARENT_FOLDER_ID = "1dQmxOhRhua45-JJlb69DUWKyx1wqD0iU"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
    return creds

def upload(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name' : "Hello.py",
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body = file_path
    ).execute()

upload("weight_test.py")