#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
count = 0
for i, line in enumerate(in_file):
    fields = line.rstrip('\n').split('\t')
    for field in fields[11:]:
        if field.startswith('NH'):
            NH_field = field.split(':')
            if int(NH_field[2]) == 1:
                count += 1
print(count)
        