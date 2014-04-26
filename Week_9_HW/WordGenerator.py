import itertools, string, random
import lexnet

class WordGenerator(object):

	def __init__(self, bigrams=False):
		self.ln = lexnet.lexnet()
		self.bigrams = bigrams
		#object objects
		self.combos = list()
		self.ncombos = dict()
		self.nposition = dict()
		self.after = dict()
		self.before = dict()
		self.posprops = dict()
		#word vars
		self.princeton = list()
		#combinations of letters in alphabet
		self.combos = [x+y for x,y in itertools.permutations(string.ascii_lowercase, 2)]
		#analyze the bigrams found in the words

	#this is a dubiously necessary setup function that must be called for newWords to return
	#anything other than NONE...blech	
	def lexicals(self, req):
		self.princeton = self.ln.words(req)
		if self.bigrams:
			self.bigramAnalyzer()

	def select_weighted(self, d):
	   offset = random.randint(0, sum(d.itervalues())-1)
	   for k, v in d.iteritems():
	      if offset < v:
	         return k
	      offset -= v


	def select_max_at_pos(self, l, d, pos):
		max_prob = 0.0
		max_at_pos = ""
		for i in l:
			if d[i][pos] > max_prob:
				max_at_pos = i
				max_prob = d[i][pos]
		return max_at_pos



	def bigramAnalyzer(self):
		
		#bigram frequency, position, and relationships
		for word in self.princeton:
			word = word.strip().lower()
			#foundBigrams = list()
			for c in self.combos:
				self.before[c] = dict()
				self.after[c] = dict()
					
				if c in word:
					#establish relationship between bigrams
					#foundBigrams.append(c)
					#get the position of the bigram in the word
					position = word.find(c) + .5
					#add the position of the word to nposition
					if c not in self.nposition:
						self.nposition[c] = dict()
						self.nposition[c][position] = 1
					else:
						self.nposition[c][position] += 1
					#let's the bigram before and...
					if position>=2:
						prevBigram = word[position-2]+word[position-1]
						if prevBigram not in self.before:
							self.relations[c][prevBigram] = -1
						else:
							self.before[c][prevBigram] -= 1
					#also let's go ahead and get the one after
					nextBigram = word[position+2] + word[position+3]
					if nextBigram not in self.after[c]:
						self.after[c][nextBigram] = 1
					else:
						self.after[c][nextBigram] += 1
					#record that we encountered the bigram
					if c in self.ncombos:
						self.ncombos[c] += 1
					else:
						self.ncombos[c] = 1
			# for b, l in self.relations.items():
			# 	temp = list()
			# 	temp = [fb for fb in foundBigrams if fb != b]
			# 	for t in temp:
			# 		if t not in l:
			# 			l[t] = 1
			# 		else:
			# 			l[t] += 1


			#organize the position of the bigrams into ranges, using ranges to bake in randomness i.e. bigrams not 
			#showing up at only the positions they 'naturally' do
			# for b in self.nposition.iterkeys():
			# 	count = 0.0
			# 	early = 0
			# 	mid = 0
			# 	late = 0
			# 	end = 0
			# 	for p in self.nposition[b]:
			# 		count += 1
			# 		if p < 3:
			# 			early += 1
			# 		elif p < 7:
			# 			mid += 1
			# 		elif p < 11:
			# 			late += 1
			# 		elif p > 11:
			# 			end +=1
			# 	self.posprops[b] = [early/count, mid/count, late/count, end/count]


	def newWord(self):
		
		if self.bigrams:
			newWord = ""
			len_of_newWord = 4 #what do I want the word length be?
			
			#get the bigram seed that will create our word and the position we want to start it in
			seed = self.select_weighted(self.ncombos)
			seedPos = self.select_weighted(self.nposition[seed])
			
			#start keeping track of our bigrams, add the seed.
			list_of_bigrams = [0]*len_of_newWord
			list_of_bigrams[seedPos] = seed
			
			#how many do we need before and after
			numBefore = seedPos
			numAfter = len_of_newWord - seedPos
			
			#choose weighted before & after bigrams
			for p in range(numBefore):
				beforeDict = self.before[seed]
				prevBigram = self.select_weighted(beforeDict)
				list_of_bigrams[p] = prevBigram
				seed = prevBigram

			for p in range(numAfter):
				afterDict = self.after[seed]
				afterBigram = self.select_weighted(afterDict)
				list_of_bigrams[p+seedPos] = afterBigram
				seed = afterBigram

			newWord = ''.join(list_of_bigrams)
			return newWord
		else:
			newWord = random.choice(self.princeton)
			#print newWord
			return newWord

if __name__ == '__main__':

	structure = ['noun.group', 'verb.contact', 'adj.all']
	story = list()
	wg = WordGenerator(True)

	for s in structure:
		 s = wg.lexicals(s)
		 w = wg.newWord()
		 story.append(w)

	print " ".join(story)






