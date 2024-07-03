import sqlite3
import csv
import os
import time
from datetime import datetime

# Structure to store expense details
class Expense:
    def __init__(self, id, date, amount, category, description):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

# List to store all expenses
expenses = []

# Database connection
db = None
ID = 0

def connection():
    global db
    db = sqlite3.connect('expense.db')
    if db:
        print("\nDatabase connection successful")
    else:
        print("\nCan't open database")

def table_creation():
    query = """
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        description TEXT
    );
    """
    try:
        db.execute(query)
        db.commit()
        print("\nTable created successfully\n")
    except sqlite3.Error as e:
        print("\nError creating table: ", e)

def insert_r():
    query = "INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)"
    try:
        for expense in expenses:
            db.execute(query, (expense.date, expense.amount, expense.category, expense.description))
        db.commit()
        print("\nData Inserted Successfully!\n")
    except sqlite3.Error as e:
        print("\nError inserting data: ", e)

def retrieve():

    query = "SELECT id, date, amount, category, description FROM expenses"
    try:
        print("\nRetrieved expense data from Database ")
        print("--------------------------------------\n")
        cursor = db.execute(query)
        print("ID | Date               | Amount        | Category               | Description")
        print("----------------------------------------------------------------------------------------")
        for row in cursor:
            print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4])
    except sqlite3.Error as e:
        print("Error: ", e)

# Function to check if a string is a number
def is_number(string):
    return string.isdigit()

# Function to check if a string is a valid amount (numeric value with at most one dot)
def is_valid_amount(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Function to get the current date and time as a string
def get_current_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to add an expense to the list
def add_expense():
    global ID
    print("\nAdd Expense\n--------------------")
    
    valid_input = False
    while not valid_input:
        amount = input("Enter the amount: ")
        if is_valid_amount(amount):
            amount = float(amount)
            valid_input = True
        else:
            print("Invalid amount! Please enter a valid numeric value")
   
    
    while True:
        category = input("Enter the category: ").strip()
        if category:
            break
        else:
            print("Category cannot be empty. Please enter a valid category!")
        

    description = input("Enter the description (optional): ").strip()
    date = get_current_date_time()
    ID += 1
    expense = Expense(ID, date, amount, category, description)
    expenses.append(expense)
    print("\nExpense added successfully!\n")

# Function to display all expenses
def display_expenses():
    print("\nExpense List:\n-----------------\n")
    print("ID | Date               | Amount        | Category               | Description")
    print("----------------------------------------------------------------------------------------")
    for expense in expenses:
        print(f"{expense.id} | {expense.date} | {expense.amount:<14} | {expense.category:<23} | {expense.description}")

# Function to save expenses to a CSV file
def save_expenses_to_csv():
    while True:
        filename = input("\nEnter the filename to save: ").strip()
        if filename.endswith('.csv'):
            break
        else:
            print("\nInvalid File Format!\nFile extension must be \".csv\"")
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            for expense in expenses:
                writer.writerow([expense.date, expense.amount, expense.category, expense.description])
        print(f"\nExpenses data saved successfully to '{filename}'!\n")
    except IOError as e:
        print(f"\nFailed to open file for writing: {e}")

def main():
    global db
    while True:
        print("\nExpense Tracker Menu:\n--------------------")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Save Expenses to CSV")
        print("4. Integrate database to store and retrieve expense data.")
        print("5. Exit")
        choice = input("\nEnter your choice (1/2/3/4/5): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            save_expenses_to_csv()
        elif choice == '4':
            while True:
                print("\nIntegrate database Menu:\n----------------------")
                print("1. Create a database table")
                print("2. Store data in database table")
                print("3. Retrieve expense data from database table")
                print("4. Exit")
                db_choice = input("\nEnter your choice (1/2/3/4): ").strip()

                if db_choice == '1':
                    connection()
                    table_creation()
                elif db_choice == '2':
                    connection()
                    insert_r()
                    db.close()
                elif db_choice == '3':
                    connection()
                    retrieve()
                    db.close()
                elif db_choice == '4':
                    print("\nThank you for using the database integration menu\n")
                    break
                else:
                    print("\nInvalid choice! Please enter a number between 1 and 4.\n")
        elif choice == '5':
            print("\nExiting the Expense Tracker. Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
