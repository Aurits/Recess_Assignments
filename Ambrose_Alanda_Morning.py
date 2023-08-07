# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year



# # Creating objects of the Car class
# car1 = Car("Toyota", "Corolla", 2021)
# car2 = Car("Ford", "Mustang", 2022)

# # Accessing object attributes
# print(car1.make)  # Output: Toyota
# print(car2.model)  # Output: Mustang
# print(car1.year)  # Output: 2021


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount



# # Creating an object of the BankAccount class
# account = BankAccount("123456789", 1000)

# # Accessing and modifying attributes using methods
# print(account.get_balance())  # Output: 1000

# account.deposit(500)
# print(account.get_balance())  # Output: 1500

# account.withdraw(200)
# print(account.get_balance())  # Output: 1300










# import tkinter as tk

# class Bonus:
#     # Constructor
#     def __init__(self, name, salary):
#         self.salary = salary
#         self.name = name
#     # The calculate function
#     def calculate_bonus(self):
#         return self.salary * 0.15

# def calculate():
#     name = name_entry.get()
#     salary = float(salary_entry.get())
#     emp = Bonus(name, salary)
#     bonus = emp.calculate_bonus()
#     result_label.config(text=f"{name}, the Bonus is {bonus}")

# # Create the Tkinter window
# window = tk.Tk()
# window.title("Bonus Calculator")

# # Create and pack the Name label and entry
# name_label = tk.Label(window, text="Name:")
# name_label.pack()
# name_entry = tk.Entry(window)
# name_entry.pack()

# # Create and pack the Salary label and entry
# salary_label = tk.Label(window, text="Salary:")
# salary_label.pack()
# salary_entry = tk.Entry(window)
# salary_entry.pack()
# # Create and pack the Calculate button
# calculate_button = tk.Button(window, text="Calculate", command=calculate)
# calculate_button.pack()
# # Create and pack the result label
# result_label = tk.Label(window, text="")
# result_label.pack()
# # Start the Tkinter event loop
# window.mainloop()










# class TemperatureConverter:
#     def __init__(self, celsius):
#         self._celsius = celsius

#     def get_celsius(self):
#         return self._celsius

#     def set_celsius(self, celsius):
#         self._celsius = celsius

#     def get_fahrenheit(self):
#         return (self._celsius * 9/5) + 32


# # Create an instance of the TemperatureConverter class
# converter = TemperatureConverter(37)
# # Accessing and displaying the Celsius temperature
# print("Celsius Temperature:", converter.get_celsius())
# # Accessing and displaying the Fahrenheit temperature
# print("Fahrenheit Temperature:", converter.get_fahrenheit())



# # Modifying the Celsius temperature
# converter.set_celsius(42)
# # Accessing and displaying the updated Celsius temperature
# print("Updated Celsius Temperature:", converter.get_celsius())
# # Accessing and displaying the updated Fahrenheit temperature
# print("Updated Fahrenheit Temperature:", converter.get_fahrenheit())

#Assignment
print("Assignment\n")
print("Show encapsulation with employee information to give a pay increamentatin (salary with employee information to new salary) e.g from 850000 to 1000000\n\n\n")

class Employee:
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary
    def get_name(self):
        return self.__name
    def get_employee_id(self):
        return self.__employee_id
    def get_salary(self):
        return self.__salary
    def give_pay_increment(self, increment_amount):
        if increment_amount > 0:
            self.__salary += increment_amount
            print(f"Pay increment successful! \n\nNew salary for {self.__name} (Employee ID: {self.__employee_id}) is {self.__salary}")

# Creating an instance of the Employee class
employee = Employee("Alex Wise", "EM12345", 850000)
# Displaying the initial salary
print(f"Current salary for {employee.get_name()} (Employee ID: {employee.get_employee_id()}) is {employee.get_salary()}")
# Giving a pay increment of 150000
employee.give_pay_increment(150000)
