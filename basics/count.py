"""
count - Itertools
"""
from itertools import count

counter = count(start=5, step=0.1)

for value in counter:
    print(round(value, 2))
    if value >= 10:
        break
