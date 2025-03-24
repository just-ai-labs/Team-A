import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents"
]

def get_credentials():
    """
    Handles Google API authentication and returns valid credentials.
    Saves a token.json file for reuse.
    """
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
 
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
          flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
          creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")


        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def list_drive_files():
    """
    Lists files from Google Drive.
    """
    creds = get_credentials()
    try:
        service = build("drive", "v3", credentials=creds)
        results = service.files().list(pageSize=10, fields="files(id, name)").execute()
        files = results.get("files", [])

        if not files:
            print("No files found.")
        else:
            print("Files in Drive:")
            for file in files:
                print(f"{file['name']} ({file['id']})")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    list_drive_files()
