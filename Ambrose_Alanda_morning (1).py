import re


print("This is AN EXAMPLE TO TEST PASSWORDS")
# Regular Expressions
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = "Contact us at info@example.com or support@example.com"
matches = re.findall(pattern, text)
print("Email addresses found:", matches)

# Password Verifier Function
def verify_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[@#$%^&+=]', password):
        return False
    return True

# Testing the Password Verifier
password = "SecureP@ssw0rd"
if verify_password(password):
    print("Password is strong.")
else:
    print("Password is weak.")

"""

# Generators
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for i in range(10):
    print(next(fib), end=" ")

print()

# Iterators
class Squares:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

squares = Squares(5)
for num in squares:
    print(num, end=" ")



"""


"""
def factorial(n):
    if n==0:
        return 1:
    else:
        return n*factorial(n-1)
#to print
for i in range(1,10):
    print(factorial(i))

"""


"""
def factorial(n):
    if n == 0:
        yield 1
    else:
        fact = 1
        for 1 in range(1,n+1):
            fact *=i
            yield fact

for i in range (1,10):
    print(*factorial(i))


"""


"""
def squares():
    for i in range(1,10):
        yield i**2


#create an iterator obj to produce the squares

squares_iterator = squares()

for i in range(5):
    print(next(squares_iterator))


"""


"""
def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
    return inner

@my_decorator
def outer_decorator():
    print("This is outer decorator")


outer_decorator()

"""