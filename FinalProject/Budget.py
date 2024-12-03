import datetime
import pytz
import pandas as pd
import schedule
import time
import threading

class BudgetTracker:
    def __init__(self):
        self.daily_income = []
        self.daily_expenses = []
        self.savings = 0
        self.timezone = pytz.timezone('Pacific/Honolulu')

    def add_income(self, name, amount):
        date = datetime.datetime.now(self.timezone).date()
        self.daily_income.append({"date": date, "name": name, "amount": amount})

    def total_income(self):
        return sum(entry["amount"] for entry in self.daily_income)

    def add_expense(self, name, amount):
        date = datetime.datetime.now(self.timezone).date()
        self.daily_expenses.append({"date": date, "name": name, "amount": amount})

    def calculate_total_expenses(self):
        return sum(entry["amount"] for entry in self.daily_expenses)

    def calculate_balance(self):
        return self.total_income() - self.calculate_total_expenses() - self.savings

    def set_savings(self, amount):
        self.savings = amount

    def show_summary(self):
        print("Income:")
        for entry in self.daily_income:
            print(f"  {entry['name']} (${entry['amount']}) on {entry['date']}")
        print(f"Total Income: ${self.total_income()}")
        
        print("Expenses:")
        for entry in self.daily_expenses:
            print(f"  {entry['name']} (${entry['amount']}) on {entry['date']}")
        print(f"Savings: ${self.savings}")
        print(f"Total Expenses: ${self.calculate_total_expenses()}")
        print(f"Balance: ${self.calculate_balance()}")

    def monthly_summary(self, year, month):
        monthly_income = sum(entry["amount"] for entry in self.daily_income if entry["date"].year == year and entry["date"].month == month)
        monthly_expenses = sum(entry["amount"] for entry in self.daily_expenses if entry["date"].year == year and entry["date"].month == month)
        print(f"Monthly Summary for {year}-{month}:")
        print(f"  Total Income: ${monthly_income}")
        print(f"  Total Expenses: ${monthly_expenses}")
        print(f"  Balance: ${monthly_income - monthly_expenses - self.savings}")

    def yearly_summary(self, year):
        yearly_income = sum(entry["amount"] for entry in self.daily_income if entry["date"].year == year)
        yearly_expenses = sum(entry["amount"] for entry in self.daily_expenses if entry["date"].year == year)
        print(f"Yearly Summary for {year}:")
        print(f"  Total Income: ${yearly_income}")
        print(f"  Total Expenses: ${yearly_expenses}")
        print(f"  Balance: ${yearly_income - yearly_expenses - self.savings}")

    def export_daily_data_to_excel(self):
        date_str = datetime.datetime.now(self.timezone).strftime('%Y-%m-%d')
        income_df = pd.DataFrame(self.daily_income)
        expenses_df = pd.DataFrame(self.daily_expenses)
        
        # Create a new Excel writer
        with pd.ExcelWriter(f'daily_budget_{date_str}.xlsx') as writer:
            income_df.to_excel(writer, sheet_name='Income', index=False)
            expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
        print(f"Daily data exported to daily_budget_{date_str}.xlsx")

def job():
    tracker.export_daily_data_to_excel()

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)  # wait one minute

# Example usage
tracker = BudgetTracker()

# Add daily income
tracker.add_income("Territorial Savings Bank", 356.05) # Start Of Python Project
tracker.add_income("Tips GEN BBQ", 25.00)
tracker.add_income("Tips GEN BBQ", 35.00)


# Add daily expenses
tracker.add_expense("BreakFast 711", 25.00)
tracker.add_expense("Lunch L&L", 20.00)
tracker.add_expense("Mcdonalds", 14.50)

# Set savings
tracker.set_savings(250000.00)

# Show daily summary
tracker.show_summary()

# Export data immediately for testing
tracker.export_daily_data_to_excel()

# Schedule job to export daily data to Excel at the end of each day
schedule.every().day.at("23:59").do(job)

# Run the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

# Now you can continue using your terminal while the scheduler runs in the background
print("Scheduler is running in the background. You can continue using your terminal.")
