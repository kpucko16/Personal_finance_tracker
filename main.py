from expense_tracker import ExpenseTracker

def main():
    user_db_credentials = {
        'host': 'localhost',
        'dbname': 'finance_tracker_user_db',
        'user': 'tracker_user',
        'password': 'your_password'
    }
    tracker = ExpenseTracker(user_db_credentials=user_db_credentials)

    # User creation and login flow
    while True:
        print("\n--- Finance Tracker ---")
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
        choice = input("Please select an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            tracker.create_user(username, password)
            print("User created successfully.")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = tracker.authenticate_user(username, password)
            if user_id:
                print(f"Welcome {username}!")
                # After login, allow user to track expenses
                while True:
                    print("\n--- Expense Tracker ---")
                    print("1. Add Expense")
                    print("2. View Expenses")
                    print("3. Log out")
                    expense_choice = input("Please select an option: ")

                    if expense_choice == '1':
                        description = input("Enter expense description: ")
                        amount = float(input("Enter expense amount: "))
                        category = input("Enter expense category (optional): ")
                        tracker.add_expenses(user_id, description, amount, category)
                        print("Expense added successfully.")
                    elif expense_choice == '2':
                        expenses = tracker.view_expenses(user_id)
                        print("\n--- Your Expenses ---")
                        for expense in expenses:
                            print(f"{expense[0]} - {expense[1]} - {expense[2]} - {expense[3]} - {expense[4]}")
                    elif expense_choice == '3':
                        print("Logging out... Goodbye!")
                        break
            else:
                print("Invalid credentials.")
        elif choice == '3':
            print("Exiting... Goodbye!")
            break

if __name__ == "__main__":
    main()
