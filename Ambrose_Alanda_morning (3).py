"""# Python Operators

Comparison Operators
== equal to
!= not equal to
> greater than
>= greater than or equal to
<= less than or equal to

Logical Operators
Logical AND 'and' 
Logical OR 'or'
Logical NOT 'not'

Assignment Operators
Assign value: '='
Add value: '+'
Add and assign: '+='
Subtract and assign: '-='
Divide and assign: '/='
Modulus and assign: '%='
Exponentiate and assign: '**='

Membership Operators
In: 'in' - checks if a value exists in a sequence
Not in: 'not in' - checks if a value does not exist in a sequence


Identity Operators
Is: 'is' operator: checks if two values are not the same

"""


# # Addition
# num1 = 5
# num2 = 3
# result = num1 + num2
# print("Addition:", result)  # Output: Addition: 8

# # Subtraction
# num3 = 7
# num4 = 2
# result = num3 - num4
# print("Subtraction:", result)  # Output: Subtraction: 5

# # Multiplication
# num5 = 4
# num6 = 6
# result = num5 * num6
# print("Multiplication:", result)  # Output: Multiplication: 24

# # Division
# num7 = 10
# num8 = 2
# result = num7 / num8
# print("Division:", result)  # Output: Division: 5.0

# # Modulus (Remainder)
# num9 = 10
# num10 = 3
# result = num9 % num10
# print("Modulus:", result)  # Output: Modulus: 1

# # Exponentiation
# num11 = 2
# num12 = 3
# result = num11 ** num12
# print("Exponentiation:", result)  # Output: Exponentiation: 8




# print(2**5)
# print(3+5)
# print(10%3)
# print(10/3)
# print(10//3)
# print(10*3)
# print(10-3)
# print(10+3)
# a = 5
# print(a)

# #Comparison Operators

# # Comparison Operators
# num1 = 5
# num2 = 3

# # Equal to
# if num1 == num2:
#     print("Numbers are equal")
# else:
#     print("Numbers are not equal")  # Output: Numbers are not equal

# # Not equal to
# if num1 != num2:
#     print("Numbers are not equal")
# else:
#     print("Numbers are equal")  # Output: Numbers are not equal

# # Greater than
# if num1 > num2:
#     print("num1 is greater than num2")  # Output: num1 is greater than num2
# else:
#     print("num1 is not greater than num2")

# # Less than
# if num1 < num2:
#     print("num1 is less than num2")
# else:
#     print("num1 is not less than num2")  # Output: num1 is not less than num2

# # Greater than or equal to
# if num1 >= num2:
#     print("num1 is greater than or equal to num2")  # Output: num1 is greater than or equal to num2
# else:
#     print("num1 is neither greater than nor equal to num2")

# # Less than or equal to
# if num1 <= num2:
#     print("num1 is less than or equal to num2")
# else:
#     print("num1 is neither less than nor equal to num2")  # Output: num1 is neither less than nor equal to num2


# a = 23.5
# b = 15
# c = 9

# #Greater than
# if (b > a):
#     print("a is greater than b")
# else:
#     print("a is less than b")
#     print(b > a)

# #Less than
# if (c < a):
#     print("c is less than a")

# #Greater than or equal to
# if (a >= b):
#     print("a is greater than or equal to b")

# #Less than or equal to
# if (c <= a):
#     print("c is less than or equal to a")

# #Equal to
# if (a == b):
#     print("a is equal to b")

# #Not equal to
# if (a != b):
#     print("a is not equal to b")

# #Examples with Logical Operators
# a = True
# b = False

# #Logical AND
# print(a and b)

# #Logical OR
# print(a or b)

# #Logical NOT
# print(not a)


# # Assigning Boolean Variables
# is_sunny = True
# is_raining = False
# is_windy = True

# # Logical Operations with Boolean Variables
# if is_sunny and not is_raining:
#     print("It's a sunny day!")  # Output: It's a sunny day!

# if is_raining or is_windy:
#     print("Weather conditions are not ideal.")  # Output: Weather conditions are not ideal.

# if not (is_sunny or is_windy):
#     print("It's neither sunny nor windy.")  # This print statement will not be executed.





# #print(a += b)

# #Identity operators
# x = 10 
# y = 10

# print(x != y)

# """
# Bitwise AND ('&'): performs bitwise AND operation between the correspoding bits of two operands
# Bitwise OR ('|'): performs bitwise OR operation between the correspoding bits of two operands
# Bitwise XOR ('^'): performs bitwise XOR operation between the correspoding bits of two operands
# Bitwise NOT ('~'): performs bitwise NOT operation on a single operand
# Bitwise left shift ('<<'): performs bitwise left shift operation on a single operand
# Bitwise right shift ('>>'): performs bitwise right shift operation on a single operand
# """

# #Examples on Bitwise Operators
# a = 10 #in binary notation 10 is 1010
# b = 20 #in binary notation 20 is 10100

# #Bitwise AND
# print(a & b)

# #Bitwise OR
# print(a | b)

# #Bitwise XOR
# print(a ^ b)

# #Bitwise NOT
# print(~a)

# #Bitwise left shift
# print(a << 2)

# #Bitwise right shift
# print(a >> 2)

#Simple Calculator application

#Assignment: create a simple calculator program with a GUI interface.
#Make your title of the calculator program with window with your name eg 'AliBryan' simple calculator

print("create a simple calculator program with a GUI interface.")
import tkinter as tk
from tkinter import ttk

# Function to append a digit to the input field
def add_digit(digit):
    entry_input.insert(tk.END, digit)

# Function to perform calculations
def calculate():
    try:
        expression = entry_input.get()
        result = eval(expression)

        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, str(result))

    except (ValueError, ZeroDivisionError):
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error: Invalid input")

# Function to clear the input and result fields
def clear():
    entry_input.delete(0, tk.END)
    entry_result.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("AMBROSE ALANDA SIMPLE CALCULATOR")
window.configure(bg='#ECECEC')

# Styling
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

# Input Field
entry_input = ttk.Entry(window)
entry_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Result Field
entry_result = ttk.Entry(window)
entry_result.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Number Buttons
numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
row_num = 2
col_num = 0
for number in numbers:
    btn_number = ttk.Button(window, text=number, command=lambda num=number: add_digit(num))
    btn_number.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

# Operator Buttons
operators = ['+', '-', '*', '/']
row_op = 2
col_op = 3
for operator in operators:
    btn_operator = ttk.Button(window, text=operator, command=lambda op=operator: add_digit(op))
    btn_operator.grid(row=row_op, column=col_op, padx=5, pady=5)
    row_op += 1

# Calculate Button
btn_calculate = ttk.Button(window, text="=", command=calculate)
btn_calculate.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Clear Button
btn_clear = ttk.Button(window, text="C", command=clear)
btn_clear.grid(row=6, column=2, columnspan=2, padx=5, pady=5)

# Start the main loop
window.mainloop()








