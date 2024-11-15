from expense_tracker import ExpenseTracker


def display_menu():
    tracker = ExpenseTracker()
    while True:
        print('\n--- Finance Tracker ---')
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Total expenses")
        print("4. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            expenses_description = input("Enter expense description: ")
            expenses_amount = input("Amount: ")
            category = input("Enter expense Category: ")
            tracker.add_expenses(expenses_description, expenses_amount, category)
        elif choice == '2':
            print("\n--- Your Expenses ---")
            print(tracker.view_expenses())
        elif choice == '3':
            category = input("Enter category (or press Enter to calculate for all categories): ")
            if category == '':
                category = None
            print(tracker.calculate_total(category))
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    display_menu()
