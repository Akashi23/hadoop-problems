#!/usr/bin/env python3

import random

numbers = [str(random.randint(0, 16)) for x in range(1000)]

print(' '.join(numbers))