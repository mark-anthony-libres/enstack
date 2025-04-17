
import random
"""
Given a list of tuples A = (x, y), where x is an integer from 0 to 13 and y is an integer
from 0 to 3, with all possible values of A without repetition and sorted by y then x in
ascending order, write a pseudocode to shuffle A.

require:
x = range from 0 to 13 witch is 14 items including 0 = [0, 1, 2, 3, ... 13]
y - range from 0 to 3 witch is 4 items including 0 = [0, 1, 2, 3]
sort by y

14x4 = 56 unique values
"""

A : list = []

"""
however if i just put range(0,3) it will only result to [0, 1, 2] not including 3, 
the question said that the x should range from 0 to 13 and y is 0 to 3 logically
"""

for x in range(0, 14):
    for y in range(0, 4):
        A.append((x, y))

# the length of A is 56 unique values
print(len(A))

# random.shuffle(A)

print(f"Before sorting: {A}")

"""
using a builtin method "sort" to order items by y axis in ascending order
by default it will sort item by item[1] the y axis. the item[0] (x) is secondary sort option
"""
A.sort(key=lambda item: (item[1], item[0]))

print(f"After sorting: {A}")

random.shuffle(A)

