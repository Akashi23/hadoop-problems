#!/usr/bin/env python3

import sys
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    numbers = line.split()
    for number in numbers:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print('{}'.format(int(number)**2))

