import sqlite3


class ExpenseTracker:
    def __init__(self, db_path="/var/finance_tracker/finance_tracker.db"):
        self.db_path = db_path
        self.initialize_db()

    def initialize_db(self):
        """Ensure the expenses table exists."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        conn.commit()
        conn.close()

    def add_expenses(self, description, amount, category=None):
        """Add a new expense to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO expenses (description, amount, category)
        VALUES (?, ?, ?)
        ''', (description, amount, category))
        conn.commit()
        conn.close()

    def view_expenses(self):
        """Retrieve and display all expenses."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def calculate_total(self, category=None):
        """Calculate the total expenses, optionally filtering by category."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        if category:
            cursor.execute('SELECT SUM(amount) FROM expenses WHERE category=?', (category,))
        else:
            cursor.execute('SELECT SUM(amount) FROM expenses')
        total = cursor.fetchone()[0] or 0  # Default to 0 if no results
        conn.close()
        return total
