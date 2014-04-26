#wordnet functions - what data do I want to extract?
#lemmas - names, antonyms, derivationally_related_forms, pertainyms (adj) 


from nltk.corpus import wordnet as wn

class Syns(object):

	def __init__(self, word, pos):
		self.structure = self.generateStructure(word, pos)
		self.lemmas = self.lemmatize(self.getLemmas())
		# self.definitions = self.getDefinition()
		self.examples = self.getExamples()
		self.hypernyms = self.lemmatize(self.getHypernyms())
		self.hyponyms = self.lemmatize(self.getHyponyms())
		self.frameStrings = self.getFrameStrings()
		self.lexNames = self.getLexNames()

	def generateStructure(self, word, pos):
		structure = dict()
		synsets = [synset for synset in wn.synsets(word) if synset.pos == pos]
		for synset in synsets:
			if synset.pos == pos:
				if synset.name not in structure:
					structure[synset.name] = synsets[0].path_similarity(synset)
		return structure

	def getDefinition(self, key):
		return wn.synset(key).definition

	def getExamples(self):
		examples = list()
		for synset in self.structure.keys():
			examples.extend(wn.synset(synset).examples)
		return examples

	def getLemmas(self):
		lemmas = list()
		for synset in self.structure.keys():
			lemmas.extend(wn.synset(synset).lemmas)
		return lemmas

	def getFrameStrings(self):
		frameStrings = list()
		for synset in self.structure.keys():
			synset = wn.synset(synset)
			for lemma in synset.lemmas:
				frameStrings.extend(lemma.frame_strings)
		return frameStrings

	def getLexNames(self):
		return [wn.synset(synset).lexname for synset in self.structure.keys()]

	#less specific
	def getHypernyms(self):
		hypernyms = list()
		for synset in self.structure.keys():
			synset = wn.synset(synset)
			hypernyms.extend(synset.hypernyms())
		return hypernyms

	#more specific
	def getHyponyms(self):
		hyponyms = list()
		for h in self.getHypernyms():
			hyponyms.extend(h.hyponyms())
		return hyponyms

	def lemmatize(self, thingList):
		try:
			return [t.name for tl in thingList for t in tl.lemmas]
		except:
			return [t.name for t in thingList]

#decode('ascii', errors='replace') this might be necessary

if __name__ == "__main__":
	import sys
	syn = Syns(sys.argv[1], sys.argv[2])
	print syn.definitions


