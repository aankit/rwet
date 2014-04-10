import itertools, string, sys, random, operator
from lexnet import LexNet

class WordGenerator(object):

	def __init__(self, bigrams=False):
		self.ln = LexNet()
		self.bigrams = bigrams
		#object objects
		self.combos = list()
		self.ncombos = dict()
		self.nposition = dict()
		self.relations = dict()
		self.posprops  = dict()
		#word vars
		self.princeton = list()
		#combinations of letters in alphabet
		self.combos = [x+y for x,y in itertools.permutations(string.ascii_lowercase, 2)]
		#analyze the bigrams found in the words

	#this is a dubiously necessary setup function that must be called for newWords to return
	#anything other than NONE...blech	
	def lexicals(self, req, senseReq=1, length=random.randint(2,5)):
		self.length = length
		#wordnet list for this guy
		# print ln.lex
		# print ln.senseNum
		self.princeton = self.ln.words(req, senseReq)
		# print self.princeton
		if self.bigrams:
			self.bigramAnalyzer()

	def select_weighted(self, d):
	   offset = random.randint(0, sum(d.itervalues())-1)
	   for k, v in d.iteritems():
	      if offset < v:
	         return k
	      offset -= v


	def select_max_at_pos(self, l, d, pos):
		pos = pos - 2
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
			foundBigrams = list()
			for c in self.combos:
				if c not in self.relations:
					self.relations[c] = dict()	
				if c in word:
					#establish relationship between bigrams
					foundBigrams.append(c)
					#get the position of the bigram in the word
					position = word.find(c)
					if c in self.nposition:
						self.nposition[c] += (position,)
					else:
						self.nposition[c] = (position,)
					#record that we encountered the bigram
					if c in self.ncombos:
						self.ncombos[c] += 1
					else:
						self.ncombos[c] = 1
			for b, l in self.relations.items():
				temp = list()
				temp = [fb for fb in foundBigrams if fb != b]
				for t in temp:
					if t not in l:
						l[t] = 1
					else:
						l[t] += 1


			#organize the position of the bigrams into ranges, using ranges to bake in randomness i.e. bigrams not 
			#showing up at only the positions they 'naturally' do
			for b in self.nposition.iterkeys():
				count = 0.0
				early = 0
				mid = 0
				late = 0
				end = 0
				for p in self.nposition[b]:
					count += 1
					if p < 3:
						early += 1
					elif p < 7:
						mid += 1
					elif p < 11:
						late += 1
					elif p > 11:
						end +=1
				self.posprops[b] = [early/count, mid/count, late/count, end/count]


	def newWord(self):
		
		if self.bigrams:
			newWord = ""
			len_of_newWord = self.length
			seed = self.select_weighted(self.ncombos)
			list_of_bigrams = list()
			list_of_bigrams.append(seed)
			tempDict = self.relations[seed]
			for l in range(len_of_newWord):
				related = self.select_weighted(tempDict)
				list_of_bigrams.append(related)
			for l in range(len_of_newWord):
				winner = self.select_max_at_pos(list_of_bigrams, self.posprops, l)
				newWord += winner
				if winner in list_of_bigrams:
					list_of_bigrams.remove(winner)
			return newWord
		else:
			newWord = random.choice(self.princeton)
			#print newWord
			return newWord

if __name__ == '__main__':
	structure = ['noun.body', 'verb.motion', 'noun.event']
	story = list()
	wg = WordGenerator()

	for s in structure:
		 s = wg.lexicals(s)
		 w = wg.newWord()
		 # print s






