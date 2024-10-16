# File to store expense data
DATA_FILE = "expenses.txt"

# Initialize data structure
expenses = []

# Load existing data
def load_data():
    global expenses
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                amount, category, date = line.strip().split(",")
                expenses.append({"amount": float(amount), "category": category, "date": date})
    except FileNotFoundError:
        pass

# Save data
def save_data():
    with open(DATA_FILE, "w") as file:
        for expense in expenses:
            file.write(f"{expense['amount']},{expense['category']},{expense['date']}\n")

# Add expense
def add_expense():
    amount = float(input("Enter amount: $"))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    save_data()
    print("Expense added successfully!")

# View summaries
def view_summaries():
    total_spending = sum(expense["amount"] for expense in expenses)
    print("Total overall spending: $", total_spending)
    
    categories = {}
    for expense in expenses:
        category = expense["category"]
        if category in categories:
            categories[category] += expense["amount"]
        else:
            categories[category] = expense["amount"]
    print("Total spending by category:")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")
    
    # Daily summary
    daily_spending = {}
    for expense in expenses:
        date = expense["date"]
        if date in daily_spending:
            daily_spending[date] += expense["amount"]
        else:
            daily_spending[date] = expense["amount"]
    print("Daily spending:")
    for date, amount in daily_spending.items():
        print(f"{date}: ${amount}")

# Delete expense
def delete_expense():
    index = int(input("Enter expense index to delete: ")) - 1
    if index < len(expenses):
        del expenses[index]
        save_data()
        print("Expense deleted successfully!")
    else:
        print("Invalid index.")

# Edit expense
def edit_expense():
    index = int(input("Enter expense index to edit: ")) - 1
    if index < len(expenses):
        expense = expenses[index]
        print("Enter new values (press Enter to keep current value):")
        expense["amount"] = float(input(f"Amount (${expense['amount']}): ") or expense["amount"])
        expense["category"] = input(f"Category ({expense['category']}): ") or expense["category"]
        expense["date"] = input(f"Date ({expense['date']}): ") or expense["date"]
        save_data()
        print("Expense updated successfully!")
    else:
        print("Invalid index.")

# Main menu
def main_menu():
    load_data()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summaries")
        print("3. Delete Expense")
        print("4. Edit Expense")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summaries()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            edit_expense()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main_menu()
