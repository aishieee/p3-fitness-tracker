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
    # Allow breaking reps into sets
    sets = int(input("Enter the number of sets: "))
    reps_per_set = []
    for s in range(sets):
        reps = int(input(f"Enter the number of reps for set {s + 1}: "))
        reps_per_set.append(reps)
    total_reps = sum(reps_per_set)
    weight = input("Enter the weight used (kg), or press Enter if none: ")
    weight = float(weight.strip()) if weight.strip() else 0
    date = datetime.now().strftime("%Y-%m-%d")
    return {
        "date": date,
        "name": name,
        "muscle_group": muscle_group,
        "sets": sets,
        "reps_per_set": ', '.join(map(str, reps_per_set)),
        "total_reps": total_reps,
        "weight": weight
    }

def save_exercise_to_google_sheet(exercise, sheet):
    """Append exercise details to Google Sheets."""
    try:
        sheet.append_row([
            exercise["date"],
            exercise["name"],
            exercise["muscle_group"],
            exercise["sets"],
            exercise["reps_per_set"],
            exercise["total_reps"],
            exercise["weight"]
        ])
        print(f"✔️ Saved: {exercise['name']} - {exercise['muscle_group']} - {exercise['total_reps']} reps - {exercise['weight']}kg")
    except Exception as e:
        print(f"❌ Error saving to Google Sheets: {e}")

def summarize_weekly_exercises(sheet):
    """Generate and display a weekly summary of exercises."""
    try:
        records = sheet.get_all_records()
        if not records:
            print("⚠️ No exercises logged yet.")
            return
        weekly_stats = {}
        for record in records:
            muscle_group = record["Muscle Group"]
            total_reps = record.get("Total Reps", 0)
            weight = record.get("Weight (kg)", 0)
        if muscle_group not in weekly_stats:
                weekly_stats[muscle_group] = {"reps": 0, "weight": 0}
            weekly_stats[muscle_group]["reps"] += int(total_reps)
            weekly_stats[muscle_group]["weight"] += float(weight)
        print("\n📊 Weekly Summary:")
        for muscle_group, stats in weekly_stats.items():
            print(f"{muscle_group}: {stats['reps']} reps, {stats['weight']} kg lifted")





   