import csv
import os
from expense_model import Expense


class ExpenseTracker:
    CATEGORIES = ["Food", "Transportation", "Entertainment", "Others"]  
    
        
    def load_expenses(self):
        """Load expenses from the CSV file at startup."""
        try:
            with open(self.file_name, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expense = Expense(row["category"], float(row["amount"]), row["date"])
                    self.expenses.append(expense)
                    if expense.category in self.categories:
                        self.categories[expense.category].append(expense)
        except FileNotFoundError:
            print("No expenses file found. Starting a new expense tracker.")
        except Exception as e:
            print(f"Error loading expenses: {e}") 
            
    def __init__(self, file_name="expenses.csv"):
        self.file_name = file_name
        self.expenses = []
        self.categories = {category: [] for category in self.CATEGORIES}  
        self.load_expenses()        
    
    def save_expense(self, expense: Expense):
        """Save an expense to the CSV file."""
        file_exists = os.path.isfile(self.file_name)
        with open(self.file_name, mode="a", newline="") as file:
            fieldnames = ["category", "amount", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Write headers only if the file is new or empty
            if not file_exists or os.stat(self.file_name).st_size == 0:
                writer.writeheader()
            writer.writerow(expense.to_dict())
            
             
    def add_expense(self, amount: float, date: str):
        category = self.select_category()
        expense = Expense(category, amount, date)
        self.expenses.append(expense)
        self.categories[category].append(expense)
        self.save_expense(expense)    
        
    def select_category(self) -> str:
        #Display available categories and let the user select one.
        print("Select a category for the expense:")
        for i, category in enumerate(self.CATEGORIES, 1):
            print(f"{i}. {category}")
        
        while True:
            try:
                choice = int(input("Enter the number of the category: "))
                if 1 <= choice <= len(self.CATEGORIES):
                    return self.CATEGORIES[choice - 1]
                else:
                    print("Invalid choice. Please select a valid category number.")
            except ValueError:
                print("Invalid input. Please enter a number.")    
                
    def view_expenses(self, category: str = None, month: str = None):
        if category:
            return self.categories.get(category, [])
        elif month:
            month_expenses = [
                expense for expense in self.expenses
                if expense.date.strftime("%m-%Y") == month
            ]
            return month_expenses
        else:
            return self.expenses   
        
    def calculate_total_expenses(self, category: str = None, month: str = None) -> float:
            if category:
                total = sum(expense.amount for expense in self.categories.get(category, []))
            elif month:
                total = sum(
                    expense.amount for expense in self.expenses
                    if expense.date.strftime("%m-%Y") == month
                )
            else:
                total = sum(expense.amount for expense in self.expenses)
            return total      
    
    # Display expenses in a readable format.   
    def display_expenses(self, expenses):
            if not expenses:
                print("No expenses found.")
            else:
                for expense in expenses:
                    print(f"{expense.category}: {expense.amount}XAF on {expense.date.strftime('%Y-%m-%d')}")   
                
                
    def menu(self):
            while True:
                print("\nExpense Tracker Menu:")
                print("1. Add new expense")
                print("2. View expenses by category")
                print("3. View expenses by month")
                print("4. Calculate total expenses by category")
                print("5. Calculate total expenses by month")
                print("6. Exit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    amount = float(input("Enter expense amount: "))
                    date = input("Enter expense date (YYYY-MM-DD): ")
                    try:
                        self.add_expense(amount, date)
                        print("Expense added successfully.")
                    except ValueError as e:
                        print(e)
                elif choice == "2":
                    category = input("Enter category to view expenses: ")
                    expenses = self.view_expenses(category=category)
                    self.display_expenses(expenses)
                elif choice == "3":
                    month = input("Enter month to view expenses (MM-YYYY): ")
                    expenses = self.view_expenses(month=month)
                    self.display_expenses(expenses)
                elif choice == "4":
                    category = input("Enter category to calculate total expenses: ")
                    total = self.calculate_total_expenses(category=category)
                    print(f"Total expenses for category '{category}': {total}XAF")
                elif choice == "5":
                    month = input("Enter month to calculate total expenses (MM-YYYY): ")
                    total = self.calculate_total_expenses(month=month)
                    print(f"Total expenses for month '{month}': {total}XAF")
                elif choice == "6":
                    print("Exiting expense tracker.")
                    break
                else:
                    print("Invalid choice. Please try again.")                                          