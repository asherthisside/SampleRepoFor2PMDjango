def abc(name, standard, address):
    return f"{name} studies is {standard} class. And he is from {address}"

# print(abc(name="Ashish", standard=23, address="Karnataka"))

# kwargs 

def abc2(**kwargs):
    for a, b in kwargs.items():
        print(a, b)

# # abc2(a = 12, b = 23, c = 34, d = 45, e = 56)
# abc2(name="Aashna", hobby="Singing", job="Developer")
# dic = {'a': 12, 'b': 23, 'c': 34, 'd': 45}
# print(dic.items())

# def abc3(*args):
#     for i in args:
#         print(i)

# def childList(*children):
#     return f"The second child is: {children[1]}"

# print(childList('abc', 'def', 'ghi', 'jkl'))

def withArguments(*args):
    total = 0
    for i in args:
        total += i 
    return total 

# print(withArguments(2, 3, 4))
# print(withArguments(2, 3, 4, 7, 9, 6, 8, 4))
# print(withArguments(2, 3))

def scream(text):
    print(text.upper())

yell = scream 


def fun_one(func):
    func("hi, i am haaris saifi")

# fun_one(scream)

# scream("thisissomething")
# print(yell("mynameishaaris"))
# print(yell)


def caller(func):
    return func(10, 20)

def add(a, b):
    return a + b  

print(caller(add))