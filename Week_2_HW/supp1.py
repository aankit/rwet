import sys

whatever = list()
stuff = list()

for tomato in sys.stdin:
	tomato = tomato.strip()
	whatever.append(tomato)

print whatever

#whatever.append(tomato)

# lIndex = 0
# for l in lines:
# 	toPrint = ""
# 	words = l.split()
# 	if lIndex%2==0 and lIndex!=0:
# 		wIndex =0
# 		for w in words:
# 			if wIndex%2==0 and w!="":
# 				toPrint = toPrint + " " + w
# 			wIndex += 1
# 		print toPrint
		
# 	lIndex += 1
	
