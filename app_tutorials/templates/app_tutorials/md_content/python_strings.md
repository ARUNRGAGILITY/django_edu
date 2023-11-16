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

# Python String Exercises 

## Exercise for Python String operations and learning

1. Write a Python program to find the length of a string.
2. Write a Python program to count the number of characters in a string.
3. Write a Python program to count the number of words in a string.
4. Write a Python program to reverse a string.
5. Write a Python program to check if a string is a palindrome.
6. Write a Python program to capitalize the first letter of each word in a string.
7. Write a Python program to convert a string to lowercase.
8. Write a Python program to remove whitespace from both ends of a string.
9. Write a Python program to find the index of a substring in a string.
10. Write a Python program to replace all occurrences of a substring with another substring in a string.
11. Write a Python program to split a string into a list of words.
12. Write a Python program to join a list of words into a single string with a specified delimiter.
13. Write a Python program to remove all digits from a string.
14. Write a Python program to count the occurrences of a specific character in a string.
15. Write a Python program to remove all punctuation from a string.
16. Write a Python program to check if a string contains only digits.
17. Write a Python program to check if a string contains only alphabetic characters.
18. Write a Python program to find the longest word in a string.
19. Write a Python program to reverse the order of words in a string.
20. Write a Python program to check if two strings are anagrams of each other.

## Solutions
Here are the solutions to the 20 Python string exercises:

1. **Length of a String:**
   ```python
   string = "Hello, World!"
   length = len(string)
   print("Length of the string:", length)
   ```

2. **Count Characters in a String:**
   ```python
   string = "Hello, World!"
   count = len([char for char in string if char.isalnum()])
   print("Number of characters in the string:", count)
   ```

3. **Count Words in a String:**
   ```python
   string = "This is a sample sentence."
   words = len(string.split())
   print("Number of words in the string:", words)
   ```

4. **Reverse a String:**
   ```python
   string = "Hello, World!"
   reversed_string = string[::-1]
   print("Reversed string:", reversed_string)
   ```

5. **Check for Palindrome:**
   ```python
   string = "racecar"
   is_palindrome = string == string[::-1]
   print("Is it a palindrome?", is_palindrome)
   ```

6. **Capitalize First Letter of Each Word:**
   ```python
   string = "hello world"
   capitalized_string = string.title()
   print("Capitalized string:", capitalized_string)
   ```

7. **Convert to Lowercase:**
   ```python
   string = "Hello, World!"
   lowercase_string = string.lower()
   print("Lowercase string:", lowercase_string)
   ```

8. **Remove Whitespace from Ends:**
   ```python
   string = "   Trim me!   "
   trimmed_string = string.strip()
   print("Trimmed string:", trimmed_string)
   ```

9. **Find Substring Index:**
   ```python
   string = "Hello, World!"
   substring = "World"
   index = string.find(substring)
   print("Index of '{}' in the string: {}".format(substring, index))
   ```

10. **Replace Substring:**
    ```python
    string = "Hello, World!"
    new_string = string.replace("World", "Python")
    print("Modified string:", new_string)
    ```

11. **Split String into Words:**
    ```python
    string = "This is a sample sentence."
    words = string.split()
    print("Words in the string:", words)
    ```

12. **Join Words into String:**
    ```python
    words = ["This", "is", "a", "sample", "sentence."]
    string = " ".join(words)
    print("Joined string:", string)
    ```

13. **Remove Digits from String:**
    ```python
    string = "Hello123"
    without_digits = ''.join([char for char in string if not char.isdigit()])
    print("String without digits:", without_digits)
    ```

14. **Count Specific Character:**
    ```python
    string = "Hello, World!"
    char_to_count = ","
    count = string.count(char_to_count)
    print("Occurrences of '{}': {}".format(char_to_count, count))
    ```

15. **Remove Punctuation from String:**
    ```python
    import string

    string_with_punctuation = "Hello, World!"
    translator = str.maketrans('', '', string.punctuation)
    no_punctuation_string = string_with_punctuation.translate(translator)
    print("String without punctuation:", no_punctuation_string)
    ```

16. **Check for Digits Only:**
    ```python
    string = "12345"
    is_digits_only = string.isdigit()
    print("Contains only digits?", is_digits_only)
    ```

17. **Check for Alphabetic Characters Only:**
    ```python
    string = "Hello"
    is_alpha_only = string.isalpha()
    print("Contains only alphabetic characters?", is_alpha_only)
    ```

18. **Find Longest Word:**
    ```python
    string = "This is a sample sentence."
    words = string.split()
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
    ```

19. **Reverse Order of Words:**
    ```python
    string = "This is a sample sentence."
    words = string.split()
    reversed_string = " ".join(reversed(words))
    print("Reversed order of words:", reversed_string)
    ```

20. **Check for Anagrams:**
    ```python
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    string1 = "listen"
    string2 = "silent"
    result = is_anagram(string1, string2)
    print("Are '{}' and '{}' anagrams?".format(string1, string2), result)
    ```