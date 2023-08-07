#day 2 Dictionary 
# Python Dictionaries
print("---- Dictionaries ----")
# Introduction
print("Dictionaries in Python are a collection of key-value pairs.")
print("Each key is used to access its associated value.")

# Example
student = {
    "name": "John Smith",
    "age": 20,
    "grade": "A"
}
print("Dictionary:", student)

# Accessing values in a dictionary using keys
name = student["name"]
print("Name:", name)

# Finding the data type of a dictionary
print("Data Type of student:", type(student))

# Determining the length of a dictionary
length = len(student)
print("Length of the dictionary:", length)

# Modifying values in a dictionary using keys
student["grade"] = "B"
print("Modified Dictionary:", student)

# Adding new key-value pairs to a dictionary
student["city"] = "New York"
print("Updated Dictionary:", student)

# Removing key-value pairs from a dictionary
del student["age"]
print("Dictionary after removing 'age':", student)

# Looping through a dictionary using items()
print("Looping through the dictionary:")
for key, value in student.items():
    print(key + ":", value)

# Nesting dictionaries within dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("Nested Dictionary:", nested_dict)


# Numbers in Python
print("\n---- Numbers ----")
# Introduction
print("In Python, there are different types of numeric data.")
print("Integer, Floating-Point, and Complex numbers.")

# Example
a = 5
b = 2.5
c = 3 + 2j
print("Integer:", a)
print("Floating-Point:", b)
print("Complex:", c)

# Performing arithmetic operations using numeric variables
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Type conversion between different numeric data types using functions
x = int(b)
y = float(a)
z = complex(a, b)
print("Type conversion:", x, y, z)


# Strings in Python
print("\n---- Strings ----")
# Introduction
print("Strings in Python are sequences of characters.")
print("They can be manipulated and accessed using various methods.")

# Example
name = "John Doe"
age = 25
message = f"Hello, my name is {name} and I am {age} years old."
print("String:", message)

# Formatting strings using f-strings to include variables
formatted_message = f"I'll be {age + 5} years old in 5 years."
print("Formatted String:", formatted_message)

# Raw strings for handling backslashes and special characters
raw_string = r"C:\path\to\file.txt"
print("Raw String:", raw_string)

# Concatenating strings using the + operator and the join() method
greeting = "Hello"
name = "Alice"
concatenated_string = greeting + " " + name
print("Concatenated String:", concatenated_string)

# Accessing individual characters in a string using indexing
first_char = name[0]
print("First Character:", first_char)

# Slicing strings to extract substrings using the : operator
substring = message[6:17]
print("Substring:", substring)

# Utilizing the len() function to find the length of a string
length = len(message)
print("Length of the string:", length)

# Iterating over characters in a string using a for loop
print("Iterating over the characters:")
for char in name:
    print(char)

# Booleans in Python
print("\n---- Booleans ----")
# Introduction
print("Booleans represent truth values: True or False.")
print("They are used in conditional statements to control program flow.")

# Example
is_raining = True
has_umbrella = False

if is_raining and not has_umbrella:
    print("Take shelter and stay dry.")
else:
    print("Enjoy the weather!")

# Evaluating conditions using comparison operators
x = 5
y = 10

print("Comparison Results:")
print("x < y:", x < y)
print("x > y:", x > y)
print("x == y:", x == y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)
print("x != y:", x != y)

# Combining conditions using logical operators
a = True
b = False

print("Logical Operator Results:")
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# Assigning boolean values based on comparisons or conditions
is_greater = x > y
print("is_greater:", is_greater)


# Exercises:
print("\n---- Exercises ----")

# Use the values() method to create a list of items from a dictionary.
values_list = list(student.values())
print("Values List:", values_list)

# Check if a specific key exists in a dictionary.
if "age" in student:
    print("The key 'age' exists in the dictionary.")
else:
    print("The key 'age' does not exist in the dictionary.")

# Change and update items in a dictionary.
student["name"] = "Jane Smith"
student["grade"] = "A+"
print("Updated Dictionary:", student)

# Add and remove items from a dictionary.
student["address"] = "123 Main St"
print("Dictionary after adding 'address':", student)

del student["city"]
print("Dictionary after removing 'city':", student)

# Demonstrate looping through a dictionary and nesting dictionaries within dictionaries.
print("Looping through the dictionary:")
for key, value in student.items():
    print(key + ":", value)

print("Nested Dictionary:", nested_dict)

# Determine the length of a string using the len() function.
length = len(message)
print("Length of the string:", length)

# Iterate through each character in a string using a for loop.
print("Iterating through the characters:")
for char in message:
    print(char)

# Slice a string to extract specific portions of it.
substring = message[7:11]
print("Substring:", substring)

# Perform arithmetic operations with numbers and print the results.
result = a + b * c
print("Arithmetic Result:", result)

# Use boolean values and conditions to control program flow.
if x > 0 and y < 20:
    print("Condition is True, \nThe END")
else:
    print("Condition is False")
