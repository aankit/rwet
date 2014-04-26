#wordnet functions - what data do I want to extract?
#lemmas - names, antonyms, derivationally_related_forms, pertainyms (adj) 

import sys, nltk, itertools
from nltk.corpus import wordnet as wn

class WordNet(object):

	def __init__(self, lex, senseNum=1):
		self.words = list()
		self.lex = lex
		self.senseNum = senseNum

	def settings(lex, senseNum):
		self.lex = lex
		self.senseNum = senseNum

	def wordList():
		for s in list(wn.all_synsets()):
			if s.lexname == self.lex and int(s.name[-2:]) == self.senseNum:
				for l in s.lemmas:
					self.words = l.name




# word = wn.synsets(sys.argv[1])

# combos = [(x,y) for x,y in itertools.permutations(word, 2)]

# for c in combos:
# 	print c
# 	print c[0].path_similarity(c[1])
