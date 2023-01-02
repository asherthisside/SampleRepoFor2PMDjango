# String concatenation
s1 = "Hello, "
s2 = "How are you?"
# print(s1 + s2)  # Concatenation
# print(10 + 45)  # Addition
# print("10" + "45")
# print(type("45"))
# print("Hello" + 23)     # Error(TypeError)

my_name = "Akanksha"
my_class = 12
my_address = "Nainital"

# My name is my_name. I study in class my_class. And I live in my_address
# print("My name is " + my_name + ". I study in class " + my_class + ". I live in " + my_address)

# Formatted strings - f-strings 
# print(f"My name is {my_name}. I study in class {my_class}, and I live in {my_address}")

# print("Hello class, How are you?")

# employee_name = "Neha"
# employee_salary = 34566785446757
# employee_designation = "Sr. Technical counselor"

# print(f"This employee's name is {employee_name}. She earns {employee_salary} per month and she works as {employee_designation}")

# print("This employee's name is {}. She earns {} per month. She works as {}".format(employee_name, employee_salary, employee_designation, my_name))

# User Input -> 
# user_input = input("Enter a number: ")
# print("You entered", user_input)
# user_int = int(user_input)
# print(user_int, type(user_int))
# print("Bye-Bye")

# Type-cast 
# a = 34
# b = float(a)
# c = int(b)

# d = str(a)
# print(a, type(a))
# print(d, type(d))

# Age, class, Roll Number 
# I am ______ years old, I study in class ______ and have a roll number _____.

# user_age = int(input("Enter your age"))
# user_class = int(input("Enter your class"))
# user_roll = int(input("Enter your roll number"))

# print(f"I am {user_age} years old. I study in class {user_class} and have a roll number {user_roll}")

# print("I am {} years old. I study in class {} and have a roll number {}".format(user_age, user_class, user_roll))

# List - Ordered, Indexed, Mutable, Allows duplicate values
fruits = ['Apple', 'Mango', 'Banana', 'Guava']
ls = [1, 2, 3, 4, "five", "six", True, False, [10, 20, 30], 45, 1, 2, 1, 3]
# print(type(ls[8]))
 
fruits[0] = 'Watermelon'

print(fruits)

# List slicing 
print(ls[2:9:2])
