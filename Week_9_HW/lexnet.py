#wordnet functions - what data do I want to extract?
#lemmas - names, antonyms, derivationally_related_forms, pertainyms (adj) 


from nltk.corpus import wordnet as wn

class Lexnet(object):

	def __init__(self, ):
		self.wordList = list()

	def settings(self, lex, senseNum):
		self.lex = lex
		self.senseNum = senseNum
		return 1

	def words(self, lex):
		for s in list(wn.all_synsets()):
			if s.lexname == lex and :
				for l in s.lemmas:
					self.wordList.append(l.name)
		return self.wordList




if __name__ == '__main__':
	thingtolookup = 'adj.all'
	thethingssense = 1
	ln = Lexnet(thingtolookup, thethingssense)
	print ln.words()
