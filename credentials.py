import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define required API scopes
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

    # Load credentials from token.json if it exists
    if os.path.exists("token.json"):
        try:
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        except Exception as e:
            print(f"Error loading token.json: {e}")
            creds = None  # Reset creds if the file is corrupted

    # If no valid credentials, initiate OAuth flow
    if not creds or not creds.valid:
        try:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())  # Refresh token if expired
            else:
                # Ensure credentials.json exists before running the OAuth flow
                if not os.path.exists("credentials.json"):
                    raise FileNotFoundError("Missing credentials.json. Download it from Google Cloud.")

                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")

            # Save the refreshed/new credentials
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        except Exception as e:
            print(f"Authentication failed: {e}")
            return None

    return creds

if __name__ == "__main__":
    creds = get_credentials()
    if creds:
        print("✅ Google API authentication successful!")
    else:
        print("❌ Authentication failed. Check your credentials.json and token.json.")
