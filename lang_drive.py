import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # Replace with Gemini API when available
from langchain.chains import LLMChain
import fitz  # For PDFs
import pandas as pd  # For CSV and Excel
import json  # For JSON files
from docx import Document  # For Word files

SCOPES = ["https://www.googleapis.com/auth/drive"]

# Step 1: Setting up LangChain LLM
llm = OpenAI(api_key="")  # Replace with Gemini API setup if applicable

# Define a prompt template for summarization
summary_prompt = PromptTemplate(
    input_variables=["content"],
    template="Summarize the following content: {content}",
)

# Create a LangChain LLM chain for summarization
llm_chain = LLMChain(llm=llm, prompt=summary_prompt)

def get_credentials():
    """
    Authenticate and get Google Drive API credentials.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=8080, access_type="offline", prompt="consent")

        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def summarize_with_llm(content):
    """
    Use LangChain to summarize content using LLM (Gemini or OpenAI).
    """
    summary = llm_chain.run(content)
    return summary

def extract_text_from_file(file_path, mime_type):
    """Extract text from different file types."""
    content = ""

    try:
        if "text/plain" in mime_type:  # TXT files
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

        elif "application/pdf" in mime_type:  # PDF files
            doc = fitz.open(file_path)
            content = "\n".join([page.get_text() for page in doc])

        elif "application/vnd.openxmlformats-officedocument.wordprocessingml.document" in mime_type:  # DOCX
            doc = Document(file_path)
            content = "\n".join([para.text for para in doc.paragraphs])

        elif "text/csv" in mime_type:  # CSV files
            df = pd.read_csv(file_path)
            content = df.to_string()

        elif "application/json" in mime_type:  # JSON files
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            content = json.dumps(data, indent=4)

        else:
            return f"❌ Unsupported file type ({mime_type}). Only TXT, PDF, DOCX, CSV, and JSON are supported."

    except Exception as e:
        return f"❌ Error extracting content: {str(e)}"

    return summarize_with_llm(content)

def summarize_file(file_id):
    """Download a file from Google Drive and summarize it."""
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    # Get file metadata
    file_metadata = service.files().get(fileId=file_id, fields="mimeType, name").execute()
    mime_type = file_metadata.get("mimeType", "")
    file_name = file_metadata.get("name", "downloaded_file")

    # Download the file
    file_path = f"./{file_name}"
    request = service.files().get_media(fileId=file_id)
    with open(file_path, "wb") as f:
        f.write(request.execute())

    # Extract and summarize text using LangChain's LLM
    summary = extract_text_from_file(file_path, mime_type)

    print("\n🔹 File Summary:")
    print(summary)

    # Cleanup
    os.remove(file_path)

def upload_file(file_path, folder_id):
    """
    Uploads a file to a specific Google Drive folder.
    """
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    file_name = os.path.basename(file_path)
    file_metadata = {"name": file_name, "parents": [folder_id]}
    media = MediaFileUpload(file_path, resumable=True)

    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    file_id = uploaded_file.get("id")
    print(f"File uploaded successfully: https://drive.google.com/file/d/{file_id}")

def list_files_in_folder(folder_id):
    """
    Lists files inside a specific Google Drive folder.
    """
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    results = service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
    files = results.get("files", [])

    if not files:
        print("No files found in this folder.")
    else:
        print("\nFiles in folder:")
        for file in files:
            print(f"{file['name']} ({file['id']})")

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Upload file")
        print("2. List files in folder")
        print("3. Summarize a text file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter the file path: ")
            folder_id = input("Enter the Google Drive folder ID: ")
            upload_file(file_path, folder_id)

        elif choice == "2":
            folder_id = input("Enter the Google Drive folder ID: ")
            list_files_in_folder(folder_id)

        elif choice == "3":
            file_id = input("Enter the Google Drive file ID: ")
            summarize_file(file_id)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
