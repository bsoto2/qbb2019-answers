#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
total = 0
lint = 0
for line in in_file:
    fields = line.rstrip('\n').split('\t')
    if fields[2] != '*':
        value = int(fields[4])
        total += value 
        lint += 1
average = total / lint
print(average)
