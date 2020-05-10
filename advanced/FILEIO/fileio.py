# Use open to return a file object
f = open("input.txt")

print(f.read())

f.seek(0) # seek cursor back to the start of the file

print(f.read())

f.seek(0)

print(f.readline())

f.seek(0)

lines = f.readlines() # returns the lines of the file as a list seperated by the newline character.

print(lines)

f.close()

# double check it is closed
print(f.closed)

# WITH Blocks
# auto closes file when exits the block.

with open("input.txt") as txt:
    data = txt.read()
    print(data)

print(txt.closed)

# Writing to Files
# This will overwite the file
# If we reference a file that doesn't exist one will be created.
with open("input.txt","w") as f:
    f.write("But wait there is more!\n")
    f.write("The story doesn't end there.\n")
    f.write("To be continued...\n")

# Modes for opening files (more on python doc website)
# r - readonly
# w - write and overwrite
# a - append to a file. Always writes to end even if cursor is not there.
# r+ - Read and write to a file based on cursor position. Does not create files tho.