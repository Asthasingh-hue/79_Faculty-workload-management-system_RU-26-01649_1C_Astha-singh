import pandas as pd

def load_data():
    try:
        df = pd.read_csv('workload.csv')
        return df
    except:
        df = pd.read_csv('../workload.csv')
        return df

def show_summary():
    df = load_data()
    summary = df.groupby('Faculty')['Hours'].sum()
    print("\n--- Faculty Workload Summary ---")
    for faculty, hours in summary.items():
        if hours > 16:
            print(f"{faculty} : {hours} hours - OVERLOADED by {hours-16} hours")
        else:
            print(f"{faculty} : {hours} hours ({16-hours} free)")

def assign_subject():
    faculty_name = input("Enter Faculty Name: ")
    subject = input("Enter Subject: ")
    try:
        hrs = int(input("Enter Hours: "))
        if hrs <= 0:
            print("Hours must be a positive whole number.")
            return
    except:
        print("Hours must be a positive whole number.")
        return

    df = load_data()
    current_hours = df[df['Faculty'] == faculty_name]['Hours'].sum()
    
    if current_hours + hrs > 16:
        print(f"Cannot assign: {faculty_name} would have {current_hours+hrs} hours, exceeding 16-hour limit.")
    else:
        print(f"Assigned. {faculty_name} now has {current_hours+hrs} hours (limit reached)." if current_hours+hrs==16 else f"Assigned. {faculty_name} now has {current_hours+hrs} hours.")

def find_free_faculty():
    try:
        need = int(input("Enter Hours needed: "))
    except:
        print("Enter valid number")
        return
    df = load_data()
    summary = df.groupby('Faculty')['Hours'].sum()
    print(f"\nFaculty with at least {need} hours free:")
    for faculty, hours in summary.items():
        free = 16 - hours
        if free >= need:
            print(f"{faculty} : {free} hours free")

while True:
    print("\n1. Show workload summary")
    print("2. Assign subject")
    print("3. Find faculty with free hours")
    print("4. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        show_summary()
    elif ch == '2':
        assign_subject()
    elif ch == '3':
        find_free_faculty()
    elif ch == '4':
        break
    else:
        print("Invalid choice")  
