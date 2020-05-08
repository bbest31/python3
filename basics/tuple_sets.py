# Ordered collection of items but it immutable
x = (1,2,3)
3 in x # True

# Tuples are lighter weight than lists and it makes those values safe from change if you desire so.

# iterating is the same as lists
# Also same methods are count, and index.

# Sets - unordered, unique elements.
s = set({1,2,3,4,5,5,5,5}) # {1,2,3,4,5}

# can't index but we can use in to check.

s.add(6) # doesn't work if it a duplicate.
s.remove(3) # removes the value 3.KeyError if not in the set.
s.discard(10) # removes an item but returns None if not in the set.
S = s.copy()

# UNION OF SETS

n = set({6,7,8,9})

union = n | s
intersection = n & s

# Set Comprehension

{x**2 for x in range(10)} #