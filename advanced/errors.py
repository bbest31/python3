# Raising our own errors
import re as regex
from random import randint 

# raise ValueError("invalid value")

#Syntax Error
# NameError -error in variable name calling
# TypeError - trying to do an operation to an invalid type.
# IndexError - trying to access an element at an index that doesn't exist.


# Try and Except

try:
    foobar
except NameError as error:
    print(error)

print("after the try/except")


# Try, Except, Else, Finally
try:
    num = int(input("Please enter a number: "))
except:
    print("That is not a number!")
else:
    print("Else runs if there is no problem")
finally:
    print("finally block runs no matter what")


# Debugging with PDB

import pdb
pdb.set_trace()
tehe = "Hello"
number = 123

 # pauses the code so we can step through or look at variable states.

# common PDB commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finish debugging)
# variable_name - gives you the current value
