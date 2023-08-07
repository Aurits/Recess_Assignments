#AMBROSE ALANDA WEEK 2
#Inheritence

#Assignment, circle and rectangle do inherit from shape class where we calculate the area and perimeter
# print("Assignment, circle and rectangle do inherit from shape class where we calculate the area and perimeter")
# class Shape:
# 	def calculate_area(self):
# 		pass

# 	def calculate_perimeter(self):
# 		pass

# class Circle(Shape):
	
# 	def __init__(self, radius):
# 		self.radius = radius

# 	def  calculate_area(self):
# 		return 3.14*self.radius*self.radius

# 	def calculate_perimeter(self):
# 		return 2*self.radius*3.14

# class Rectangle(Shape):
	
# 	def __init__(self, length, width):
# 		self.length = length
# 		self.width = width

# 	def calculate_area(self):
# 		return self.length*self.width

# 	def calculate_perimeter(self):
# 		return 2*(self.length+self.width)
		
# #create the objects of the child classes

# circle = Circle(5)

# rectangle = Rectangle(5,8)

# print("For the circle:")
# print(circle.calculate_area())
# print(circle.calculate_perimeter())

# print("\nFor the rectangle:")
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())

#multiple inheritence

# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def get_color(self):
#         return self.color


# class Material:
#     def __init__(self, material):
#         self.material = material

#     def get_material(self):
#         return self.material


# class Square(Shape, Material):
#     def __init__(self, side_length, color, material):
#         Shape.__init__(self, color)
#         Material.__init__(self, material)
#         self.side_length = side_length

#     def calculate_area(self):
#         return self.side_length * self.side_length


# # Create an object of the Square class
# square = Square(5, 'red', 'wood')

# # Access methods from Shape class
# print(square.get_color())

# # Access methods from Material class
# print(square.get_material())

# # Access methods from Square class
# print(square.calculate_area())




# #method overriding
# print("\nmethod overriding")
# class Animal:

# 	def make_sound(self):
# 		print("The big animal does make sound")

# class Dog(Animal):
	
# 	def make_sound(self):
# 		print("This sound is made by the dog!!")

# class Cat(Animal):
	
# 	def make_sound(self):
# 		print("This is the sound made by the cat")

# def sound_made(animal):
# 	animal.make_sound()	


# animal = Animal()
# dog = Dog()
# cat = Cat()

# animal.make_sound()
# sound_made(dog)
# sound_made(cat)
		
	
		
#Polymorphism
#Allows you to write code that can work with different objects'
#we shall do method overriding and method overriding

#Overloadin

# def add(self,a ,b):
# 	return a+b

# def add(self,a,b,c):
# 	return a+b+c


# print(add(1,3))

# print(add(1,2,3))

#Abstraction
#Allows you to focus on essential features and hide from the unnecessary details
# print("Demonstration of abstraction")
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
# 	@abstractmethod
# 	def start(self):
# 		pass

# 	@abstractmethod
# 	def stop(self):
# 		pass


# class Car(Vehicle):

# 	def start(self):
# 		print("Starting the car----------")

# 	def stop(self):
# 		print("Stopping the car-----------")


# class Truck(Vehicle):

# 	def start(self):
# 		print("Starting the Truck----------")

# 	def stop(self):
# 		print("Stoppimg the Truck-----------")


# #create the objects
# car = Car()
# truck = Truck()

# car.start()
# car.stop()
# print("\n")
# truck.start()
# truck.stop()

#exercie
# print("Demonstration of abstraction for area of the circle and rectangle")
# from abc import ABC, abstractmethod

# class Shape(ABC):
# 	@abstractmethod
# 	def calculate_area(self):
# 		pass   


# class Circle(Shape):
# 	def __init__(self, radius):
# 	 	self.radius = radius

# 	def calculate_area(self):
# 		return 3.14*self.radius


# class Rectangle(Shape):
# 	def __init__(self,length,width):
# 		self.length  = length
# 		self.width = width

# 	def calculate_area(self):
# 		return self.length*self.width

# #the objects
# circle = Circle(3)
# rectangle = Rectangle(4,3)

# print("The results")
# print("the area of the circle is",circle.calculate_area())
# print("\nthe area of the rectangle is", rectangle.calculate_area())


#Assignment
# How name you file when sendind on my email jeff.geoff.cis@gmail.com
# Accepted Format: A1_firstname_surname_morning.py | firstname_surname_afternoon.py

#Assignment 1 : Deadline 01 July 2023 Time 5:00PM EAT
# Create a receipt printing program with GUI interface, 
# a more advanced detail earns you more points.

print("Create a receipt printing program with GUI interface")

import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas

