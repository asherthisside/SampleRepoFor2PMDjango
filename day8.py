lst = [12, 5, 10, 343, 54, 34, 15, 34, 56, 23, 20, 45, 67, 12, 11, 1, 3, 45, 43, 32, 45, 56, 56, 76, 87, 90]
print(len(lst))
# print(lst[len(lst) - 1])
# i = 0
# while i < len(lst):
#     if lst[i] <= 50:
#         print(lst[i], end=" ")
#     i += 1

# WAP to take a number as input from the user, then print all the tables from 1 to that particular number.
# ui = int(input("Enter a number"))
# table_count = 1
# i = 0 
# while table_count <= ui: 
#     print(f"Priting table of {table_count}")
#     i = 0 
#     while i <= 10:
#         print(f"{table_count} * {i} = {table_count * i}")
#         i += 1
#     # print(i)
#     table_count += 1    

# For Loop - for variable in collection

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# st = "This is a string"
# for i in st:
#     print(i)

# Range function = range(starting, ending)

# rn = list(range(1, 11, 2))
# print(rn)


# for i in range(1, 100, 2):
#     print(i, end=" ")

# for i in lst:
#     if i <= 50:
#         print(i)


# Print first 30 multiples of 4
# for i in range(1, 31):
#     print(i * 4)


# Print all the even numbers between 1 and 100, and tell the number of even numbers

# number_count = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end=", ")
#         number_count += 1

# print(f"Count of even numbers: {number_count}")
# while True:
#     print(1)

# Loop control statements - Pass, Break and Continue
# for i in range(1, 11):
#     pass


# my_name = "Shruti Bhola"
# for i in my_name:
#     print(i)
#     if i == 'i' or i == 'o' or i == 'l':
#         continue

# for i in my_name:
#     if i == 'i' or i == 'o' or i == 'l':
#         continue
#     print(i)

# print("This is abc")

# for i in lst:
#     if i % 5 == 0:
#         continue
#     print(i)

ui = int(input("Enter a number: "))
i = 1
tab = 1

while tab <= ui:
    # print(tab)
    i = 1
    while i <= 10:
        print(tab * i)
        i += 1
    tab += 1