
name = "Brandon" # string is iterable
name_iter = iter(name)
next(name_iter) # B - keeps going until it raises a StopIteration error

#Custom For loop

def my_for(iterable, func):
    it = iter(iterable)
    while True:
        try:
            item = next(it)
        except StopIteration:
            break
        else:
            func(item)

# Generators
# are iterators created with generator functions adn use the yield keyword.
# can also yield more than once.

def count_up_to(max):
    count = 1
    while count <= max:
        yield count # when it hits yield it stops and waits for us to call next() again
        count += 1

gen = count_up_to(5)

print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3

def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        ]
    for day in days:
        yield day

'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(count=99, beverage="soda"):
    bottles = count
    while bottles >=0:
        if bottles > 1:
            yield str(bottles) + " bottles of " + beverage + " on the wall."
            bottles -= 1
        elif bottles == 1:
            yield 'Only 1 bottle of ' + beverage +' left!'
            bottles -= 1
        else:
            yield "No more " + beverage+"!"
            bottles -= 1
    raise StopIteration

'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(num=1,count=10):
    for n in range(1, count+1):
        yield num*n

'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

def get_unlimited_multiples(num=1):
    multiplier = 1
    while True:
        yield num*multiplier
        multiplier += 1


## GENERATOR EXPRESSIONS
# faster way of writing generators using () and the list comprehension syntax
# If doing like sums for instance the generator expression has way better performance than a list comp.
def nums():
    for num in range(1,10):
        yield num

g = nums()
# Expression version
g = (num for num in range(1,10))

