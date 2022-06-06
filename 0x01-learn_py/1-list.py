#!/usr/bin/python3
import random
import math

new_list = []
for j in range(1, 10):
    if len(new_list) == 5:
        break
    new_list.append(random.choice(range(1, 10)))
print("new_list : {}".format(new_list))