def generate_receipt():
    customer_name = name_entry.get()
    customer_address = address_entry.get()
    items = []
    for i in range(len(item_entries)):
        item_name = item_entries[i].get()
        item_quantity = quantity_entries[i].get()
        item_price = price_entries[i].get()
        
        if not item_quantity:
            messagebox.showwarning("Error", "Please fill in the quantity for item {}".format(i+1))
            return

        total_price = int(item_quantity) * float(item_price)
        items.append((item_name, item_quantity, item_price, total_price))

    receipt_text = "Customer: {}\n".format(customer_name)
    receipt_text += "Address: {}\n\n".format(customer_address)

    # Add items table to the receipt
    receipt_text += "Item\t\tQuantity\tUnit Price\tTotal Price\n"
    receipt_text += "-----------------------**************----------------------\n"
    for item in items:
        receipt_text += "{}\t\t{}\t\tUGX{}\t\tUGX{:.2f}\n".format(item[0], item[1], item[2], item[3])
    receipt_text += "-----------------------**************----------------------\n"

    total_price = sum([item[3] for item in items])
    receipt_text += "Total Price: UGX{:.2f}\n".format(total_price)
    receipt_text += "Thank you for your purchase!"

    receipt_textbox.delete(1.0, tk.END)  # Clear any previous content
    receipt_textbox.insert(tk.END, receipt_text)

    generate_pdf_receipt(customer_name, customer_address, items)


def generate_pdf_receipt(customer_name, customer_address, items):
    file_name = "{}_receipt.pdf".format(customer_name.replace(" ", "_"))

    c = canvas.Canvas(file_name)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Receipt")
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Customer: {}".format(customer_name))
    c.drawString(50, 730, "Address: {}".format(customer_address))
    c.drawString(50, 700, "-----------------------**************----------------------")
    y = 670
    for item in items:
        c.drawString(50, y, "Item: {}".format(item[0]))
        c.drawString(200, y, "Quantity: {}".format(item[1]))
        c.drawString(320, y, "Unit Price: UGX{}".format(item[2]))
        c.drawString(450, y, "Total Price: UGX{:.2f}".format(item[3]))
        y -= 20
    c.drawString(50, y, "-----------------------**************----------------------")
    total_price = sum([item[3] for item in items])
    c.drawString(50, y-20, "Total Price: UGX{:.2f}".format(total_price))
    c.drawString(50, y-50, "Thank you for your purchase!")
    c.save()

    messagebox.showinfo(f"Receipt Generated", f"Receipt has been generated as {file_name}")


def add_item_field():
    row = len(item_entries) + 4  # Add 2 to account for existing rows (Customer Name and Address)
    
    # Item Name label and entry
    item_label = tk.Label(app, text="Item Name:")
    item_label.grid(row=row, column=0, padx=5, pady=5)
    item_entry = tk.Entry(app)
    item_entry.grid(row=row, column=1, padx=5, pady=5)
    item_entries.append(item_entry)
    item_labels.append(item_label)

    # Quantity label and entry
    quantity_label = tk.Label(app, text="Quantity:")
    quantity_label.grid(row=row, column=2, padx=5, pady=5)
    quantity_entry = tk.Entry(app)
    quantity_entry.grid(row=row, column=3, padx=5, pady=5)
    quantity_entries.append(quantity_entry)
    quantity_labels.append(quantity_label)

    # Price label and entry
    price_label = tk.Label(app, text="Unit Price:")
    price_label.grid(row=row, column=4, padx=5, pady=5)
    price_entry = tk.Entry(app)
    price_entry.grid(row=row, column=5, padx=5, pady=5)
    price_entries.append(price_entry)
    price_labels.append(price_label)


def remove_item_field(row):
    item_entries[row - 4].destroy()
    item_labels[row - 4].destroy()
    quantity_entries[row - 4].destroy()
    quantity_labels[row - 4].destroy()
    price_entries[row - 4].destroy()
    price_labels[row - 4].destroy()

    item_entries.pop(row - 4)
    item_labels.pop(row - 4)
    quantity_entries.pop(row - 4)
    quantity_labels.pop(row - 4)
    price_entries.pop(row - 4)
    price_labels.pop(row - 4)


def clear_fields():
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    for entry in item_entries:
        entry.destroy()
    for label in item_labels:
        label.destroy()
    for entry in quantity_entries:
        entry.destroy()
    for label in quantity_labels:
        label.destroy()
    for entry in price_entries:
        entry.destroy()
    for label in price_labels:
        label.destroy()
    item_entries.clear()
    item_labels.clear()
    quantity_entries.clear()
    quantity_labels.clear()
    price_entries.clear()
    price_labels.clear()
    receipt_textbox.delete(1.0, tk.END)


# Create the main application window
app = tk.Tk()
app.title("Receipt Printing Program")
app.configure(bg="lightgray")

# Create and arrange the widgets
name_label = tk.Label(app, text="Customer Name:", bg="lightgray")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=5, pady=5)

address_label = tk.Label(app, text="Customer Address:", bg="lightgray")
address_label.grid(row=1, column=0, padx=5, pady=5)
address_entry = tk.Entry(app)
address_entry.grid(row=1, column=1, padx=5, pady=5)

item_entries = []
quantity_entries = []
price_entries = []
item_labels = []
quantity_labels = []
price_labels = []

add_item_button = tk.Button(app, text="Add Item", command=add_item_field)
add_item_button.grid(row=2, column=0, padx=5, pady=5)

print_button = tk.Button(app, text="Print Receipt", command=generate_receipt)
print_button.grid(row=2, column=1, padx=5, pady=5)

clear_button = tk.Button(app, text="Clear Fields", command=clear_fields)
clear_button.grid(row=2, column=2, padx=5, pady=5)

receipt_textbox = tk.Text(app, height=10, width=60)
receipt_textbox.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

# Start the application event loop
app.mainloop()
