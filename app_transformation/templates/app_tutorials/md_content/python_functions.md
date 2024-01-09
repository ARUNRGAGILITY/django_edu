<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Python Functions</b>
<br>
# Python Functions

Functions are a fundamental concept in Python, and understanding various aspects of them is crucial. 
Here, we are providing examples that cover nested functions, pass by value, pass by reference, different types of arguments (positional and keyword), and the use of `*args` and `**kwargs` for beginners to learn Python functions in-depth.

**1. Nested Functions:**

Nested functions are functions defined inside other functions.

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
result = add_five(3)
print(result)  # Output: 8
```

**2. Pass by Value vs. Pass by Reference:**

In Python, arguments are passed by object reference. Mutable objects (e.g., lists) can be modified within functions, while immutable objects (e.g., integers) cannot.

```python
def modify_list(my_list):
    my_list.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

def modify_int(x):
    x = x + 1

my_var = 5
modify_int(my_var)
print(my_var)  # Output: 5
```



In Python, all arguments are passed by object reference. 
However, there can be a misconception about "pass by value" and "pass by reference" in Python. 
In reality, Python uses a mechanism that can be thought of as "pass by object reference."

Here's an example that illustrates the concept of "pass by object reference" in Python and provides comments to explain it:

```python
# Function to demonstrate pass by object reference
def modify_list(lst):
    # Within this function, lst is a reference to the same list object as the original list
    print("Inside modify_list - Before Modification:", lst)

    # Modifying the list in-place
    lst.append(4)
    lst[0] = 99

    print("Inside modify_list - After Modification:", lst)

# Main program
my_list = [1, 2, 3]

print("Before calling modify_list:", my_list)

# Call the function, passing the reference to the list
modify_list(my_list)

print("After calling modify_list:", my_list)
```

Output:
```
Before calling modify_list: [1, 2, 3]
Inside modify_list - Before Modification: [1, 2, 3]
Inside modify_list - After Modification: [99, 2, 3, 4]
After calling modify_list: [99, 2, 3, 4]
```

Explanation:
1. We define a function `modify_list(lst)` that takes a list as an argument.
2. In the main program, we have a list called `my_list` with the values `[1, 2, 3]`.
3. Before calling the `modify_list` function, we print the original list.
4. We call the `modify_list` function, passing `my_list` as an argument. This passes a reference to the same list object.
5. Inside the `modify_list` function, we modify the list by appending `4` and changing the first element to `99`.
6. After returning from the function, we print the list again in the main program, and it reflects the changes made inside the function.

Key Points:
- In Python, when you pass a mutable object like a list to a function, changes made to the object inside the function affect the original object.
- This behavior is because the function receives a reference to the same object, not a copy of the object.
- In contrast, immutable objects like integers and strings cannot be modified in-place. If you assign a new value to an immutable object inside a function, it won't affect the original object.

Remember that while Python uses "pass by object reference," the concept of "pass by value" and "pass by reference" 
is not the most accurate way to describe Python's argument passing mechanism. 
It's better to think of it as passing references to objects rather than values or references in the traditional sense.


**3. Positional Arguments:**

Positional arguments are passed in the order defined in the function signature.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

**4. Keyword Arguments:**

Keyword arguments are passed with explicit parameter names.

```python
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet(age=25, name="Alice")
# Output: Hello, Alice. You are 25 years old.
```

**5. `*args` (Variable-Length Positional Arguments):**

`*args` allows a function to accept a variable number of positional arguments as a tuple.

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4)
print(result)  # Output: 10
```

**6. `**kwargs` (Variable-Length Keyword Arguments):**

