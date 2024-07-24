import json
import os

# File path for storing data
DATA_FILE = "expenses.json"

# Initialize expenses dictionary to store data
expenses = {}

# Load existing data from file if available
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        expenses = json.load(file)

# Function to save expenses data to file
def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add an expense
def add_expense(category, amount):
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]
    print(f"Added ${amount} to {category} expenses.")
    save_data()

# Function to view expenses by category
def view_expenses():
    for category, amounts in expenses.items():
        total = sum(amounts)
        print(f"{category}: ${total}")

# Function to generate a report of total expenses
def generate_report():
    total_expenses = sum(sum(amounts) for amounts in expenses.values())
    print(f"Total expenses: ${total_expenses}")

# Function to handle user input with error handling
def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except KeyboardInterrupt:
            print("\nOperation interrupted. Try again.")
        except Exception as e:
            print(f"Error: {str(e)}. Try again.")

# Function to get float input with error handling
def get_float_input(prompt):
    while True:
        try:
            user_input = float(get_user_input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"Error: {str(e)}. Try again.")

# Function to display main menu and handle user choices
def main_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report")
    print("4. Exit")

    choice = get_user_input("Enter your choice (1-4): ")

    if choice == '1':
        category = get_user_input("Enter expense category: ")
        amount = get_float_input("Enter amount spent: $")
        add_expense(category, amount)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        generate_report()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

# Main function to run the program
def main():
    print("Welcome to Expense Tracker!")

    while True:
        main_menu()

if __name__ == "__main__":
    main()
