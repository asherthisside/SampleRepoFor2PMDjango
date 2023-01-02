# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# choice = input("Enter your choice. Press 1. For addition, 2. For Subtraction, 3. For multiplication, and 4. For Division: ")

# if choice == '1':
#     print(num1 + num2)
# elif choice == '2':
#     print(num1 - num2)
# elif choice == '3':
#     print(num1 * num2)
# elif choice == '4':
#     print(num1 / num2)
# else:
#     print("Please enter a valid choice")

# Escape Sequence/Characters(\)

# My name is "Haaris"
# print('My name is "Haaris"')
# name = "Neha"
# print("My name is \"Haaris\". I study is \"Class 12\"")

# print(f"My name is \"{name}\"")

# \t, \n

# val = input("Enter a number:\n")
# print(val)

# Iterative Control structure
# print(1)
# print(2)
# print(3)

# automate - Run forever(Infinite loop)

# Loops - Iterative Control statements (While loop and For loop)

# Syntax: 

# Controlled Environemt - Starting condition, ending condition and update 

# Syntax: 
# Condition initialization 
# While Condition check:
    # Statements 
    # Update

# WET - Write Everything Twice
# DRY - Don't Repeat Yourself
a = 1
while a <= 10:
    print(a, end=" ")
    print(a)
    a += 1

# print(f"A = {a}")


# Print "My name is _________" 10 times using while loop

# print_count = 1
# print_string = "My name is Ajay"
# print(print_string)
# while print_count <= 10:
#     print(print_string)
#     print_count += 1


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# a = 1
# while a <= 20:
#     # print(a, end=" ")
#     if a % 2 != 0:
#         print(a, end=" ")
#     a += 1

# WAP to print all the multiples of 5 between 1 and 50

# start = 1 
# while start <= 50:
#     if start % 5 == 0:
#         print(start, end=" ")
#     start = start + 1


# Take a number a input from the user, and print its table

user_num = int(input("Enter a number you want to print table of: "))
mul = 1

while mul <= 10:
    print(f"{user_num} *  {mul} = {user_num * mul}");
    mul += 1

# Take a list with 20 numbers in it, Then print out all the numbers that are lesser than 50.

# Tokens -> 

# abc = "Thisisastring"
# a = 0
# while a < len(abc):
#     if a % 2 == 0:  
#         print(abc[a])
#     a += 1  

b = 10
while b >= 0:
    print(b)
    b -= 1