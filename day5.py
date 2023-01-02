# Operators - Symbols that help us in performing any operation

# 1. Arithmetic 
# 2. Assignment 
# 3. Comparision operators - ==, <, >, >=, <=, !=
# 4. Membership operator - in, not in
# 5. Identity operator - is
# 6. Bitwise operator - (&, |, !)
# 7. Logical operator (and, or, not)

a = 69.99
c = 78 

# print(a < c)

# ls = ['Akash', 'Bunty', 'Chandan', 'Deepak', 'Ellora']
# ls2 = [1, 2, 3, 4, 5, 6, 7]
# b = 'Bharat'
# print('Chandan' in ls)

# a = 34 
# b = a 
# print(id(a))
# print(id(ls))
# print(id(ls2))
# print(id(b))

# print(a is b)


# 1 2 4 8 16
# 1 1 1 0 0 = 7
# 1 1 0 1 0 = 11

# a = 5
# b = 10
# print(a & b)

# print(a & b)

# Binary and Logical operartions 

# print(False and False)


# Control Structure -> 1. Sequential, 2. Conditional, and 3. Iterative

# Conditional control structure -> if, else and elif (IF statement, IF-ELSE statement, IF - ELIF Ladders or NESTED IF - ELSE)

# if statement 
# syntax: 
# if condition:
    # statements

# Indentation - 
a = 6
b = 10
if a > b:
    print("A is greater than B")
else:
    print("Condition is False")

# Take a string input from the user and if its length is lesser than 10, then print that the string is invalid 
user_input = input("Enter any string: ")
if len(user_input) < 10:
    print("Invalid string") 