import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets
def setup_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("FitnessTracker").sheet1
    return sheet
