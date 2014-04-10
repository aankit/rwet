#wordnet functions - what data do I want to extract?
#lemmas - names, antonyms, derivationally_related_forms, pertainyms (adj) 

import sys, nltk, itertools
from nltk.corpus import wordnet as wn

class LexNet(object):

	def __init__(self, ):
		self.wordList = list()

	def settings(self, lex, senseNum):
		self.lex = lex
		self.senseNum = senseNum
		return 1

	def words(self, lex, senseNum=1):
		for s in list(wn.all_synsets()):
			if s.lexname == lex and int(s.name[-2:]) == senseNum:
				for l in s.lemmas:
					self.wordList.append(l.name)
		return self.wordList


if __name__ == '__main__':
	thingtolookup = 'adj.all'
	thethingssense = 1
	ln = LexNet(thingtolookup, thethingssense)
	print ln.words()
