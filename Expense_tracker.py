from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now()

    def __str__(self):
        return f"Amount: ${self.amount}, Category: {self.category}, Description: {self.description}, Date: {self.date}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def expenses_by_category(self):
        categories = {}
        for expense in self.expenses:
            if expense.category in categories:
                categories[expense.category] += expense.amount
            else:
                categories[expense.category] = expense.amount
        return categories

def Tracker():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            expense = Expense(amount, category, description)
            tracker.add_expense(expense)
            print("Expense added successfully!")
        elif choice == "2":
            print("\nAll Expenses:")
            tracker.view_expenses()
        elif choice == "3":
            print(f"\nTotal Expenses: ${tracker.total_expenses():.2f}")
        elif choice == "4":
            print("\nExpenses by Category:")
            expenses_by_category = tracker.expenses_by_category()
            for category, amount in expenses_by_category.items():
                print(f"{category}: ${amount:.2f}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

Tracker()
