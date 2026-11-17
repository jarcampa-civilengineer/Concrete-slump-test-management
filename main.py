from test_manager import SlumpTestManager
from reports import show_record, show_history

def ask(label, optional=False):
    while True:
        v = input(label).strip()
        if v or optional:
            return v
        print("This field is required.")

def number(label, minimum=0):
    while True:
        try:
            v = float(input(label))
            if v >= minimum:
                return v
            print(f"Enter a value >= {minimum}.")
        except ValueError:
            print("Enter a valid number.")

def main():
    manager = SlumpTestManager()
    while True:
        print("\n=== CONCRETE SLUMP TEST MANAGEMENT ===")
        print("1. Record test\n2. View history\n3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            low = number("Specified minimum slump (in): ")
            high = number("Specified maximum slump (in): ", low)
            record = manager.add(
                project=ask("Project: "), location=ask("Placement/location (optional): ", True),
                batch=ask("Batch/ticket number: "), truck=ask("Truck number (optional): ", True),
                mix=ask("Mix design ID: "), technician=ask("Tester/technician: "),
                slump=number("Measured slump (in): "), minimum=low, maximum=high,
                notes=ask("Notes (optional): ", True))
            show_record(record)
        elif choice == "2":
            show_history(manager.history())
        elif choice == "3":
            break
        else:
            print("Select 1, 2, or 3.")

if __name__ == "__main__":
    main()
