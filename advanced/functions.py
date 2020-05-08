# Advanced Function concepts

'''
Parameter ordering
1. params
2. *args
3. default params
4. **kwargs
'''

'''
*args

special operator we can pass to functions
Gathers remaining arguments as a tuple

you can call it any name (i.e. *params, etc)
'''

def sum_all(*args):
    """Sums all the numbers given"""
    total = 0
    for num in args:
        total += num
    return total

# Unpacking Lists or Tuples using *
# If the function is expecting params as individual values then we can pass in an iterable with * to unpack it so the function can use the elements as individual values.
nums = [1,2,3,4,5,6]
print(sum_all(*nums,10, 11))


def display_name(first, last):
    print(f"{first} {last}")
# Unpacking Dictionaries
name = {"first":"Brandon","last":"Best"}

display_name(**name)

'''
**kwargs
A special operator we can pass to functions
Gathers remaining keyword arguments as a dictionary
'''

def key_word_args(**kwargs):
    print(kwargs)



key_word_args(adam="A",brandon="B",codie="c",david="D")