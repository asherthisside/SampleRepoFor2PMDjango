# Sum of 100 natural numbers 
# Sum of natural numbers between 200 and 500
# Sum of natural numbers in range provided by the user.
# user_range = int(input("Enter the limit"))
# sum_of_100_nat_num = 0
# for i in range(1, user_range + 1):
#     sum_of_100_nat_num += i 
# print(sum_of_100_nat_num)


# Nested for loops | Pattern making | Map, filter and Reduce 

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# for i in range(1, 9):
#     print(i)

# 1 2 3 4 5 6 7 8
# for i in range(1, 9):
#     print(i, end=" ")


# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55

# Nested for loops 
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, j, end="    ")
#     print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end="    ")
#     print()

# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, end="    ")
#     print()

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end="  ")
#     print()


# Increasing triangle 
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# Decreasing triangle 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

#          *
#        * * 
#      * * * 
#    * * * * 
#  * * * * * 

#          *
#        * * * 
#      * * * * * 
#    * * * * * * *
#  * * * * * * * * * 

rows = int(input("Enter no. of rows you want: "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# Reverse triangle 
# for i in range(1, rows + 1):
#     for j in range(i, rows + 1):
#         print("*", end=" ")
#     print()

for i in range(1, rows + 1):
    for j in range(i, rows):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    print()

# * * * * * 
#   * * * *
#     * * *
#       * *
#         *
for i in range(1, rows + 1):
    for j in range(1, i):
        print(" ", end=" ")
    for i in range(i, rows + 1):
        print("*", end=" ")
    
    print()