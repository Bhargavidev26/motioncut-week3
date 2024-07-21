# Initialize an empty list to store expenses
all_expenses = []

# Define a function to get expense input from the user
def get_expense_input():
    amount = float(input("Enter the expense amount: "))
    description = input("Enter a brief description: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    return {"amount": amount, "description": description, "date": date}

# Define a function to add an expense to the list
def add_expense(expense):
    all_expenses.append(expense)

# Define expense categories (you can add more as needed)
expense_categories = {
    "food": [],
    "transportation": [],
    "entertainment": [],
}

# Define a function to categorize an expense
def categorize_expense(expense):
    category = input("Enter the expense category: ").lower()
    if category in expense_categories:
        expense_categories[category].append(expense)
    else:
        print("Invalid category. Please choose from:", list(expense_categories.keys()))

# Define a function to display all expenses
def display_expenses():
    for category, expenses in expense_categories.items():
        print(f"{category.capitalize()} expenses:")
        for expense in expenses:
            print(f"  Amount: {expense['amount']} | Description: {expense['description']}")

# Main loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add an expense")
    print("2. Display expenses")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        expense_data = get_expense_input()
        add_expense(expense_data)
        categorize_expense(expense_data)
        print("Expense added successfully!")
    elif choice == "2":
        display_expenses()
    elif choice == "3":
        print("Exiting Expense Tracker. Have a great day!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# End of the program