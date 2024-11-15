class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expenses(self, description, amount, category):
        self.expenses.append((description, amount, category))

    def view_expenses(self):
        for expense in self.expenses:
            return expense

    def calculate_total(self, category=None):
        total = 0
        for _, amount, expenses_category in self.expenses:
            if category is None or category == expenses_category:
                total += int(amount)
        return total
