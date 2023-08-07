# #AMBROSE ALANDA week2

# Exception handling

# file handling



# File Handling and Exception Handling in Python


# Read Mode ("r"): Used to open a file for reading its contents. 
# File must exist. (open("example.txt", "r"))

# Write Mode ("w"): Used to open a file for writing data to it. 
# File is created if it doesn't exist. Existing contents are completely overwritten. 
# (open("example.txt", "w"))

# Append Mode ("a"): Used to open a file for appending data to it. 
# File is created if it doesn't exist. New data is added at the end of the file, preserving existing contents. 
# (open("example.txt", "a"))


"""
# File path
file_path = "test.txt"

try:
    # Open file in read mode ("r")
    with open(file_path, "r") as file:
        # Read the contents of the file using read()
        file_contents = file.read()

        # Print file contents
        print("File contents:")
        print(file_contents)

    # Open file in write mode ("w")
    with open(file_path, "w") as file:
        # Write to file using write()
        file.write("Hello, World!")
        print("Write operation successful!")

    # Open file in append mode ("a")
    with open(file_path, "a") as file:
        # Append to file using write()
        file.write("\nThis is an appended line.")
        print("Append operation successful!")

    # Open file in read mode ("r")
    with open(file_path, "r") as file:
        # Read line by line using readline()
        print("File contents (line by line):")
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()

except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("Permission denied to access the file!")

except Exception as e:
    print("An error occurred while handling the file:")
    print(e)

else:
    print("File operations completed successfully.")

finally:
    # Close the file in the finally block
    try:
        file.close()
        print("File closed.")
    except NameError:
        pass

# Example: Writing to the file from keyboard input

try:
    # Open file in write mode ("w")
    with open(file_path, "w") as file:
        # Get input from the user
        user_input = input("Enter text to write to the file: ")

        # Write user input to the file
        file.write(user_input)
        print("Write operation successful!")

except PermissionError:
    print("Permission denied to write to the file!")

except Exception as e:
    print("An error occurred while writing to the file:")
    print(e)

else:
    print("File write operation completed successfully.")

finally:
    # Close the file in the finally block
    try:
        file.close()
        print("File closed.")
    except NameError:
        pass
"""



# File Handling and Exception Handling in Python

# File path
file_path = "subscribers.txt"

try:
    # Open file in read mode
    with open(file_path, "r") as file:
        # Read the current subscribers from the file
        subscribers = file.readlines()

        # Print the current subscribers
        print("Current subscribers:")
        for subscriber in subscribers:
            print(subscriber.strip())

except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("Permission denied to access the file!")

except Exception as e:
    print("An error occurred while handling the file:")
    print(e)

else:
    print("Subscriber list retrieved successfully.")

finally:
    # Close the file in the finally block
    try:
        file.close()
        print("File closed.")
    except NameError:
        pass

# Example: Adding a subscriber

try:
    # Open file in append mode
    with open(file_path, "a") as file:
        # Get input from the user
        new_subscriber = input("Enter the name of the new subscriber: ")

        # Add the new subscriber to the file
        file.write(new_subscriber + "\n")
        print("Subscriber added successfully.")

except PermissionError:
    print("Permission denied to modify the file!")

except Exception as e:
    print("An error occurred while adding a subscriber:")
    print(e)

else:
    print("Subscriber added successfully.")

finally:
    # Close the file in the finally block
    try:
        file.close()
        print("File closed.")
    except NameError:
        pass







"""
# Open file in read mode
with open("subscribers.txt", "r") as file:
    # Read the entire contents of the file using read()
    file_contents = file.read()
    print(file_contents)

    # Read the contents line by line using readlines()
    lines = file.readlines()
    for line in lines:
        print(line.strip())


"""


"""
import os

# Specify the file path
file_path = "test.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist.")

"""