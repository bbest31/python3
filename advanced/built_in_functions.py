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
any([0,1]) # True

all([char for char in "eio" if char in "aeiou"]) # true
my_list = [[1],[1],[1],[],[1]]
all_list = all([i for i in my_list if type(i) == list])
all_list = True
for i in my_list:
    if type(i) != list:
        all_list = False
print(all_list)

# SORTED
# returns a new sorted list from the items in iterable
# This method does not change the original but just returns the sorted version.
# calling .sort() changes the iterable (in-place sorting).

nums = [6,1,7,3,10]
print(sorted(nums))
print(sorted(nums, reverse=True))
# sorted() on list of dicts
# sorted(dict, key=<function/lambda>)
# Ex.
# sorted(users, key=lambda user: user['username']) - sorts by username

# MAX and MIN
# Can pass in an iterable or two or more args and select between those.
# Can also use a generator expression

names = ["Brandon", "Emma", "Name", "Anothername"]

print(max(len(name) for name in names)) # len of the longest name
print(max(names, key=lambda n: len(n))) # the longest name

# reversed()
# Returns a reverse iterator

# zip()
# Make an iterator that aggregates elements from each of the iterables
# returns an iterator of tuples, where the ith tuple contains the ith element from both argument sequences.
# the iterator stops when the shortest input iterable is exhausted.
# you also have to convert it to a list or dict afterwards if you want it to be an instance of those.
