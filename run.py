import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Setup Google Sheets
def setup_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("FitnessTracker").sheet1
    return sheet

def main():
    print("🏋️‍♂️ Welcome to the Fitness Tracker!")

# Main fitness tracker
def main():
    print("🏋️‍♂️ Welcome to the Fitness Tracker!")
    sheet = setup_google_sheet()
    # Add headers if not found
    ensure_headers(sheet)
    while True:
        print("\n1. Add an exercise\n2. View weekly summary\n3. Exit") # Display menu options
        # Get user input for their chosen action
        choice = input("Choose an option: ")
        # Handle user choices
        if choice == "1":
            exercise = get_user_exercise()
            save_exercise_to_google_sheet(exercise, sheet)
        elif choice == "2":
            # Summarise exercises for the week
            summarise_weekly_exercises(sheet)
        elif choice == "3":
            # User wants to exit the program
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


   