# higher order functions
# 1. Pass functions as args
# 2. define a function within another function and call it within it.
# 3. can also return a function

from random import choice
from functools import wraps
import time

def make_choice_func(color):
    def get_choice():
        c = choice(("RED", "BLUE", "GREEN", color)) # even tho color was not passed into the inner func it is accessible.
        return c
    return get_choice

my_choice = make_choice_func("YELLOW")
print(my_choice())

# Decorator
# A function that wraps other functions and enhance their behaviour
# usually want your wrapper function to have *args and **kwargs for multiple fn with different parameter numbers to be wrapped.

def be_polite(fn):
    @wraps(fn) # this anotation hellps preserve the metadata of fn so you can access __name__ or __doc__
    def wrapper(*args, **kwargs):
        print("Nice to meet you.")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    """Prints a greeting"""
    print("My name is Brandon")

greeting = be_polite(greet)
greeting()

# With Decorator Syntax

@be_polite
def hello():
    print("My name is Brandon.")

hello() # no need to set hello = be_polite(greet)

###################################################

# Ex. Speed Test Decorator


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Time Elapsed: {end - start}")
        return result
    return wrapper

@speed_test
def sum_nums():
    return sum(x for x in range(10000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(10000000)])

sum_nums()
sum_nums_list()


# Decorator that takes in a parmeter
# Not working code!

def decorator(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return inner

#When we write
@decorator
def func(*args, **kwargs):
    pass
# We're really doing
func = decorator(func)

#When we write
@decorator(arg)
def func(*args, **kwargs):
    pass
# We are really doing:
func = decorator(arg)(func)