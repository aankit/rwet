import itertools, string, sys, random, operator
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

combos = list()
ncombos = dict()
nposition = dict()
relations = dict()

posprops  = dict()
nprops = dict() #proportion of bigram
newWords = list()

#word creation controls
absurdity = .001
shortest = 1
longest = 14
numWords = 100

#functions
def select_weighted(d):
   offset = random.randint(0, sum(d.itervalues())-1)
   for k, v in d.iteritems():
      if offset < v:
         return k
      offset -= v


#combinations of letters in alphabet
combos = [x+y for x,y in itertools.permutations(string.ascii_lowercase, 2)]

#count up how often those combinations appear in the english language, words form Wordnet
for word in sys.stdin:
	word = word.strip().lower()
	foundBigrams = list()
	for c in combos:
		
		if c in word:
			#establish relationship between bigrams
			foundBigrams.append(c)
			if c not in relations:
				relations[c] = list()
			#get the position of the bigram in the word
			position = word.find(c)
			if c in nposition:
				nposition[c] += (position,)
			else:
				nposition[c] = (position,)
			#record that we encountered the bigram
			if c in ncombos:
				ncombos[c] += 1
			else:
				ncombos[c] = 1
	# for b, l in relations.items():
	# 	temp = list()
	# 	temp = [fb for fb in foundBigrams if fb != b]
	# 	l.append(temp)




#organize the position of the bigrams into ranges, using ranges to avoid bigrams showing
#up where they normally do
for pos in nposition.iterkeys():
	count = 0.0
	early = 0
	mid = 0
	late = 0
	end = 0
	for p in nposition[pos]:
		count += 1
		if p < 2:
			early += 1
		elif p < 6:
			mid += 1
		elif p < 10:
			late += 1
		elif p > 10:
			end +=1
	posprops[pos] = (early/count, mid/count, late/count, end/count)


#add up the total number of matches for some math!
total_matches = 0.0
most_matches = 0
winner = ''
for c, m in ncombos.iteritems():
	total_matches += m
	if m > most_matches:
		most_matches = m
		winner = c


#calculate frequency combos appear and weed out combos that are negligble
modeList = list()
mean = 0
count = 0
for c in ncombos.iterkeys():
	 x = ncombos[c]/total_matches
	 if x > absurdity:				#absurdity is how low the frequency needs to be for the bigram to qualify
	 	mean += x
	 	count += 1
	 	nprops[c] = x
	 	modeList.append(x)

#sort nprops

sorted_nprops = sorted(nprops.iteritems(), key=operator.itemgetter(1), reverse=True)


#determine mode and mean
data = Counter(modeList)
mode = data.most_common(1)
mean = mean/count


sum_of_sqdiffs = 0.0
sum_of_qdiffs = 0.0
for prop in nprops.itervalues():
	sum_of_sqdiffs = sum_of_sqdiffs + (prop - mean)**2
	sum_of_qdiffs = sum_of_qdiffs + (prop-mean)**4 

alpha = (sum_of_qdiffs/count)/((sum_of_sqdiffs/count)**2)-2 #KURTOSIS, aka shape of the curve
stddev =(sum_of_sqdiffs/count)**(1/2) #standard deviation


for words in range(numWords):
	newWord = ""
	len_of_newWord = random.randint(shortest, longest)
	seed = select_weighted(ncombos)
	print seed

	# for i in range(len(sorted_ncombos)):
	# 	if chooser < sorted_ncombos[i][2]:
	# 		seeder = sorted_ncombos[i][0]
	# 	chooser -= sorted_ncombos[i][2]
	
	# for l in range(len_of_newWord):
	# 	#old pareto variate method - chooser = mode[0][0]*random.paretovariate(alpha)
	# 	#print chooser
	# 	winRange = 1
	# 	winner = ""
	# 	for c in nprops.iterkeys():
	# 		compare = abs((nprops[c] - chooser))
	# 		if compare < winRange:
	# 			winner = c
	# 			winRange = compare
	# 	#print winner
	# 	newWord += winner
	# newWords.append(newWord)

# for word in newWords:
# 	print word

#let's create some new nouns!





