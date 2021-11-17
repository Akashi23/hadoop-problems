#!/usr/bin/env python3

import random

numbers = [random.randint(0, 16) for x in range(1000)]

print(' '.join(str(numbers)))