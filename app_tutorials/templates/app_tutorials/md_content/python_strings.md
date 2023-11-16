<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Python Strings</b>
<br>

# Python Strings
Python string is a immutable, sequence data type.
```python
# 1. Creating a string
my_string = "Hello, World!"

# 2. Printing a string
print(my_string)

# 3. String length
length = len(my_string)
print(f"Length of the string: {length}")

# 4. Accessing individual characters in a string
first_char = my_string[0]  # Indexing starts from 0
print(f"First character: {first_char}")

# 5. Slicing a string
substring = my_string[0:5]  # Extracts characters from index 0 to 4
print(f"Substring: {substring}")

# 6. Concatenating strings
str1 = "Hello"
str2 = "World"
combined_str = str1 + ", " + str2
print(f"Concatenated string: {combined_str}")

# 7. String repetition
repeated_str = "Python " * 3  # Repeats the string 3 times
print(f"Repeated string: {repeated_str}")

# 8. String methods
# - Upper and lower case conversion
uppercase_str = my_string.upper()
lowercase_str = my_string.lower()
print(f"Uppercase: {uppercase_str}")
print(f"Lowercase: {lowercase_str}")

# - Checking for substrings
contains_hello = "Hello" in my_string
contains_hi = "Hi" in my_string
print(f"Contains 'Hello': {contains_hello}")
print(f"Contains 'Hi': {contains_hi}")

# - Finding the index of a substring
index_world = my_string.index("World")
print(f"Index of 'World': {index_world}")

# - Replacing substrings
new_string = my_string.replace("World", "Python")
print(f"Replaced string: {new_string}")

# - Splitting a string into a list of substrings
split_str = my_string.split(", ")
print(f"Split string: {split_str}")

# 9. String formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)
```

