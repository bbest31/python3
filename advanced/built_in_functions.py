def square(num):
    return num*num

# lambda version
square2 = lambda num: num * num

print(square2(2))

add = lambda a,b: a + b

# Lambdas are small functions that can be passed as parameters. You typically wouldn't store in a variable.

# MAP
# A standard function that accepts at least two args, a function and an iterable(list, tuple, string, etc.).
# Runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure.
nums = [1,2,3,4,5,6,7,8,9]

doubles = map(lambda x : x*2, nums)
print(list(doubles))

# FILTER
# Use a lambda for each value in the iterable. Returns an object to be converted into an iterable which holds the items which made it through the filter.
my_list = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, my_list))
print(evens)

# ANY or ALL

# all returns True if all elements of an iterable are truthy
# any returns true if any elements of an iterable are truthy
all([1,2,3,4]) # True
all([0,1]) # False

all([char for char in "eio" if char in "aeiou"]) # true