my_list = [1, 2, 3, 4]

# This syntax can be used to make a new list with an iteration.
list_2 = [x*10 for x in my_list]
print(list_2)


# LC with conditional logic

# Not mutating the value x just some conditional
list_3 = [x for x in my_list if x % 2 == 0]
print(list_3)

# Conditionally mutating x before insertion.
list_4 = [x*2 if x % 2 ==0 else x/2 for x in my_list ]
print(list_4)


# Can also use different var than iteration
# Just inserts Hi 3 times.
list_5 = ["Hi" for x in range(0,3)]
print(list_5)