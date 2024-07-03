# Expense Tracker

## Objective
Develop an expense tracker application that allows users to log their expenses, categorize them, and view summaries. The application should store expense data in a CSV file without the use of a database. Additionally, implement input validation to ensure users enter a valid numeric amount.

## Features
### Add Expense:
- Users can add a new expense by entering the amount, category, and an optional description.
- The application records the date and time of each expense.

### Display Expenses:
- Users can view a list of all recorded expenses, including details such as date, amount, category, and description.
- The display is user-friendly, presenting the data in a readable format.

### Save Expenses to CSV:
- When choosing to save expenses, the application prompts users to input the filename for saving.
- The CSV file includes a header row and organizes the data in columns (e.g., Date, Amount, Category, Description).

### User Interaction:
- The application provides a simple console-based user interface.
- Users can navigate through the menu to perform actions such as adding expenses, displaying expenses, saving to the CSV file, and exiting the application.

### Input Validation:
- When entering the amount, input validation ensures users provide a valid numeric value.
- Users are continuously prompted for input until a valid numeric amount is entered.

### Error Handling:
- Basic error handling is implemented to manage unexpected scenarios.
- Appropriate error messages are displayed to users when necessary.

## Bonus
Integrate an SQLite database to store and retrieve expense data.
Create a table named `expenses` with columns for `id`, `date`, `amount`, `category`, and `description`.

## Implementation
- Use Python or any other programming language for the implementation.
- Utilize the datetime module to record the date and time of expenses.
- Use the csv module for saving and loading data in CSV format.
- Organize the code into functions for modularity and readability.

## Constraints
- The CSV file should be human-readable, and the format should be simple and well-organized.
- The application should be console-based, and the user interface should be easy to understand.




## Sample
### Input:
```plaintext
Expense Tracker Menu:
1. Add Expense
2. Display Expenses
3. Save Expenses to CSV
4. Exit

Enter your choice (1/2/3/4): 1
Enter the amount: 25.5
Enter the category: Groceries
Enter the description (optional): Monthly grocery shopping

Expense Tracker Menu:
1. Add Expense
2. Display Expenses
3. Save Expenses to CSV
4. Exit

Enter your choice (1/2/3/4): 2

Expense List:
ID | Date                  | Amount | Category  | Description
-------------------------------------------------------------
1  | 2022-02-22 15:30:00  | 25.5   | Groceries | Monthly grocery shopping

Expense Tracker Menu:
1. Add Expense
2. Display Expenses
3. Save Expenses to CSV
4. Exit

Enter your choice (1/2/3/4): 3
Enter the filename to save: expenses.csv
Expenses saved successfully to 'expenses.csv'!

Expense Tracker Menu:
1. Add Expense
2. Display Expenses
3. Save Expenses to CSV
4. Exit

Enter your choice (1/2/3/4): 4
Exiting the Expense Tracker. Goodbye!