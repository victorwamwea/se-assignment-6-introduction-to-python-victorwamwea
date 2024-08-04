Python Basics:
Answer:

Python is a high-level, interpreted programming language known for its readability, simplicity, and versatility. Some of its key features include:

Readability: Python's syntax is clear and intuitive, making it easy to read and write.
Dynamically Typed: Variables in Python do not require an explicit declaration to reserve memory space.
Interpreted: Python code is executed line-by-line, which makes debugging easier.
Extensive Standard Library: Python's standard library offers a wide range of modules and functions.
Community Support: Python has a large and active community that contributes to its continuous improvement and provides a wealth of resources.
Use Cases:

Web Development: Frameworks like Django and Flask.
Data Science: Libraries like Pandas, NumPy, and Scikit-Learn.
Automation: Scripting for automating tasks.

Installing Python:
Windows:
Download the Python installer from python.org.
Run the installer and check the "Add Python to PATH" option.
Complete the installation.

macOS:
Install Homebrew (if not already installed): /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install Python: brew install python

Linux:
Update package list: sudo apt update
Install Python: sudo apt install python3

Verification:
Open a terminal or command prompt.
Type python --version or python3 --version to verify the installation.
Set Up a Virtual Environment:
python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate

Python Syntax and Semantics:
Answer:
print("Hello, World!")
print(): This is a built-in function that outputs text to the console.
"Hello, World!": This is a string, a sequence of characters enclosed in quotes.

Data Types and Variables:
Answer:
Basic Data Types:
int: Integer numbers
float: Floating-point numbers
str: Strings
bool: Boolean values (True or False)
list: Ordered collection of items
dict: Collection of key-value pairs

Script:
# Integer
age = 30
# Float
height = 5.9
# String
name = "John"
# Boolean
is_student = False
# List
fruits = ["apple", "banana", "cherry"]
# Dictionary
person = {"name": "Alice", "age": 25}

print(age, height, name, is_student, fruits, person)

Control Structures:
Answer:
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
For Loop:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

Functions in Python:
Answer:
Functions are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable, and reducing redundancy.
def add(a, b):
    return a + b
# Calling the function
result = add(5, 3)
print(result)  # Output: 8

Lists and Dictionaries:
Answer:
List: Ordered collection of items, accessed by index.
Dictionary: Unordered collection of key-value pairs, accessed by key.
# List
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adding an item
print(numbers[2])  # Accessing an item by index
# Dictionary
student = {"name": "Alice", "age": 25}
student["grade"] = "A"  # Adding a key-value pair
print(student["name"])  # Accessing a value by key

Exception Handling:
Answer:
Exception handling is used to manage errors that occur during program execution, allowing the program to continue running or to fail gracefully.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This block always executes.")

Modules and Packages:
Answer:
Module: A file containing Python code, such as functions and classes.
Package: A directory containing multiple modules and an __init__.py file.
import math
print(math.sqrt(16))  # Output: 4.0

File I/O:
Answer:
Reading from a File:
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
Writing to a File:
lines = ["First line", "Second line", "Third line"]
with open('output.txt', 'w') as file:
    for line in lines:
        file.write(line + "\n")




