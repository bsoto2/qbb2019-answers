#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
count = 0
for i, line in enumerate(in_file):
    #print(line.rstrip('\n'))
    if line.startswith('@'):
        count += 0
        continue
    fields = line.rstrip('\n').split('\t')
    if fields[2] != ('*'):
        count += 1
print(count)