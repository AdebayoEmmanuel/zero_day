#!/usr/bin/python3
# get number of rows
height = input("kindly enter the tree height: ")
# convert to integer
height = int(height)
# Get the starting spaces for the top of loop
spaces = height - 1
# There is one hash to start with that will be incremented
hashes = 1
# Save stump spaces till later
stump_space = height - 1
# Make sure the right number of rows are printed
while height != 0:
    # Print the spaces
    for i in range(spaces):
        print(' ', end="")
# print the hashes
    for i in range(hashes):
        print('#', end="")
# Newline after each row is printed
    print()
# Space is decremented by 2 each time
    spaces -= 1
# Hashes are incremented by 2 each time
    hashes += 2
# Decrement tree height each time to jump out of the loop
    height -= 1
# Print the spaces before the stump and then the hash
for i in range(stump_space):
    print(' ', end="")
print('#')
