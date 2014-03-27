import itertools, string, sys, random, operator

combos = list()
ncombos = dict()
nposition = dict()
relations = dict()
posprops  = dict()

meanLength = 4
stdLength = 1.7
numWords = 100

#functions
def select_weighted(d):
   offset = random.randint(0, sum(d.itervalues())-1)
   for k, v in d.iteritems():
      if offset < v:
         return k
      offset -= v

def select_max_at_pos(l, d, pos):
	if pos < 2:
		pos = 0
	elif pos < 6:
		pos = 1
	elif pos < 10:
		pos = 2
	elif pos > 10:
		pos = 3
	max_prob = 0.0
	max_at_pos = ""
	for i in l:
		if d[i][pos] > max_prob:
			max_at_pos = i
			max_prob = d[i][pos]
	return max_at_pos


#combinations of letters in alphabet
combos = [x+y for x,y in itertools.permutations(string.ascii_lowercase, 2)]

#bigram frequency, position, and relationships
for word in sys.stdin:
	word = word.strip().lower()
	foundBigrams = list()
	for c in combos:
		
		if c in word:
			#establish relationship between bigrams
			foundBigrams.append(c)
			if c not in relations:
				relations[c] = dict()
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
	for b, l in relations.items():
		temp = list()
		temp = [fb for fb in foundBigrams if fb != b]
		for t in temp:
			if t in l:
				l[t] += 1
			else:
				l[t] = 1


#organize the position of the bigrams into ranges, using ranges to bake in randomness i.e. bigrams not 
#showing up where they normally do
for b in nposition.iterkeys():
	count = 0.0
	early = 0
	mid = 0
	late = 0
	end = 0
	for p in nposition[b]:
		count += 1
		if p < 3:
			early += 1
		elif p < 7:
			mid += 1
		elif p < 11:
			late += 1
		elif p > 11:
			end +=1
	posprops[b] = [early/count, mid/count, late/count, end/count]



#make the words

for words in range(numWords):
	newWord = ""
	len_of_newWord = int(random.gauss(meanLength,stdLength))
	if len_of_newWord == 0:
		len_of_newWord = int(random.gauss(meanLength,stdLength))
	seed = select_weighted(ncombos)
	list_of_bigrams = list()
	list_of_bigrams.append(seed)
	tempDict = relations[seed]
	for l in range(len_of_newWord-1):
		related = select_weighted(tempDict)
		list_of_bigrams.append(related)
	for l in range(len_of_newWord):
		winner = select_max_at_pos(list_of_bigrams, posprops, l)
		newWord += winner
		list_of_bigrams.remove(winner)
	print newWord








