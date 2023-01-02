ls = [1, 2, 3, "three", "four", "five", True, False]
print(ls)
print(ls[5])

# Index numbers - denotes the position of an element in a list. Index number starts from zero.
ls[3] = "MY_NAME"
# print(ls)

# Nested list - List inside a list
ls2 = [10, 20, 30, "Naveen", "Nadeem", 10, 30, 20, 30, 10, [5, 10, 15, 20]]
# print(ls2[5], type(ls2[3]))
# print(ls2[5][2])

# print(ls2[-1][-2])
# print(ls2)

# Strings also have index 
myname = "SHWETABHGANGWAR"
# print(myname[6:12])
# print(myname[0])
# print(myname[1])
# print(myname[2])
# print(myname[3])
# print(myname[4])
# print(myname[5])
# print(myname[-1])
# print(myname[-2])
# print(myname[-3])

# print(ls)

# List is mutable, ordered, indexed and it allows duplicate value

# Slicing - Proces of creating slices 
ls2 = [10, 20, 30, "Naveen", "Nadeem", 10, 30, 20, 30, 10, [5, 10, 15, 20]]
# print(ls2[5:10])

intro = "My name is Naseem Shah";
# Print out your name only 
# print(intro[11:22])

# Type Conversion 
# int() function - Convert to integer
# float() function - Convert to Floating point number 
# str() function - Convert to string 
# bool() function - Convert to tuple
# numb = "234"
# numb = True 
# n = int(numb)
# print(numb, type(numb))
# print(n, type(n))
# n_float = float(n)
# print(n_float)
# print(n - 10)

# str1 = "Hello"
# str2 = "Every"
# str3 = False 
# str4 = str(str3)
# print(str1 + str2 + str4)

# print(bool(str1))

True - 1
False - 0

str5 = 'This is a string'
ls3 = list(str5)
# print(ls3)

# Datatypes -> Type of data that can be worked upon by python
# 2 Data types 
# 1 - Singular datatypes - integer(No decimal point), floats (Have decimal points), string (Group of character) and Boolean values(True/False)
# 2 - Collection type datatypes - list, dictionary, set and tuple

# Variable -> Empty containers that are used to store values 
# 2 steps to use variable -> Variable declaration
                            # Variable Initialization

demo = 45
# type() function - Used to display the type of data stored
demo = 67.5
demo = "Havoc"
# print(type(demo))

# print(56)

# print() - Used to display the output on terminal 

# Comment -> Part of praogram that doesn't get executed!

# print("My name is Haaris Saifi")
# Compiler and Interpreter 

# Interpreter -> ??

n2 = "Heel", "Toe", "Mistletoe"
print(n2, type(n2))