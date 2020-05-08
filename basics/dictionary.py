# Couple ways of creating dictionaries
# 1. Classic
my_dict = {"name":"Brandon", "age":25}

#2. use the dict object
my_dict = dict(name="Brandon", age=25)

# Accessing Values
my_dict["name"]

# Iterating

# Iterate values

for value in my_dict.values():
    print(f"Value is: {value}")

# Iterate Keys
for key in my_dict.keys():
    print(f"Key is: {key}")

# Get both in a tuple
for tup in my_dict.items():
    print(tup)

# Check for keys

"sex" in my_dict # False
"name" in my_dict # True

"Jim" in my_dict.values() # False
"Brandon" in my_dict.values() # True

# dict.clear() to empty dict

#Clones the dict
copy_dict = my_dict.copy()

#Fromkeys creates key-values pairs from comma seperated values
{}.fromkeys(["a"],10)

# We can also set a bunch of keys to default values
{}.fromkeys(["name","age", "sex", "height"],"unknown")
# comprehension way
{k:"unknown" for k in ["name","age", "sex", "height"]}

# Get - returns the value of the key and returns None if there is no key with that value.

my_dict.get("name") # "Brandon"
my_dict.get("shoe size") # None

# Pop - provide key to pop and returns the value
age = my_dict.pop("age") # 25

# Popitems remove random key from dictionary

# Update - update key-value pairs in dict
second_dict = {}

second_dict.update(my_dict) # {"name":"Brandon"}

#Dictionary comprehension

{x:x**2 for x in range(10)}

# zip() - zips two list together into the keys and values for a dict
list1 = ["AB", "BC", "ON"]
list2 = ["Alberta", "British Columbia", "Ontario"]

province_dict = dict(zip(list1,list2))
print(province_dict)

# from list of tuples to dict
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# 1. Comprehension
answer = {thing[0]: thing[1] for thing in person}
# 2. Comprehension without index ref
answer = {k:v for k,v in person}
#3. Dict constructor - this works when passing in a list of pairs.
answer = dict(person)
