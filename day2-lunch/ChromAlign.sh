#!/bin/bash

INPUT=~/qbb2019-answers/day2-lunch/SRR072893.sam

# for $INPUT
# do
	cut -f 3 | 
	grep -v "2L" |
	grep -v "2R" |
	grep -v "3L" |
	grep -v "3R" |
	grep -v "4" |
	grep -v "X" |
	grep -v "Y" |
	sort -f 3
	uniq -c > ChromMatch.txt
# done