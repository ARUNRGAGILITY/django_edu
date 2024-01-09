<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Python Foundations</b>
<br>

# Python Foundations

### 1. Variables and Data Types
Python supports various data types:
```python
# Variables and data types
name = "Alice"           # String
age = 30                 # Integer
height = 5.6             # Float
is_student = True        # Boolean
```

### 2. Basic Operations
Performing operations in Python:
```python
# Basic operations
result = 10 + 5          # Addition
difference = 20 - 8      # Subtraction
product = 6 * 4          # Multiplication
quotient = 15 / 3        # Division
remainder = 10 % 3       # Modulo (remainder)
```

### 3. Control Structures
Using if-else statements:
```python
# Control structures
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### 4. Loops
Using for and while loops:
```python
# Loops
for i in range(5):
    print(i)             # Prints numbers 0 to 4

counter = 0
while counter < 5:
    print(counter)
    counter += 1         # Prints numbers 0 to 4
```

### 5. Functions
Creating and using functions:
```python
# Functions
def greet(name):
    print("Hello,", name)

greet("Bob")             # Calls the function with an argument
```

### 6. Lists and Dictionaries
Working with collections:
```python
# Lists and dictionaries
my_list = [1, 2, 3, 4]                  # List
print(my_list[0])                       # Accessing elements

my_dict = {"name": "Alice", "age": 30}  # Dictionary
print(my_dict["name"])                  # Accessing values by keys
```

### 7. Input/Output
Taking user input and displaying output:
```python
# Input/Output
user_input = input("Enter your name: ")
print("Hello,", user_input)
```

Absolutely, let's delve deeper into more advanced Python topics:

### Functions
Functions encapsulate reusable code:
```python
# Functions
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)   # Calling the function
print(result)                # Output: 8
```

### Collections (Tuples and Sets)
Tuples and sets in Python:
```python
# Tuples and sets
my_tuple = (1, 2, 3)       # Tuple
print(my_tuple[0])         # Accessing elements

my_set = {1, 2, 3, 3}     # Set
print(my_set)              # Output: {1, 2, 3} (sets don't allow duplicates)
```

### Object-Oriented Programming (OOP)
Creating classes and objects in Python:
```python
# Object-Oriented Programming (OOP)
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance (object) of the class
my_dog = Dog("Buddy", 3)
my_dog.bark()          # Output: Buddy says Woof!
```

### Exceptions
Handling exceptions in Python:
```python
# Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### File I/O
Reading and writing to files:
```python
# File I/O
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text.")  # Writing to a file

with open("example.txt", "r") as file:
    content = file.read()                        # Reading from a file
    print(content)                               # Output: Hello, this is a sample text.
```

