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

def ensure_headers(sheet):
    """Ensure the sheet has proper headers."""
    existing_headers = sheet.row_values(1)  # Fetch the first row
    required_headers = ["Date", "Exercise Name", "Muscle Group", "Sets", "Reps per Set", "Total Reps", "Weight (kg)"]
    if existing_headers != required_headers:
        sheet.insert_row(required_headers, index=1)
        print("✔️ Added headers to the Google Sheet.")

def get_user_exercise():
    """Collect exercise details from the user."""
     # User to enter the exercise name
    name = input("Enter the exercise name: ").strip()
    # Define list of muscle groups
    muscle_groups = ["Chest", "Back", "Legs", "Arms", "Shoulders", "Core", "Cardio"]
    print("Choose a muscle group:")
    for i, group in enumerate(muscle_groups, start=1):
        print(f"{i}. {group}")
    muscle_group = None
    while not muscle_group:
        try:
            choice = int(input("Enter the number: "))
            muscle_group = muscle_groups[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")



   