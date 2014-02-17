#computer generated looped acrostic
#Aankit Patel, ITP-NYU, Reading & Writing Electronic Text

import sys

searchstr = "freedom"
counter = 0
future_lines = list()

for line in sys.stdin:
	line = line.strip()
	line_words = line.split()
	index = 0
	for word in line_words:
		#print counter
		if word == searchstr:
			pass
		elif len(word) > 3 and word[0]==searchstr[counter]:
			line_words[index] = " "+word+" "
			if counter<len(searchstr)-1:
				counter += 1
			else:
				counter = 0
		else:
			 line_words[index]= " "
		index += 1
	line = "".join(line_words)
	print line			