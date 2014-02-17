#movie scripts

import sys
import re

f = open('txt-files/thebiglebowski.txt', 'r')
all_lines = list()
walter = list()
character = list()
count = 0
for line in f:
	count += 1
	all_lines.append(line)
	offset = line.find("WALTER")
	if offset!=-1:
		walter.append(count)
for w in walter:
	lstart = w
	x = 0
	total = ""
	while True:
		check = lstart + x
		if all_lines[check] == '\n':
			if len(total)>0:
				character.append(total)
				total = ""
			break
		else:
			i = all_lines[check]
			i = i.strip()
			total = total + " " + i
			x +=1

for char_lines in character:
	print char_lines