`**kwargs` allows a function to accept a variable number of keyword arguments as a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, country="USA")
# Output:
# name: Alice
# age: 25
# country: USA
```

These examples should provide a solid foundation for understanding Python functions, including their various features and use cases. 
Experiment with these concepts to gain a deeper understanding of Python's function capabilities.


# Python Functions as Building Blocks

Certainly! Here are some Python project ideas that involve functions, calling functions, and passing arguments to construct larger programs. These projects will help you practice and reinforce your understanding of functions while building more complex applications step by step:

**1. To-Do List Manager:**
   Create a command-line to-do list manager. Implement functions for adding tasks, marking tasks as complete, deleting tasks, and displaying the list. Use functions to organize the code.

**2. Calculator:**
   Build a basic calculator that can perform arithmetic operations like addition, subtraction, multiplication, and division. Define functions for each operation and call them based on user input.

**3. Simple Inventory System:**
   Create an inventory system for tracking items. Write functions to add new items, update item quantities, display the inventory, and generate reports. Use functions to manage different aspects of the inventory.

**4. Student Grade Tracker:**
   Develop a program for tracking student grades. Create functions to input student information, calculate grades, display student data, and generate reports. Use functions to modularize the code.

**5. Text-Based Adventure Game:**
   Design a text-based adventure game with multiple scenarios and choices. Implement functions to handle different game states, user choices, and outcomes. Functions can represent various game interactions.

**6. Weather App:**
   Build a weather application that fetches weather data from an API. Define functions for fetching data, parsing JSON responses, and displaying weather information. Use functions to organize the code logic.

**7. URL Shortener:**
   Create a URL shortening service. Define functions for shortening long URLs and expanding short URLs. Functions can handle the conversion and database operations.

**8. Contact Management System:**
   Develop a contact management system. Write functions for adding contacts, searching for contacts, updating contact information, and deleting contacts. Functions can manage the contact database.

**9. Bookstore Inventory:**
   Build a program for managing a bookstore's inventory. Implement functions for adding books, updating book details, searching for books, and generating sales reports. Functions can handle inventory operations.

**10. Expense Tracker:**
    Create an expense tracking application. Define functions for adding expenses, categorizing expenses, calculating totals, and generating expense reports. Functions can help manage financial data.

These projects provide opportunities to practice using functions effectively in larger programs. As you work on these projects, you'll learn how to modularize your code, improve code reusability, and create more organized and maintainable applications.


# Python Functions code library (Examples)

Code library for the projects mentioned above

**1. To-Do List Manager:**

```python
# Define a list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added!")

# Function to display tasks
def display_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks to display.")

# Function to mark a task as complete
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] += " (Completed)"
        print("Task marked as complete!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted!")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task number to mark as complete: "))
        complete_task(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task number to delete: "))
        delete_task(task_index)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
```

**2. Calculator:**

```python
# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

while True:
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '5':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please try again.")
```

These are simplified versions of the projects to get you started. 

**3. Simple Inventory System:**

```python
# Define an inventory as a dictionary
inventory = {}

# Function to add an item to the inventory
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"{quantity} {item_name}(s) added to inventory.")

