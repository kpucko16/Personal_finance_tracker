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
                # Proceed to expense tracking functions
                break
            else:
                print("Invalid credentials.")
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
