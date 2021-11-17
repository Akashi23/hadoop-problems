import sys
from functools import reduce

numbers = []

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    numbers.append(int(line))

print(reduce(lambda x, y: x+y, numbers))