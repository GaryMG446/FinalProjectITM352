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
        monthly_income = [entry for entry in self.daily_income if entry["date"].year == year and entry["date"].month == month]
        monthly_expenses = [entry for entry in self.daily_expenses if entry["date"].year == year and entry["date"].month == month]
        
        monthly_income_total = sum(entry["amount"] for entry in monthly_income)
        monthly_expenses_total = sum(entry["amount"] for entry in monthly_expenses)

        print(f"Monthly Summary for {year}-{month}:")
        print(f"  Total Income: ${monthly_income_total}")
        print(f"  Total Expenses: ${monthly_expenses_total}")
        print(f"  Balance: ${monthly_income_total - monthly_expenses_total - self.savings}")

    def yearly_summary(self, year):
        yearly_income = [entry for entry in self.daily_income if entry["date"].year == year]
        yearly_expenses = [entry for entry in self.daily_expenses if entry["date"].year == year]

        yearly_income_total = sum(entry["amount"] for entry in yearly_income)
        yearly_expenses_total = sum(entry["amount"] for entry in yearly_expenses)

        print(f"Yearly Summary for {year}:")
        print(f"  Total Income: ${yearly_income_total}")
        print(f"  Total Expenses: ${yearly_expenses_total}")
        print(f"  Balance: ${yearly_income_total - yearly_expenses_total - self.savings}")

    def export_daily_data_to_excel(self):
        date_str = datetime.datetime.now(self.timezone).strftime('%Y-%m-%d')
        income_df = pd.DataFrame(self.daily_income)
        expenses_df = pd.DataFrame(self.daily_expenses)
        
        # Create a new Excel writer
        with pd.ExcelWriter(f'daily_budget_{date_str}.xlsx') as writer:
            income_df.to_excel(writer, sheet_name='Income', index=False)
            expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
        print(f"Daily data exported to daily_budget_{date_str}.xlsx")

    def export_monthly_summary_to_excel(self):
        current_date = datetime.datetime.now(self.timezone)
        year, month = current_date.year, current_date.month

        monthly_income = [entry for entry in self.daily_income if entry["date"].year == year and entry["date"].month == month]
        monthly_expenses = [entry for entry in self.daily_expenses if entry["date"].year == year and entry["date"].month == month]

        income_df = pd.DataFrame(monthly_income)
        expenses_df = pd.DataFrame(monthly_expenses)

        monthly_income_total = sum(entry["amount"] for entry in monthly_income)
        monthly_expenses_total = sum(entry["amount"] for entry in monthly_expenses)

        # Create a new Excel writer
        with pd.ExcelWriter(f'monthly_budget_{year}_{month}.xlsx') as writer:
            income_df.to_excel(writer, sheet_name='Income', index=False)
            expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
            
            # Write totals to a new sheet
            totals_df = pd.DataFrame({
                'Category': ['Income', 'Expenses'],
                'Total': [monthly_income_total, monthly_expenses_total]
            })
            totals_df.to_excel(writer, sheet_name='Totals', index=False)

        print(f"Monthly summary exported to monthly_budget_{year}_{month}.xlsx")

    def export_yearly_summary_to_excel(self):
        current_date = datetime.datetime.now(self.timezone)
        year = current_date.year

        yearly_income = [entry for entry in self.daily_income if entry["date"].year == year]
        yearly_expenses = [entry for entry in self.daily_expenses if entry["date"].year == year]

        income_df = pd.DataFrame(yearly_income)
        expenses_df = pd.DataFrame(yearly_expenses)

        yearly_income_total = sum(entry["amount"] for entry in yearly_income)
        yearly_expenses_total = sum(entry["amount"] for entry in yearly_expenses)

        # Create a new Excel writer
        with pd.ExcelWriter(f'yearly_budget_{year}.xlsx') as writer:
            income_df.to_excel(writer, sheet_name='Income', index=False)
            expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
            
            # Write totals to a new sheet
            totals_df = pd.DataFrame({
                'Category': ['Income', 'Expenses'],
                'Total': [yearly_income_total, yearly_expenses_total]
            })
            totals_df.to_excel(writer, sheet_name='Totals', index=False)

        print(f"Yearly summary exported to yearly_budget_{year}.xlsx")

def job_daily():
    tracker.export_daily_data_to_excel()

def job_monthly():
    tracker.export_monthly_summary_to_excel()

def job_yearly():
    tracker.export_yearly_summary_to_excel()

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)  # wait one minute

def is_last_day_of_month(date):
    next_day = date + datetime.timedelta(days=1)
    return next_day.month != date.month

def is_last_day_of_year(date):
    next_day = date + datetime.timedelta(days=1)
    return next_day.year != date.year

def job_monthly_check():
    current_date = datetime.datetime.now(pytz.timezone('Pacific/Honolulu')).date()
    if is_last_day_of_month(current_date):
        job_monthly()

def job_yearly_check():
    current_date = datetime.datetime.now(pytz.timezone('Pacific/Honolulu')).date()
    if is_last_day_of_year(current_date):
        job_yearly()

# Example usage
tracker = BudgetTracker()

# Add daily income
tracker.add_income("Territorial Savings Bank", 499.00)  # Start Of Python Project
tracker.add_income("Tips Work", 0.00)
tracker.add_income("Tips Work", 0.00)

# Add daily expenses
tracker.add_expense("BreakFast", 28.95)
tracker.add_expense("Lunch", 14.75)
tracker.add_expense("Dinner", 0.00)

# Set savings
tracker.set_savings(250000.00)

# Show daily summary
tracker.show_summary()

# Export data immediately for testing
tracker.export_daily_data_to_excel()
tracker.export_monthly_summary_to_excel()
tracker.export_yearly_summary_to_excel()

# Schedule job to export daily data to Excel at the end of each day
schedule.every().day.at("23:59").do(job_daily)

# Schedule job to check for the last day of the month
schedule.every().day.at("23:59").do(job_monthly_check)

# Schedule job to check for the last day of the year
schedule.every().day.at("23:59").do(job_yearly_check)

# Run the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

# Now you can continue using your terminal while the scheduler runs in the background
print("Scheduler is running in the background. You can continue using your terminal.")
