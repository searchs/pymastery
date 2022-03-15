#!/usr/bin/env python3

from typing import Dict
from collections import Counter


"""Building a Christnas tree in code """

pics = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for item in pics:
    for obj in item:
        if obj == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ")


# Check duplicates in list

a_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
counted = dict()
for item in a_list:
    if item in counted:
        counted[item] += 1
    else:
        counted[item] = 1

dups = [k for k, v in counted.items() if v > 1]
print(dups)

# Solution 2

duplicates = []
for value in a_list:
    if a_list.count(value) > 1 and value not in duplicates:
        duplicates.append(value)

print("Second Solutions:\n\t", duplicates)

# in-built solution
result = Counter(a_list)
print("Result: ", result)
