#!/usr/bin/python3
import random
import math

newlist = []
bubblesorted = []
for j in range(5):
    newlist.append(random.choice(range(1, 10)))
print("new_list : {}".format(newlist))

i = len(newlist) - 1

while i > 1:

    j = 0

    while j < i:

        if newlist[j] > newlist[j + 1]:

            temp = newlist[j]
            newlist[j] = newlist[j + 1]
            newlist[j + 1] = temp
        j += 1
    i -= 1
for k in newlist:
    bubblesorted.append(k)
print("Bubble Sorted : {}".format(bubblesorted))
