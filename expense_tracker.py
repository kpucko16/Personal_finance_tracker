import sqlite3
import psycopg2
from psycopg2 import sql
from werkzeug.security import generate_password_hash, check_password_hash


class ExpenseTracker:
    def __init__(self, expense_db_path="/var/finance_tracker/finance_tracker.db", user_db_credentials=None):
        self.expense_db_path = expense_db_path
        self.user_db_credentials = user_db_credentials
        self.initialize_db()

    def initialize_db(self):
        """Ensure the expenses table exists in SQLite."""
        conn = sqlite3.connect(self.expense_db_path)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')
        conn.commit()
        conn.close()

    # User management functions
    def create_user(self, username, password):
        """Create a new user, storing hashed password in PostgreSQL."""
        hashed_password = generate_password_hash(password)  # Hash the password before storing
        conn = psycopg2.connect(**self.user_db_credentials)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (username, password) VALUES (%s, %s)
        ''', (username, hashed_password))
        conn.commit()
        conn.close()

    def authenticate_user(self, username, password):
        """Authenticate a user by checking their password against the hashed value in PostgreSQL."""
        conn = psycopg2.connect(**self.user_db_credentials)
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):
            return user[0]  # Return the user ID
        else:
            return None  # Authentication failed

    # Expense functions
    def add_expenses(self, user_id, description, amount, category=None):
        """Add an expense for a specific user."""
        conn = sqlite3.connect(self.expense_db_path)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO expenses (description, amount, category, user_id)
        VALUES (?, ?, ?, ?)
        ''', (description, amount, category, user_id))
        conn.commit()
        conn.close()

    def view_expenses(self, user_id):
        """Retrieve all expenses for a specific user."""
        conn = sqlite3.connect(self.expense_db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def calculate_total(self, user_id, category=None):
        """Calculate the total expenses for a user."""
        conn = sqlite3.connect(self.expense_db_path)
        cursor = conn.cursor()
        if category:
            cursor.execute('SELECT SUM(amount) FROM expenses WHERE user_id = ? AND category = ?', (user_id, category))
        else:
            cursor.execute('SELECT SUM(amount) FROM expenses WHERE user_id = ?', (user_id,))
        total = cursor.fetchone()[0] or 0  # Default to 0 if no results
        conn.close()
        return total
