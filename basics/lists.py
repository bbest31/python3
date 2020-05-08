my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#use extend to add multiple values to the end of a list.

my_list.extend([10, 11, 12])
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