class BudgetTracker:
    def __init__(self):
        self.income_sources = {}
        self.expenses = {}
        self.savings = 0

    def add_income(self, name, amount):
        if name in self.income_sources:
            self.income_sources[name] += amount
        else:
            self.income_sources[name] = amount

    def total_income(self):
        return sum(self.income_sources.values())

    def add_expense(self, name, amount):
        self.expenses[name] = amount

    def calculate_total_expenses(self):
        return sum(self.expenses.values())

    def calculate_balance(self):
        return self.total_income() - self.calculate_total_expenses() - self.savings

    def set_savings(self, amount):
        self.savings = amount

    def show_summary(self):
        print("Income:")
        for name, amount in self.income_sources.items():
            print(f"  {name}: ${amount}")
        print(f"Total Income: ${self.total_income()}")
        print("Expenses:")
        for name, amount in self.expenses.items():
            print(f"  {name}: ${amount}")
        print(f"Savings: ${self.savings}")
        print(f"Total Expenses: ${self.calculate_total_expenses()}")
        print(f"Balance: ${self.calculate_balance()}")

# Example usage
tracker = BudgetTracker()

# Add income
tracker.add_income("Paycheck 1", 2500)  # First pay stub
tracker.add_income("Paycheck 2", 2500)  # Second pay stub

# Add expenses
tracker.add_expense("Rent", 1200)
tracker.add_expense("Groceries", 300)
tracker.add_expense("Utilities", 150)
tracker.add_expense("Transport", 100)
tracker.add_expense("School", 25000)

# Set savings
tracker.set_savings(250000.00)

# Show summary
tracker.show_summary()
