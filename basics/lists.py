my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list = list(range(1,10))
# my_list = [x for x in range(1,10)] - only really use the comprehension if you want to do some mutation or logic to the items, otherwise the above is fine.

# Get the size of a list
size = len(my_list)

# Use append to add a new item to the end of a list
my_list.append(10)

#use extend to add multiple values to the end of a list.
my_list.extend([11, 12, 13])
print(my_list)

# Insert into index i moves the current item to the i+1 spot.
my_list.insert(2,2.5)

# Clear empties the list
# my_list.clear()

#Pop removes an item at a given index and returns it.
my_list.pop(0)

# Remove the first item whos value is x
my_list.remove(10)

# index(x) gives the index of the first appearance of x. index(x, n, k) gives the index of x after the index n but before the index k

my_list_2 = ["a", "b", "c"]

#join to join list items with a designated string in between.
new_string = " ".join(my_list_2)
print(new_string)

#list.index(x,y,z) - find the first position of x between the indices of y and z
my_list_2.index("a") # 0
my_list_2.index("b",0,-1) # 1

# COUNT - return the number of times x appears in a list
my_list.count(6) # 1
# reverse() - reverses the order of the list
# sort() - sorts the list in ascending order

# List slicing
# new_list = some_list[start:end:step]
my_list = list(range(0,5))

my_list[2:] # [2,3,4,5] inclusive!
my_list[:4] # [0,1,2,3] exclusive!
my_list[1:3] # [1,2] exclusive for the end

#swapping values
my_list[0], my_list[1] = my_list[1], my_list[0]

