# WAP to take an alphabetic character as the input from the user, and then print whether it is a vowel or consonants.

# user_input = input("Enter an alphabet(1 character only): ")
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# if user_input in vowels:
#     print(f"{user_input} is a vowel")
# else:
#     print(f"{user_input} is a consonant")

# Write a praogram for a user to check whether he/she is eligible to vote or not. (Minimum age required: 18 years)
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# a = 19 
# if a > 10 and a < 18 or a != 12:
#     print("All the conditions are true")
# else: 
#     print("All the conditions are not true")

# Password Creation - WAP for user to enter a password wherein you'll check it for the conditions: 
    # i. Length should be greater than 8.
    # ii. The first character should be a numeral 

# password = input("Enter your Password here: ")
# numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
# print(len(password), password[0])
# if len(password) >= 8 and int(password[0]) in numerals:
#     print("Password is Valid")
# else: 
#     print("Invalid Password")

# If-elif ladder 
z = 36 
# if z < 10:
#     print("z is lesser than 10")
# elif z < 20:
#     print("z is lesser than 20")
# elif z <  30:
#     print("z is lesser than 30")
# elif z < 40: 
#     print("z is lesser than 40")
# else:
#     print('z is greater than 40')  

# Nested If-Else 
if z > 10:
    print("z is greater than 10")
    if z > 20:
        print("z is greater than 20")
        if z > 30:
            print("z is greater than 30")
            if z > 40:
                print("z is greater than 40")
            else:
                print("z is lesser than 40")
        else:
            print("z is lesser than 30")
    else:
        print("z is lesser than 20")
else:
    print("z is lesser than 10")

# - Home Assignment -> Take three numbers and print which one is greatest, smallest and middle one among them.

# Pass statement 
if z > 30:
    pass 

print("Bye - Bye")

