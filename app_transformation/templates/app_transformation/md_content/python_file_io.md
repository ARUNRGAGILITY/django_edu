<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Python File I/O Basics</b>
<br>

### Step 1: Basic File Reading

**Objective:** Learn to open and read the contents of a file.

**Task:** Create a text file named `example.txt` and write a few lines of text in it. Then write a Python script to read and print the contents of the file.

```python
# Step 1: Basic File Reading

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

# Test the function
print(read_file('example.txt'))
```

### Step 2: Line by Line Reading

**Objective:** Understand how to read a file line by line.

**Task:** Modify the script to read the file line by line and print each line.

```python
# Step 2: Line by Line Reading

def read_file_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Test the function
read_file_line_by_line('example.txt')
```

### Step 3: Writing to a File

**Objective:** Learn to write data to a file.

**Task:** Create a function to write a given string to a file.

```python
# Step 3: Writing to a File

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Test the function
write_to_file('example.txt', 'This is a new line.\n')
```

### Step 4: Appending to a File

**Objective:** Learn how to append data to an existing file.

**Task:** Modify the script to append a new line to the file instead of overwriting it.

```python
# Step 4: Appending to a File

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

# Test the function
append_to_file('example.txt', 'Adding another line.\n')
```

### Step 5: Reading and Writing Binary Files

**Objective:** Understand how to handle binary files.

**Task:** Write a function to read and another to write binary data to a file.

```python
# Step 5: Reading and Writing Binary Files

def write_binary_file(filename, content):
    with open(filename, 'wb') as file:
        file.write(content)

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        content = file.read()
    return content

# Test the functions
write_binary_file('example.bin', b'\x00\x01\x02\x03')
print(read_binary_file('example.bin'))
```

### Step 6: Working with JSON Data

**Objective:** Learn to work with JSON data in files.

**Task:** Create a function to save a Python dictionary as a JSON file and another function to read JSON data into a dictionary.

```python
import json

# Step 6: Working with JSON Data

def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Test the functions
sample_data = {"name": "John", "age": 30}
write_json('data.json', sample_data)
print(read_json('data.json'))
```

This gradual approach will help beginners understand various aspects of file handling in Python, starting from simple text file operations to handling binary and JSON data. 
Each step can be followed by practical exercises or small projects to reinforce learning.