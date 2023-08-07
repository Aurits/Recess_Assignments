#day 2 (control flow statemen in python)
# If Statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

print("\n--- If Statement ---\n")

#also
# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are underage")
# elif age >= 18 and age <= 65:
#     print("You are an adult")
# else:
#     print("You are a senior citizen")




# For Loop
word = "Python"

for char in word:
    print(char)

print("\n--- For Loop ---\n")


#also
#FOR LOOP EXAMPLE

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
  
# cars = ["Tesla", "Jeep", "Toyota", "Ford", "BMW"]

# for y in cars:
#     print(y)
    
# numbers = [1,5,4,3,7]
# for z in numbers:
#     print((z*3))



# While Loop
count = 10

while count > 0:
    print(count)
    count -= 1

print("\n--- While Loop ---\n")


#also this
#The use of the while
# i = 1
# while i < 6:

#   if i == 3
#     break
#   print(i)
#   i += 1
  
# r = 5
# while r  <  100:
#     print(r)
#     r = r+1




# Break Statement
numbers = [3, 9, 4, 7, 2, 11, 6]

for num in numbers:
    if num % 2 == 0:
        print("The first even number found:", num)
        break

print("\n--- Break Statement ---\n")





# Continue Statement
numbers = [2, 7, 4, 9, 6, 11, 8]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

print("\n--- Continue Statement ---\n")




# Pass Statement
def some_function():
    pass

print("\n--- Pass Statement ---\n")




# Try-Except Statement
num1 = 10
num2 = 0

try:
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("\n--- Try-Except Statement ---\n")

#EXERCISE
print("\n--- Solution for Exercise about mental health rating ---\n")
def calculate_mental_health_rating(ratings):
    total = sum(ratings.values())
    average_rating = total / len(ratings)
    return average_rating

def main():
    mental_health_ratings = {}
    
    # Get user input for mood, anxiety, and stress ratings
    mood = int(input("Please rate your mood (1-10): "))
    anxiety = int(input("Please rate your anxiety level (1-10): "))
    stress = int(input("Please rate your stress level (1-10): "))
    
    # Store the ratings in the dictionary
    mental_health_ratings["Mood"] = mood
    mental_health_ratings["Anxiety"] = anxiety
    mental_health_ratings["Stress"] = stress
    
    # Calculate the mental health rating
    rating = calculate_mental_health_rating(mental_health_ratings)
    
    # Print the overall mental health rating
    print("Your overall mental health rating is: {:.2f}".format(rating))

# Run the program
if __name__ == "__main__":
    main()
    
    print("\nThe END")


