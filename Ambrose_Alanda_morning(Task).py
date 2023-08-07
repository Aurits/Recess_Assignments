# Assignment A7:
# 1a) Show a context manager for file handling that automatically opens and closes a file.
# b) Shows a context manager for managing a database connection.
# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.

# Context manager for file handling
print("Context manager for file handling")

"""
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage of the context manager
with FileManager('test.txt') as file:
    data = file.read()
    print(data)
"""







print("\nOR\n")







"""
from contextlib import contextmanager
# Context manager for file handling
@contextmanager
def file_manager(filename):
    try:
        file = open(filename, 'r')
        yield file
    finally:
        file.close()

# Usage of the context manager
with file_manager('test.txt') as file:
    data = file.read()
    print(data)

"""






import sqlite3
# Context manager for managing a database connection
print("\nContext manager for managing a database connection")
"""
class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

# Usage of the context manager
with DatabaseManager('Users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    print(data)
"""








print("Multithreading and multiprocessing!!!!!")
"""
import time
import threading
import multiprocessing

# Function for multithreading
def print_hello():
    time.sleep(2)  # Simulate a delay
    print("Hello")

# Function for multiprocessing
def print_hi():
    time.sleep(2)  # Simulate a delay
    print("Hi")

if __name__ == '__main__':
    # Multithreading
    threads = []

    for _ in range(3):
        thread = threading.Thread(target=print_hello)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Multithreading finished")

    # Multiprocessing
    processes = []

    for _ in range(3):
        process = multiprocessing.Process(target=print_hi)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing finished")

"""




print("\nOR\n")




import time
import threading
# Function for multithreading - Thread 1
def print_hello():
    time.sleep(2)  # Simulate a delay
    print("Hello")

# Function for multithreading - Thread 2
def print_hi():
    time.sleep(2)  # Simulate a delay
    print("Hi")

if __name__ == '__main__':
    # Create Thread 1
    thread1 = threading.Thread(target=print_hello)
    thread1.start()

    # Create Thread 2
    thread2 = threading.Thread(target=print_hi)
    thread2.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()

    print("BYE !!!!")
    # print('\U0001F602')

print("     ,--.     ")
print("    ([ oo ]    ")
print("     `'/.,\    ")
print("     |__|_|    ")
print("     |__|_|    ")
print("     |__|_|    ")
print("     |__|_|    ")
print("    _| _|_|_   ")
print("  _| _| _| _|_ ")
print(" |  _| _| _|  |")
print("<| _| _| _| _ |")
print(" |___________|")
print("Multithreading finished")
