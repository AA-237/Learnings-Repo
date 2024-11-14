from expense_tracker import ExpenseTracker

if __name__ == "__main__":
    tracker = ExpenseTracker()
    print("-----------------------")
    print("Expenses loaded:")
    
    # Print loaded expenses for verification
    for expense in tracker.expenses:
        print(f"Category: {expense.category}, Amount: {expense.amount}, Date: {expense.date}")
    
    print("-----------------------------------")
    tracker.menu()