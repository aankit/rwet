import itertools, string, sys, random, operator
import matplotlib.pyplot as plt
from collections import Counter

combos = list()
ncombos = dict()
nprops = dict()
newWords = list()

#word creation controls
absurdity = .001
shortest = 2
longest = 4
numWords = 100


#combinations of letters in alphabet
combos = [x+y for x,y in itertools.permutations(string.ascii_lowercase, 2)]

#count up how often those combinations appear in the english language, words form Wordnet
for word in sys.stdin:
	word = word.strip().lower()
	for c in combos:
		if c in word:
			if c in ncombos:
				ncombos[c] += 1
			else:
				ncombos[c] = 1

#add up the total number of matches for some math!
total_matches = 0.0
most_matches = 0
for matches in ncombos.itervalues():
	if matches > most_matches:
		most_matches = matches
	total_matches += matches

upper = most_matches/total_matches

#calculate frequency combos appear and weed out combos that are negligble
modeList = list()
mean = 0
count = 0
for c in ncombos.iterkeys():
	 x = ncombos[c]/total_matches
	 if x > absurdity:
	 	mean += x
	 	count += 1
	 	nprops[c] = x
	 	modeList.append(x)

data = Counter(modeList)
mode = data.most_common(1)
mean = mean/count

sum_of_sqdiffs = 0.0
sum_of_qdiffs = 0.0
for prop in nprops.itervalues():
	sum_of_sqdiffs = sum_of_sqdiffs + (prop - mean)**2
	sum_of_qdiffs = sum_of_qdiffs + (prop-mean)**4

alpha = (sum_of_qdiffs/count)/((sum_of_sqdiffs/count)**2)-3
stddev =(sum_of_sqdiffs/count)**(1/2)


for words in range(numWords):
	newWord = ""
	len_of_newWord = random.randint(shortest, longest)
	for l in range(len_of_newWord):
		chooser = mode[0][0]*random.paretovariate(alpha)
		winRange = 1
		winner = ""
		for c in nprops.iterkeys():
			compare = abs((nprops[c] - chooser))
			if compare < winRange:
				winner = c
				winRange = compare
		#print winner
		newWord += winner
	newWords.append(newWord)

for word in newWords:
	print word

#let's create some new nouns!





