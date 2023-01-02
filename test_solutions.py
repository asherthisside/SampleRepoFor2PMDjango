# Prime Number
# user_input = int(input("Enter any number"))
# prime = False
# if user_input == 1 or user_input == 2:
#     prime = True
# else:
#     for i in range(2, user_input):
#         if user_input % i == 0:
#             prime = False
#             break
#         else:
#             prime = True
# if prime:
#     print("This is a prime number")
# else:
#     print("Not a prime number")


# Q - 14
mytext = "I'm a student."
vowels = ['a', 'e', 'i', 'o', 'u']
vowelcount = 0
consonantcount = 0
total_characters = len(mytext)
words = len(mytext.split(" "))
for i in mytext:
    if i.isalpha():
        if i in vowels or i.lower() in vowels:
            vowelcount += 1 
        else:
            consonantcount += 1
print(f"Total Characters: {total_characters}\nWords: {words}\nVowels: {vowelcount}\nConsonants: {consonantcount}")