# Function to update item quantity
def update_item(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print(f"{item_name} quantity updated.")
    else:
        print(f"{item_name} not found in inventory.")

# Function to display the inventory
def display_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

while True:
    print("\nSimple Inventory System")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. Display Inventory")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '4':
        break

    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_item(item_name, quantity)
    elif choice == '2':
        item_name = input("Enter item name to update: ")
        new_quantity = int(input("Enter new quantity: "))
        update_item(item_name, new_quantity)
    elif choice == '3':
        display_inventory()
    else:
        print("Invalid choice. Please try again.")
```

**4. Student Grade Tracker:**

```python
# Define a dictionary to store student information
students = {}

# Function to add student information
def add_student(name, grade):
    students[name] = grade
    print(f"{name}'s grade added.")

# Function to calculate and display student grades
def display_grades():
    if students:
        print("Student Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No student grades to display.")

while True:
    print("\nStudent Grade Tracker")
    print("1. Add Student Grade")
    print("2. Display Student Grades")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '3':
        break

    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        add_student(name, grade)
    elif choice == '2':
        display_grades()
    else:
        print("Invalid choice. Please try again.")
```



**7. URL Shortener:**

```python
# Define a dictionary to store short URLs and their corresponding long URLs
url_dict = {}

# Function to shorten a URL
def shorten_url(long_url):
    short_url = hash(long_url) % (10**8)  # Generate a short URL using a hash function
    url_dict[short_url] = long_url
    return short_url

# Function to expand a short URL
def expand_url(short_url):
    if short_url in url_dict:
        return url_dict[short_url]
    else:
        return "Short URL not found."

while True:
    print("\nURL Shortener")
    print("1. Shorten URL")
    print("2. Expand URL")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '3':
        break

    if choice == '1':
        long_url = input("Enter the long URL to shorten: ")
        short_url = shorten_url(long_url)
        print(f"Shortened URL: {short_url}")
    elif choice == '2':
        short_url = int(input("Enter the short URL to expand: "))
        long_url = expand_url(short_url)
        print(f"Expanded URL: {long_url}")
    else:
        print("Invalid choice. Please try again.")
```

**8. Contact Management System:**

```python
# Define a dictionary to store contact information
contacts = {}

# Function to add a contact
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        return f"Contact: {name}, Phone: {contacts[name]}"
    else:
        return "Contact not found."

# Function to update a contact
def update_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Contact '{name}' updated.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '5':
        break

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        name = input("Enter contact name to search: ")
        result = search_contact(name)
        print(result)
    elif choice == '3':
        name = input("Enter contact name to update: ")
        new_phone = input("Enter new phone number: ")
        update_contact(name, new_phone)
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    else:
        print("Invalid choice. Please try again.")
```


**9. Bookstore Inventory:**

```python
# Define a dictionary to store book information
inventory = {}

# Function to add a book to the inventory
def add_book(title, author, quantity):
    book_info = {"author": author, "quantity": quantity}
    inventory[title] = book_info
    print(f"Book '{title}' added to inventory.")

# Function to update book quantity
def update_quantity(title, new_quantity):
    if title in inventory:
        inventory[title]["quantity"] = new_quantity
        print(f"Quantity for book '{title}' updated.")
    else:
        print(f"Book '{title}' not found in inventory.")

# Function to search for a book
def search_book(title):
    if title in inventory:
        book_info = inventory[title]
        author = book_info["author"]
        quantity = book_info["quantity"]
        return f"Title: {title}, Author: {author}, Quantity: {quantity}"
    else:
        return f"Book '{title}' not found in inventory."

# Function to display the entire inventory
def display_inventory():
    if inventory:
        print("Inventory:")
        for title, book_info in inventory.items():
            author = book_info["author"]
            quantity = book_info["quantity"]
            print(f"Title: {title}, Author: {author}, Quantity: {quantity}")
    else:
        print("Inventory is empty.")

while True:
    print("\nBookstore Inventory")
    print("1. Add Book")
    print("2. Update Book Quantity")
    print("3. Search Book")
    print("4. Display Inventory")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '5':
        break

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        quantity = int(input("Enter book quantity: "))
        add_book(title, author, quantity)
    elif choice == '2':
        title = input("Enter book title to update quantity: ")
        new_quantity = int(input("Enter new quantity: "))
        update_quantity(title, new_quantity)
    elif choice == '3':
        title = input("Enter book title to search: ")
        result = search_book(title)
        print(result)
    elif choice == '4':
        display_inventory()
    else:
        print("Invalid choice. Please try again.")
```

**10. Expense Tracker:**

```python
# Define a list to store expense records
expenses = []

# Function to add an expense record
def add_expense(date, description, amount):
    expense_record = {"date": date, "description": description, "amount": amount}
    expenses.append(expense_record)
    print("Expense added.")

# Function to calculate and display total expenses
def calculate_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    return total

# Function to display the list of expenses
def display_expenses():
    if expenses:
        print("Expense Records:")
        for expense in expenses:
            date = expense["date"]
            description = expense["description"]
            amount = expense["amount"]
            print(f"Date: {date}, Description: {description}, Amount: {amount}")
        print(f"Total Expenses: {calculate_total_expenses()}")
    else:
        print("No expense records to display.")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '3':
        break

    if choice == '1':
        date = input("Enter expense date (YYYY-MM-DD): ")
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        add_expense(date, description, amount)
    elif choice == '2':
        display_expenses()
    else:
        print("Invalid choice. Please try again.")
```

