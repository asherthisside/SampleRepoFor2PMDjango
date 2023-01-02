# Decorators - 
import time

def hello_decorator(func):
    def inner1():
        print("Calling function ...")
        func()
        print("Function ended")
    return inner1 


@hello_decorator
def to_use():
    print("This is a normal function")

# to_use()

@hello_decorator
def print10():
    for i in range(10):
        print(i)

# print10()

# to_use = hello_decorator(to_use)
# to_use()

# print10 = hello_decorator(print10)
# print10()

def create_adder(x):
    def adder(y):
        return x + y 
    return adder 

# add_45 = (create_adder(45))
# print(add_45(10))


# Create a decorator that tells how much time did the function take to get executed?
# Functions are objects 

def time_calculator(func):
    def inner():
        old_time = time.time()
        func()
        new_time = time.time()
        time_taken = new_time - old_time
        print(f"Time taken: {time_taken} seconds") 
    return inner 

@time_calculator
def print10000():
    for i in range(100001):
        pass 
    print(i)

# @time_calculator
# def add(a, b):
#     return a + b

print10000()
# add()
# Modules(Python file with some code written in it.) - Import 
# User-defined modules and Predefined modules 
# Django -> Package -> Collection of modules(Python file) -> Web development framework