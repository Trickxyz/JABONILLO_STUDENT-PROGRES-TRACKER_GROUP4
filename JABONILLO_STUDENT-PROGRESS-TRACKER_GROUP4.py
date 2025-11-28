def input_name(prompt):
    while True:
        name = input(prompt).strip()
        if name.replace(" ", "").isalpha():
            return name
        print("Invalid input. Name must contain letters only and cannot be blank.")

def input_float(prompt, min_val=0, max_val=10000):
    while True:
        try:
            val = float(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Enter a number.")

def calculate_grade(records):
    outputs = {
        "Daily Activities": 0.20,
        "Quiz": 0.25,
        "Exam": 0.30,
        "PT": 0.25
    }
    total = 0
    for key, output in outputs.items():
        avg = sum(records[key]) / len(records[key]) if records[key] else 0
        total += avg * output
    return total

def record_score(category, records):
    earned = input_float(f"Enter points earned for {category}: ", 0)
    total = input_float(f"Enter total points possible for {category}: ", earned)
    percentage = (earned / total) * 100
    records[category].append(percentage)
    print(f"{category} score recorded: {round(percentage,2)}%")
    grade = calculate_grade(records)
    print(f"Current Overall Grade: {round(grade,2)}%")

def confirm_exit():
    while True:
        confirm = input("Are you sure you want to exit? (Y/N): ").strip().lower().upper()
        if confirm in ("y", "yes", "Y", "YES"):
            return True
        elif confirm in ("n", "no", "N", "NO"):
            return False
        else:
            print("Please enter Y (yes) or N (no).")
def main():
    student = {}
    student['name'] = input_name("Enter student name: ")
    student['records'] = {
        "Daily Activities": [],
        "Quiz": [],
        "Exam": [],
        "PT": []
    }

    while True:
        print("\n=== MENU ===")
        print("1. Record Daily Activities")
        print("2. Record Quiz")
        print("3. Record Exam")
        print("4. Record Performance Task (PT)")
        print("5. View Records & Calculate Grade")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            record_score("Daily Activities", student['records'])
        elif choice == "2":
            record_score("Quiz", student['records'])
        elif choice == "3":
            record_score("Exam", student['records'])
        elif choice == "4":
            record_score("PT", student['records'])
        elif choice == "5":
            print(f"\nRecords for {student['name']}:")
            for key, scores in student['records'].items():
                print(f"{key}: {', '.join(f'{s:.2f}%' for s in scores)}")
            grade = calculate_grade(student['records'])
            print(f"Overall Grade: {round(grade,2)}%")
        elif choice == "6":
            if confirm_exit():
                print("Exiting...")
                break
            else:
                print("Exit canceled.")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()