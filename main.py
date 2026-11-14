import pandas as pd
import os

FILE_NAME = "workload.csv"
LIMIT = 16

def load_data():
    if not os.path.exists(FILE_NAME):
        print(f"Error: {FILE_NAME} file not found!")
        return None
    try:
        df = pd.read_csv(FILE_NAME)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def show_summary():
    df = load_data()
    if df is None: return
    grouped = df.groupby("Faculty")["Hours"].sum()
    print("\n--- Workload Summary ---")
    for faculty, hours in grouped.items():
        if hours > LIMIT:
            print(f"{faculty} : {int(hours)} hours - OVERLOADED by {int(hours - LIMIT)} hours")
        else:
            free = LIMIT - hours
            print(f"{faculty} : {int(hours)} hours ({int(free)} free)")

def assign_subject():
    df = load_data()
    if df is None: return
    
    faculty = input("Faculty: ").strip()
    subject = input("Subject: ").strip()
    try:
        hours = int(input("Hours: ").strip())
    except:
        print("Hours must be a positive whole number.")
        return

    if hours <= 0:
        print("Hours must be a positive whole number.")
        return

    grouped = df.groupby("Faculty")["Hours"].sum()
    current_hours = grouped.get(faculty, 0)

    if current_hours + hours > LIMIT:
        print(f"Cannot assign: {faculty} would have {int(current_hours + hours)} hours, exceeding the 16-hour limit.")
        return
    else:
        new_row = pd.DataFrame([{"Faculty": faculty, "Subject": subject, "Hours": hours}])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(FILE_NAME, index=False)
        total = current_hours + hours
        if total == LIMIT:
            print(f"Assigned. {faculty} now has {int(total)} hours (limit reached).")
        else:
            print(f"Assigned. {faculty} now has {int(total)} hours ({int(LIMIT-total)} free).")

def find_faculty():
    df = load_data()
    if df is None: return
    try:
        needed = int(input("Hours needed: ").strip())
    except:
        print("Please enter valid number.")
        return
        
    grouped = df.groupby("Faculty")["Hours"].sum()
    print(f"\nFaculty available for {needed} hours:")
    found = False
    for faculty, hours in grouped.items():
        free = LIMIT - hours
        if free >= needed:
            print(f"{faculty} : {int(free)} hours free")
            found = True
    if not found:
        print("No faculty available.")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Show workload summary")
        print("2. Assign subject")
        print("3. Find faculty with free hours")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            show_summary()
        elif choice == '2':
            assign_subject()
        elif choice == '3':
            find_faculty()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()