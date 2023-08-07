print("\nQuestion")# Exercise 1 (Lists)
print("Exercise 1:")
print("\nQuestion")# 1
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 2
names[0] = "Alex"
print(names)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 3
names.append("Frank")
print(names)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 4
names.insert(2, "Bathel")
print(names)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 5
names.pop(3)
print(names)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 6
print(names[-1])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 7
new_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Honey"]
print(new_list[2:5])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 8
countries = ["USA", "Canada", "France", "Germany"]
countries_copy = countries.copy()
print(countries_copy)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 9
for country in countries:
    print(country)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 10
animal_names = ["Lion", "Elephant", "Tiger", "Giraffe", "Monkey"]
animal_names.sort()
print("Ascending order:", animal_names)
animal_names.sort(reverse=True)
print("Descending order:", animal_names)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 11
animal_names_with_a = [name for name in animal_names if 'a' in name]
print("Animal names with 'a':", animal_names_with_a)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 12
first_names = ["John", "Alice", "Bob"]
second_names = ["Doe", "Smith", "Johnson"]
full_names = first_names + second_names
print(full_names)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# Exercise 2 (Tuples)
print("Exercise 2:")
print("\nQuestion")# 1
phones = ("samsung", "iphone", "tecno", "redmi")
print(phones[1])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 2
print(phones[-2])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 3
phones = list(phones)
phones[1] = "itel"
phones = tuple(phones)
print(phones)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 4
phones = phones + ("Huawei",)
print(phones)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 5
for phone in phones:
    print(phone)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 6
phones = list(phones)
phones.pop(0)
phones = tuple(phones)
print(phones)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 7
uganda_cities = tuple(("Kampala", "Jinja", "Entebbe", "Gulu"))
print(uganda_cities)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 8
phone1, phone2, phone3, phone4 = phones
print(phone1, phone2, phone3, phone4)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 9
print(uganda_cities[1:4])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 10
first_names = ("John", "Alice", "Bob")
second_names = ("Doe", "Smith", "Johnson")
full_names = first_names + second_names
print(full_names)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 11
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears:", count_8)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# Exercise 3 (Sets)
print("Exercise 3:")
print("\nQuestion")# 1
beverages = set(["coffee", "tea", "juice"])
print(beverages)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 2
beverages.add("soda")
beverages.update(["water", "milk"])
print(beverages)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 4
mySet.remove("kettle")
print(mySet)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 5
for item in mySet:
    print(item)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 6
set1 = {1, 2, 3, 4}
list1 = [5, 6]
set1.update(list1)
print(set1)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 7
ages = {25, 30, 35}
first_names = {"John", "Alice", "Bob"}
combined_set = ages.union(first_names)
print(combined_set)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# Exercise 4 (Strings)
print("Exercise 4:")
print("\nQuestion")# 1
num = 10
text = "The number is " + str(num)
print(text)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 2
txt = " Hello, Uganda! "
print(txt.strip())
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 3
txt = txt.upper()
print(txt)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 4
txt = txt.replace("U", "V")
print(txt)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 5
y = "I am proudly Ugandan"
print(y[1:4])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 6
x = 'All "Data Scientists" are cool!'
print(x)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# Exercise 5 (Dictionaries)
print("Exercise 5:")
print("\nQuestion")# 1
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(shoes["size"])
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 2
shoes["brand"] = "Adidas"
print(shoes)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 3
shoes["type"] = "sneakers"
print(shoes)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 4
keys = list(shoes.keys())
print(keys)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 5
values = list(shoes.values())
print(values)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 6
print("size" in shoes)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 7
for key, value in shoes.items():
    print(key, ":", value)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 8
del shoes["color"]
print(shoes)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 9
shoes.clear()
print(shoes)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 10
dictionary = {"key": "value"}
dictionary_copy = dictionary.copy()
print(dictionary_copy)
print("\n---------------------------------------------------------------------------------------------------")

print("\nQuestion")# 11
nested_dict = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Alice", "age": 30}
}
print(nested_dict)
print("\n---------------------------------------------------------------------------------------------------")
