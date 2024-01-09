<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Python Introduction</b>
<br>
# Python Introduction
<a id="table-of-contents"></a>
- [Python Introduction](#python-introduction)
        - [Python Quick Introduction](#python-quick-introduction)
        - [Python Output statement](#python-output-statement)
        - [Python Variables](#python-variables)
        - [Python List, Tuple, Set, Dictionary comparison](#python-list-tuple-set-dictionary-comparison)
        - [Python Operators](#python-operators)
        - [Python Control Statements](#python-control-statements)
          - [`if`, `elif`, and `else` Examples:](#if-elif-and-else-examples)
          - [`match case` Examples (Python 3.10+):](#match-case-examples-python-310)
        - [Python Loops (for and while loop)](#python-loops-for-and-while-loop)
          - [`for` Loop Examples:](#for-loop-examples)
          - [Example 1: Using `for` Loop with `else`](#example-1-using-for-loop-with-else)
          - [Example 2: Using `for` Loop to Check for Prime Numbers](#example-2-using-for-loop-to-check-for-prime-numbers)
          - [`while` Loop Examples:](#while-loop-examples)
        - [Python Object-Oriented Programming](#python-object-oriented-programming)
    - [Basic OOP Example:](#basic-oop-example)
        - [Python OOP example with Car](#python-oop-example-with-car)
        - [More OOP Operations](#more-oop-operations)
        - [Python Test-First Development](#python-test-first-development)
        - [Python Collections Classes](#python-collections-classes)
        - [Python Another quick reference of Sequential data-types (List, Tuple, Set, Dictionary)](#python-another-quick-reference-of-sequential-data-types-list-tuple-set-dictionary)
        - [Python references](#python-references)


##### Python Quick Introduction
Here is a quick Introduction of Python Programming Language

Python is a high-level, versatile, and dynamically-typed programming language that was created by Guido van Rossum and first released in 1991. It is known for its simplicity, readability, and elegant syntax, which make it an excellent choice for both beginners and experienced developers. Python's design philosophy emphasizes code readability and encourages developers to write clear, concise, and easily maintainable code.

Key features of Python include:

1. **Easy-to-Read Syntax:** Python uses indentation (whitespace) to define code blocks, making it visually clear and reducing the need for curly braces or other delimiters. This feature helps maintain consistent and readable code.

2. **High-Level Language:** Python provides a high-level abstraction that simplifies complex tasks. Developers can focus on solving problems without needing to worry about low-level details.

3. **Interpreted Language:** Python is an interpreted language, meaning that code is executed line by line by an interpreter rather than being compiled into machine code. This makes development and debugging easier and more interactive.

4. **Dynamic Typing:** Python is dynamically typed, which means that variable types are determined at runtime. This flexibility makes Python forgiving and easy to use but requires attention to data types.

5. **Extensive Standard Library:** Python comes with a comprehensive standard library that includes modules and packages for various tasks, such as file I/O, networking, web development, and data manipulation. This rich ecosystem simplifies development and reduces the need for reinventing the wheel.

6. **Cross-Platform Compatibility:** Python is available on various platforms, including Windows, macOS, and Linux. It supports a wide range of hardware architectures, making it highly portable.

7. **Community and Ecosystem:** Python has a large and active community of developers who contribute to its growth. This community-driven development has resulted in a vast ecosystem of libraries, frameworks, and tools for various domains, including web development, data analysis, machine learning, and more.

8. **Open Source:** Python is open-source software, meaning that its source code is freely available for anyone to view, modify, and distribute. This open nature has contributed to Python's widespread adoption and continuous improvement.

Python is used in a wide range of applications, including web development (using frameworks like Django and Flask), data analysis and visualization (with libraries like NumPy and Matplotlib), machine learning and artificial intelligence (using libraries like TensorFlow and PyTorch), scientific computing, automation, scripting, and more.

In summary, Python is a powerful and versatile programming language known for its simplicity, readability, and extensive ecosystem. Whether you're a beginner or an experienced developer, Python is an excellent choice for a wide range of programming tasks.

[Go Back to Table of Contents](#table-of-contents)

##### Python Output statement 

In Python, you can use the `print()` function to display output to the console. Here are some examples of Python output statements:

* Printing Text:
```python
print("Hello, World!")  # Prints the string "Hello, World!"
```

* Printing Variables:
```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Prints variable values along with text
```

* Printing Numbers and Expressions:
```python
x = 5
y = 10
sum_result = x + y
print("Sum:", sum_result)  # Prints the result of an expression
```

* Formatting Output:
   You can format the output using f-strings or the `str.format()` method.
```python
name = "Bob"
age = 25
print(f"Name: {name}, Age: {age}")  # Using f-strings
print("Name: {}, Age: {}".format(name, age))  # Using str.format()
```

* Printing Multiple Lines:
   You can use triple-quoted strings for multi-line output.
```python
message = """
This is a multi-line
message in Python.
"""
print(message)
```

Here is a simple summary of all the output, comments, basic data types, input 

```python
## Python Basics

## Python Output Statement
print("Hello from Python!")

## Python Output Statement / Print Statement
name = "John"
last_name = "Smith"
print("Welcome ", name, last_name)


## Python Comments

# This is a single line comment

'''
This is a multi-line comment
Here we can enter some description of the program
Here you enter some description
'''


## Python Basic Data Types
int_var = 10
float_var = 20.01
boolean_var = True
string_var = "String variable"
complex_num_var = 5 + 2j

print_string = f"""
====================================
int_var: {int_var}
float_var: {float_var}
boolean_var: {boolean_var}
string_var: {string_var}
complex_num_var: {complex_num_var}
====================================
"""

print(f"Printing the Basic Data Types:  {print_string}")

## Creating Variable Names with some meaning for recognition
name = "John"
age = 40
bank_balance = 1000223.11
city = "New York"
occupation = "Engineer"
work_history = ["Company ABC", "Company 123", "Company 456"]

## Python Input statement
get_name = input("Enter your Name: ")
print(f"User's Name is: {get_name}")

## Python identify the type of variable
get_name = input("Enter your Name: ")
type_of_var = type(get_name)
print(f"User's Name is: {get_name} is of Type: {type_of_var}")
```


* Printing Lists and Iterables:
```
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)  # Prints the list
```

* Printing Using a Loop:
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)  # Prints each number in the list
```

* Redirecting Output:
You can redirect the output to a file using the `sys.stdout` object.
```python
import sys
with open("output.txt", "w") as file:
    sys.stdout = file
    print("This will be written to output.txt")
    sys.stdout = sys.__stdout__  # Reset the output to the console
```

These are some basic examples of how to use the `print()` function in Python to display output. You can use it to showcase results, debug your code, or provide information to users when developing Python programs.

[Go Back to Table of Contents](#table-of-contents)

##### Python Variables

 Here are 10 examples of Python variables:

1. **Integer Variable:**
```python
age = 25
```

2. **Float Variable:**
```python
price = 12.99
```

3. **String Variable:**
```python
name = "Alice"
```

4. **Boolean Variable:**
```python
is_student = True
```

5. **List Variable:**
```python
fruits = ["apple", "banana", "cherry"]
```

6. **Tuple Variable:**
```python
coordinates = (3.0, 4.5)
```

7. **Dictionary Variable:**
```python
person = {"name": "Bob", "age": 30}
```

8. **Set Variable:**
```python
unique_numbers = {1, 2, 3, 4, 5}
```

9. **NoneType Variable:**
```python
result = None
```

10. **Custom Object Variable:**
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Camry")
```

These examples cover various types of Python variables, including numbers (integers and floats), strings, booleans, collections (lists, tuples, dictionaries, and sets), the special `None` value, and custom objects. Python is dynamically typed, so you don't need to declare variable types explicitly. You can assign values of different types to variables as needed.

[Go Back to Table of Contents](#table-of-contents)

##### Python List, Tuple, Set, Dictionary comparison

Here's a comparison of Python's List, Tuple, Set, and Dictionary in a tabular format, along with code examples and their key differences:

| Data Structure | Declaration | Mutable | Ordered | Duplicate Values | Example |
|----------------|-------------|---------|---------|-------------------|---------|
| List           | `my_list = [1, 2, 3]` | Yes | Yes | Yes | `numbers = [1, 2, 3]` |
| Tuple          | `my_tuple = (1, 2, 3)` | No | Yes | Yes | `coordinates = (3, 4)` |
| Set            | `my_set = {1, 2, 3}` | Yes | No | No | `unique_numbers = {1, 2, 3}` |
| Dictionary     | `my_dict = {"key": "value"}` | Yes (for values) | Yes (since Python 3.7) | Yes (for keys) | `person = {"name": "Alice", "age": 25}` |

Here are explanations and code examples for each data structure:

**List:**
- Declaration: `my_list = [1, 2, 3]`
- Mutable: Yes
- Ordered: Yes (Maintains the order of elements)
- Duplicate Values: Allowed
- Example: `numbers = [1, 2, 3]`

**Tuple:**
- Declaration: `my_tuple = (1, 2, 3)`
- Mutable: No (Immutable)
- Ordered: Yes (Maintains the order of elements)
- Duplicate Values: Allowed
- Example: `coordinates = (3, 4)`

**Set:**
- Declaration: `my_set = {1, 2, 3}`
- Mutable: Yes (for adding/removing elements)
- Ordered: No (Unordered collection)
- Duplicate Values: Not allowed (Automatically removes duplicates)
- Example: `unique_numbers = {1, 2, 3}`

**Dictionary:**
- Declaration: `my_dict = {"key": "value"}`
- Mutable: Yes (for values, keys are immutable)
- Ordered: Yes (since Python 3.7, and guaranteed in Python 3.7+)
- Duplicate Values: Not allowed for keys (Keys must be unique)
- Example: `person = {"name": "Alice", "age": 25}`

Each of these data structures has its own characteristics and use cases. Lists are versatile and allow duplicates, tuples are immutable and ordered, sets are used for unique values, and dictionaries store key-value pairs.

Remember that Python 3.7 and later versions maintain insertion order for dictionaries. In earlier versions of Python, dictionaries were unordered collections.


[Go Back to Table of Contents](#table-of-contents)
##### Python Operators
Python supports various types of operators that are used to perform operations on variables and values. Here are some of the different types of operators in Python with examples:

**Arithmetic Operators:**
   - Used for mathematical calculations.
   
```python
a = 10
b = 5

# Addition
result = a + b  # Result: 15

# Subtraction
result = a - b  # Result: 5

# Multiplication
result = a * b  # Result: 50

# Division
result = a / b  # Result: 2.0 (float division)

# Floor Division
result = a // b  # Result: 2 (integer division)

# Modulus (Remainder)
result = a % b   # Result: 0

# Exponentiation
result = a ** b  # Result: 100000
```

**Comparison (Relational) Operators:**
   - Used to compare values.
   
```python
a = 10
b = 5

# Equal to
result = a == b  # Result: False

# Not equal to
result = a != b  # Result: True

# Greater than
result = a > b   # Result: True

# Less than
result = a < b   # Result: False

# Greater than or equal to
result = a >= b  # Result: True

# Less than or equal to
result = a <= b  # Result: False
```

**Logical Operators:**
   - Used to combine and manipulate logical values (`True` or `False`).
   
```python
x = True
y = False

# Logical AND
result = x and y  # Result: False

# Logical OR
result = x or y   # Result: True

# Logical NOT
result = not x    # Result: False
```

**Assignment Operators:**
   - Used to assign values to variables.
   
```python
x = 5
y = 10

# Addition assignment
x += y  # Equivalent to x = x + y

# Subtraction assignment
x -= y  # Equivalent to x = x - y

# Multiplication assignment
x *= y  # Equivalent to x = x * y

# Division assignment
x /= y  # Equivalent to x = x / y
```

**Bitwise Operators:**
   - Used for bitwise operations on integers.
   
```python
a = 5
b = 3

# Bitwise AND
result = a & b  # Result: 1

# Bitwise OR
result = a | b  # Result: 7

# Bitwise XOR
result = a ^ b  # Result: 6

# Bitwise NOT
result = ~a     # Result: -6 (Note: Result is a two's complement)
```

**Membership Operators:**
   - Used to test if a value is a member of a sequence.
   
```python
sequence = [1, 2, 3, 4, 5]

# Membership (in)
result = 3 in sequence  # Result: True

# Membership (not in)
result = 6 not in sequence  # Result: True
```

**Identity Operators:**
   - Used to compare object identities.
   
```python
x = [1, 2, 3]
y = x

# Identity (is)
result = x is y  # Result: True

# Identity (is not)
result = x is not y  # Result: False
   ```

**Ternary (Conditional) Operator:**
   - Used for conditional expressions.
   
```python
a = 10
b = 5

# Ternary operator
max_value = a if a > b else b  # Result: 10
```

These are some of the primary operators in Python, each serving a specific purpose in various programming scenarios.
[Go Back to Table of Contents](#table-of-contents)

##### Python Control Statements

Here are examples of Python `if`, `elif`, `else`, and `match case` control statements to demonstrate their usage in various scenarios:

###### `if`, `elif`, and `else` Examples:

**Basic `if` Statement:**
```python
# Check the person in the theme park by age
age = 18
if age >= 18:
      print("You are an adult.")
```

**`if`-`else` Statement:**
```python
temperature = 25
if temperature > 30:
      print("It's hot outside.")
else:
      print("It's not too hot.")
```

**`if`-`elif`-`else` Statement:**
```python
score = 85
if score >= 90:
      print("A grade")
elif score >= 80:
      print("B grade")
else:
      print("C grade or below")
```

**Nested `if` Statements:**
```python
age = 25
if age >= 18:
      if age < 60:
         print("You are an adult, not a senior.")
      else:
         print("You are a senior citizen.")
else:
      print("You are a minor.")
```

###### `match case` Examples (Python 3.10+):

**Simple `match case` Example:**
```python
grade = "A"
match grade:
      case "A":
         print("Excellent")
      case "B":
         print("Good")
      case "C":
         print("Average")
      case _:
         print("Other")
```

**Using Patterns in `match case`:**
```python
value = (1, 2)
match value:
      case (1, 2):
         print("Tuple is (1, 2)")
      case (3, 4):
         print("Tuple is (3, 4)")
```

**`match` with Lists:**
```python
numbers = [1, 2, 3]
match numbers:
      case [1, 2]:
         print("List is [1, 2]")
      case [3, 4]:
         print("List is [3, 4]")
```

**`match` with Custom Classes:**
```python
class Animal:
      pass

class Dog(Animal):
      pass

animal = Dog()
match animal:
      case Animal():
         print("It's an animal")
      case Dog():
         print("It's a dog")
```

**`match` with Type Annotations:**
```python
value: int = 42
match value:
      case int:
         print("It's an integer")
```

**`match` with Named Constants:**
```python
STATUS_OK = 200
status_code = 404
match status_code:
   case STATUS_OK:
      print("Request is successful")
   case 404:
      print("Page not found")
```

These examples showcase different scenarios where `if`, `elif`, `else`, and `match case` control statements are used to make decisions and handle various cases based on conditions or patterns. The `match case` examples are applicable in Python 3.10 and later versions.
[Go Back to Table of Contents](#table-of-contents)

##### Python Loops (for and while loop)
Here are examples of `for` and `while` loops in Python to help you understand their basics and usage:

###### `for` Loop Examples:

**Iterating Over a List:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
      print(fruit)
```

**Iterating Over a Range of Numbers:**
```python
for i in range(5):
      print(i)
```

**Iterating Over a Dictionary:**
```python
person = {"name": "Alice", "age": 30}
for key, value in person.items():
      print(f"{key}: {value}")
```

**Nested Loops - Multiplication Table:**
```python
for i in range(1, 6):
      for j in range(1, 11):
         print(f"{i} x {j} = {i * j}")
```

Note: In Python, you can use a `for` loop with an `else` block to execute code when the loop completes normally (i.e., without encountering a `break` statement). Here are a couple of examples:

###### Example 1: Using `for` Loop with `else`

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "apple":
        print("Found apple! Exiting loop.")
        break
    print(f"Processing {fruit}...")
else:
    print("Loop completed without finding apple.")
```

In this example, the `for` loop iterates through a list of fruits. When it encounters "banana," it prints a message and exits the loop using `break`. If the loop completes without encountering a `break`, the `else` block is executed, indicating that the banana was not found.

###### Example 2: Using `for` Loop to Check for Prime Numbers

```python
for num in range(2, 11):
    for divisor in range(2, num):
        if num % divisor == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
```

In this example, the `for` loop iterates through numbers from 2 to 10. It has an inner `for` loop that checks for divisors of each number. If a divisor is found (i.e., `num % divisor == 0`), the number is not prime, and the loop exits using `break`. If no divisors are found, the `else` block is executed, indicating that the number is prime.

These examples demonstrate how to use a `for` loop with an `else` block to handle different scenarios when looping through data.

###### `while` Loop Examples:

**Simple `while` Loop:**
```python
count = 0
while count < 5:
      print(count)
      count += 1
```

**Using `break` to Exit a Loop:**
```python
count = 0
while True:
      print(count)
      count += 1
      if count >= 5:
         break
```

**Using `continue` to Skip Iteration:**
```python
count = 0
while count < 5:
      count += 1
      if count == 3:
         continue
      print(count)
```

**Infinite Loop with `while` and User Input:**
```python
while True:
      user_input = input("Enter 'q' to quit: ")
      if user_input == 'q':
         break
```

**`while` Loop with Conditional Exit:**
```python
num = 1
while num <= 10:
      print(num)
      num += 1
else:
      print("Loop completed.")
```

These examples cover a wide range of scenarios where `for` and `while` loops are used in Python. You can use `for` loops when you have a finite number of iterations or when you want to iterate over sequences like lists and dictionaries. `while` loops are useful when you need to loop until a certain condition is met or when you want to create infinite loops with appropriate exit conditions.
[Go Back to Table of Contents](#table-of-contents)

Exception handling in Python is done using `try`, `except`, `else`, and `finally` blocks. Here are six examples of Python exception handling:

**Handling a Specific Exception:**

```python
try:
    num = int("abc")
except ValueError:
    print("ValueError: Invalid conversion")
```

In this example, we attempt to convert the string "abc" to an integer, which raises a `ValueError`. We catch the `ValueError` and print a custom error message.

**Handling Multiple Exceptions:**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero")
except Exception as e:
    print(f"Exception: {e}")
```

Here, we handle both a `ZeroDivisionError` and any other exceptions that might occur using a generic `Exception` catch block.

**Using `else` with `try`:**

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("ValueError: Invalid input")
else:
    print(f"You entered: {num}")
```

The `else` block is executed if no exceptions occur in the `try` block. In this case, it prints the entered number.

**Using `finally`:**

```python
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: File not found")
finally:
    print("This will always be executed")
```

The `finally` block is executed regardless of whether an exception is raised or not. It's often used for cleanup actions.

**Raising Custom Exceptions:**

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

We define a custom exception using `raise` and then raise it when a division by zero is attempted.

**Using `except` without an Exception Type:**

```python
try:
    value = int("123")
except:
    print("An exception occurred")
```

This catches any exception without specifying a specific exception type. However, it's generally better to catch specific exceptions to handle them appropriately.

These examples demonstrate how to handle exceptions in Python using `try`, `except`, `else`, and `finally` blocks to gracefully handle errors and exceptions in your code.

[Go Back to Table of Contents](#table-of-contents)

##### Python Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that focuses on organizing code using objects, which represent real-world entities. Here is a basic example and a tabular column illustrating the key principles of OOP: Abstraction, Polymorphism, Inheritance, and Encapsulation (APIE).

### Basic OOP Example:

Let's consider a simple example of a `Person` class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling methods on instances
person1.introduce()
person2.introduce()
```

Now, let's break down this example using the APIE principles:

| Principle      | Description                                                                                                                                                     | Example                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Abstraction    | Abstraction hides complex implementation details and exposes a simplified interface.                                                                           | The `Person` class abstracts away the internal details of a person's name and age.               |
| Polymorphism   | Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables method overriding and dynamic method dispatch. | The `introduce` method is common across `Person` objects, allowing us to call it on any instance. |
| Inheritance    | Inheritance allows a new class (subclass or derived class) to inherit properties and behaviors from an existing class (base class or superclass).          | If we create a `Student` class inheriting from `Person`, it inherits the name and age properties. |
| Encapsulation  | Encapsulation restricts access to an object's internal state and behaviors. It hides the details of an object's implementation.                                | The `name` and `age` attributes of a `Person` object are encapsulated within the class.          |

This table summarizes the OOP principles and their presence in the example.

| Principle     | Example                                       |
| ------------- | --------------------------------------------- |
| Abstraction   | `Person` class abstracts name and age details |
| Polymorphism  | `introduce` method is common                  |
| Inheritance   | `Student` can inherit from `Person`           |
| Encapsulation | `name` and `age` attributes are encapsulated  |

These principles form the foundation of OOP and help in creating modular, maintainable, and reusable code.

[Go Back to Table of Contents](#table-of-contents)

##### Python OOP example with Car

Let's continue with the example of a `Car` class to illustrate more aspects of Object-Oriented Programming (OOP). We'll cover inheritance, encapsulation, and polymorphism with this example.

**Example: Car Class**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Initial speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.make} {self.model} is accelerating. Current speed: {self.speed} mph")

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            print(f"{self.make} {self.model} is braking. Current speed: {self.speed} mph")
        else:
            print(f"{self.make} {self.model} is already stopped.")

    def honk(self):
        print(f"{self.make} {self.model} is honking!")

# Inheriting from Car to create a specific car type
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    # Overriding the accelerate method for electric cars
    def accelerate(self):
        if self.speed < 100:
            self.speed += 20
            print(f"{self.make} {self.model} (Electric) is accelerating. Current speed: {self.speed} mph")

    # Additional method for electric cars
    def charge_battery(self):
        print(f"{self.make} {self.model} (Electric) is charging. Battery capacity: {self.battery_capacity} kWh")

# Create instances of Car and ElectricCar
car1 = Car("Toyota", "Camry", 2022)
electric_car1 = ElectricCar("Tesla", "Model 3", 2022, 75)

# Using the methods
car1.accelerate()
car1.brake()
car1.honk()

electric_car1.accelerate()
electric_car1.brake()
electric_car1.charge_battery()
```

In this extended example, we have a `Car` class with basic attributes and methods to accelerate, brake, and honk. Then, we create a subclass `ElectricCar` that inherits from `Car` and adds specific behaviors for electric cars. Here's how it demonstrates the OOP principles:

- **Inheritance**: `ElectricCar` inherits attributes and methods from `Car` and can extend or override them.
- **Encapsulation**: Attributes like `make`, `model`, `year`, and `speed` are encapsulated within the classes.
- **Polymorphism**: Both `Car` and `ElectricCar` have an `accelerate` method, but they behave differently when called.

This example shows how OOP allows you to create classes that represent real-world objects, reuse code through inheritance, encapsulate data and behaviors, and provide polymorphic behavior for different types of objects.

[Go Back to Table of Contents](#table-of-contents)

##### More OOP Operations

Here are some additional operations and scenarios using the `Car` and `ElectricCar` classes:

**More Operations with Car and ElectricCar:**

```python
# Create more instances
car2 = Car("Ford", "Mustang", 2022)
electric_car2 = ElectricCar("Nissan", "Leaf", 2022, 40)

# Accelerate both cars
car2.accelerate()
electric_car2.accelerate()

# Perform braking
car2.brake()
electric_car2.brake()

# Honk the horn
car2.honk()
electric_car2.honk()

# Check battery capacity (ElectricCar-specific method)
print(f"Battery capacity of {electric_car2.make} {electric_car2.model}: {electric_car2.battery_capacity} kWh")

# Charge the electric car's battery
electric_car2.charge_battery()

# Using the parent class method on the child class object
electric_car2.accelerate()  # This calls the overridden method in ElectricCar
car2.accelerate()           # This calls the method in Car
```

In this extended example, we perform various operations on instances of both `Car` and `ElectricCar`:

- We create more instances to represent different car models.
- We accelerate, brake, and honk for both types of cars.
- We use the `charge_battery` method specific to `ElectricCar` to check the battery capacity and charge the battery.
- We demonstrate that the overridden `accelerate` method in `ElectricCar` is called when used with an `ElectricCar` instance, while the parent class method is called when used with a `Car` instance.

These operations showcase how you can work with objects of different classes, including subclasses, to perform actions specific to their types while maintaining code reusability and readability.

[Go Back to Table of Contents](#table-of-contents)

##### Python Test-First Development 

Test-First Development, also known as Test-Driven Development (TDD), is a software development practice where you write tests for a piece of code before writing the code itself. It helps ensure that your code meets the desired requirements and remains robust as you make changes. Here's how to do Test-First Development in Python with a few examples using the `unittest` framework:

**Example 1: Testing a Simple Function**

Let's say you want to create a function that adds two numbers. You would write the test for it first.

1. Write the Test:
```python
import unittest

class TestAddition(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
```

2. Write the Code:
```python
def add_numbers(a, b):
    return a + b
```

3. Run the Test: Running the test will fail initially because the function `add_numbers` doesn't exist yet. This prompts you to implement the function.

4. Implement the Code: Implement the `add_numbers` function to pass the test.

**Example 2: Testing a Class**

Let's say you want to create a simple `Person` class with a method to calculate the age based on birth year.

1. Write the Test:
```python
import unittest

class TestPerson(unittest.TestCase):
    def test_calculate_age(self):
        person = Person("Alice", 1990)
        age = person.calculate_age(2022)
        self.assertEqual(age, 32)

if __name__ == '__main__':
    unittest.main()
```

2. Write the Code:
```python
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def calculate_age(self, current_year):
        return current_year - self.birth_year
```

3. Run the Test: Initially, the test will fail because the `Person` class and its method are not implemented.

4. Implement the Code: Implement the `Person` class and the `calculate_age` method to pass the test.

**Example 3: Testing Edge Cases**

Testing edge cases is an important part of TDD. For example, let's test a function that returns the largest element in a list.

1. Write the Test:
```python
import unittest

class TestLargestElement(unittest.TestCase):
    def test_find_largest(self):
        lst = [5, 2, 8, 10, 1]
        result = find_largest(lst)
        self.assertEqual(result, 10)

    def test_empty_list(self):
        lst = []
        result = find_largest(lst)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
```

2. Write the Code:
```python
def find_largest(lst):
    if not lst:
        return None
    return max(lst)
```

3. Run the Test: Initially, the tests will fail because the `find_largest` function is not implemented.

4. Implement the Code: Implement the `find_largest` function to pass both tests, including the edge case of an empty list.

By following these steps, you can practice Test-First Development in Python, ensuring that your code is tested thoroughly and that it meets the specified requirements.

[Go Back to Table of Contents](#table-of-contents)

##### Python Collections Classes

Here are examples for all the nine collections classes:

**Counters**

```python
from collections import Counter

# Example: Counting elements in a list
fruits = ["apple", "banana", "apple", "cherry", "banana"]
fruit_counts = Counter(fruits)
print(fruit_counts)  # Output: Counter({'apple': 2, 'banana': 2, 'cherry': 1})
```

**DefaultDict**

```python
from collections import defaultdict

# Example: Creating a defaultdict
word_count = defaultdict(int)

# Counting word occurrences
text = "apple banana apple cherry banana"
for word in text.split():
    word_count[word] += 1

print(word_count["apple"])  # Output: 2
```

**OrderedDict**

```python
from collections import OrderedDict

# Example: Creating an OrderedDict
ordered_dict = OrderedDict()
ordered_dict["one"] = 1
ordered_dict["two"] = 2
ordered_dict["three"] = 3

# Iterating in the order of insertion
for key, value in ordered_dict.items():
    print(key, value)

# Output:
# one 1
# two 2
# three 3
```

**ChainMap**

```python
from collections import ChainMap

# Example: Creating a ChainMap
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
chain_map = ChainMap(dict1, dict2)

# Accessing values
print(chain_map["a"])  # Output: 1
print(chain_map["b"])  # Output: 2 (from dict1)
print(chain_map["c"])  # Output: 4 (from dict2)
```

**NamedTuple**

```python
from collections import namedtuple

# Example: Creating a namedtuple
Person = namedtuple("Person", ["name", "age"])
person = Person(name="Alice", age=30)

# Accessing fields
print(person.name)  # Output: "Alice"
print(person.age)   # Output: 30
```

**DeQue**

```python
from collections import deque

# Example: Creating a deque
queue = deque(["apple", "banana", "cherry"])

# Appending and popping elements
queue.append("date")
queue.popleft()
print(queue)  # Output: deque(['banana', 'cherry', 'date'])
```

**UserList**

```python
from collections import UserList

# Example: Creating a custom list
class MyList(UserList):
    def even_numbers(self):
        return [x for x in self.data if x % 2 == 0]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list.even_numbers())  # Output: [2, 4]
```

**UserString**

```python
from collections import UserString

# Example: Creating a custom string
class MyString(UserString):
    def reverse(self):
        return self.data[::-1]

my_str = MyString("hello")
print(my_str.reverse())  # Output: "olleh"
```

**UserDict**

```python
from collections import UserDict

# Example: Creating a custom dictionary
class MyDict(UserDict):
    def double_values(self):
        return {key: value * 2 for key, value in self.data.items()}

my_dict = MyDict({"a": 2, "b": 3})
print(my_dict.double_values())  # Output: {'a': 4, 'b': 6}
```

These examples cover various features and use cases of the collections classes you requested, including Counters, DefaultDict, OrderedDict, ChainMap, NamedTuple, DeQue, UserList, UserString, and UserDict.

[Go Back to Table of Contents](#table-of-contents)

##### Python Another quick reference of Sequential data-types (List, Tuple, Set, Dictionary)

Here's a tabular comparison of Python data types: List, Tuple, Set, and Dictionary, highlighting their differences and providing code examples for declarations.

| Feature                  | List                            | Tuple                           | Set                             | Dictionary                      |
|--------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| Declaration              | `my_list = [1, 2, 3]`           | `my_tuple = (1, 2, 3)`          | `my_set = {1, 2, 3}`            | `my_dict = {'a': 1, 'b': 2}`   |
| Mutable                  | Yes                             | No                              | Yes (but individual items not) | Yes                             |
| Ordered                  | Yes                             | Yes                             | No                              | No                              |
| Duplicate Elements       | Allowed                         | Allowed                         | Not Allowed                     | Not Allowed                     |
| Access by Index          | Yes                             | Yes                             | No                              | Yes (by key)                   |
| Iteration                | Yes                             | Yes                             | Yes                             | Yes                             |
| Examples                 | `my_list = [1, 2, 3]`           | `my_tuple = (1, 2, 3)`          | `my_set = {1, 2, 3}`            | `my_dict = {'a': 1, 'b': 2}`   |
|                         | `my_list.append(4)`             | `element = my_tuple[0]`         | `my_set.add(4)`                 | `my_dict['c'] = 3`             |
|                         | `my_list.remove(2)`             | `len(my_tuple)`                 | `len(my_set)`                   | `del my_dict['b']`             |

These are the key differences between List, Tuple, Set, and Dictionary in Python. Each data type has its own strengths and use cases, so choosing the right one depends on the specific requirements of your program.

[Go Back to Table of Contents](#table-of-contents)

##### Python references 

Here's the tabular comparison of popular Python learning resources with their descriptions and URLs:

| Resource                 | Description                                                        | URL                                      |
|--------------------------|--------------------------------------------------------------------|------------------------------------------|
| Python.org               | The official Python website with documentation, tutorials, and more. | [Python.org](https://www.python.org/)    |
| edX                      | Provides Python courses, including ones by Microsoft.              | [edX](https://www.edx.org/)             |
| Python.org Beginner's Guide | Dedicated beginner's guide with resources and tutorials.          | [Python.org Beginner's Guide](https://docs.python.org/3/tutorial/index.html) |
| Stack Overflow           | A platform for asking and answering Python-related questions.      | [Stack Overflow](https://stackoverflow.com/) |
| YouTube Python Tutorials | Video tutorials on Python topics from various creators.           | N/A (Search for Python tutorials on YouTube) |

You can click on the URLs to access these Python learning resources.

[Go Back to Table of Contents](#table-of-contents)

