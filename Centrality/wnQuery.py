#wordnet functions - what data do I want to extract?
#lemmas - names, antonyms, derivationally_related_forms, pertainyms (adj) 


from nltk.corpus import wordnet as wn
import random

class Syns(object):

	def __init__(self, word, pos):
		self.number = 0
		self.structure = self.generateStructure(word, pos)

	def generateStructure(self, word, pos):
		structure = dict()
		synsets = [synset for synset in wn.synsets(word) if synset.pos == pos]
		for synset in synsets:
			if synset.pos == pos:
				if synset.name not in structure:
					self.number += 1
					structure[synset.name] = synsets[0].path_similarity(synset)
		return structure

	def ontoList(self, synset):
		# things to pick from
		ln = wn.synset(synset).lexname
		hyper = self.lemmatize(self.getHypernyms(synset))
		definition = self.getDefinition(synset)
		lemmas = self.lemmatize(self.getLemmas(synset))
		examples = self.getExamples(synset)
		strings = self.getFrameStrings(synset)
		hypo = self.lemmatize(self.getHyponyms(synset))
		
		# this is a fun thing to play with
		ontologyList = [ln, lemmas, hypo]
		returnList = list()
		for o in ontologyList:
			if o:
				returnList.append(o)
		return returnList

	def ontologies(self, synset, sd):
		o = self.ontoList(synset)
		inBounds = list()
		for i in range(len(o)):
			lbound = 0 - len(o)/2.0 + i
			upbound = lbound + 1
			if sd>=lbound and sd<=upbound:
				if type(o[i]) == list:
					# print "this is o[i]: " + str(o[i])
					j = random.choice(o[i])
					inBounds.append(j)
				else:
					inBounds.append(o[i])
		return inBounds

	def getDefinition(self, synset):
		return wn.synset(synset).definition

	def getExamples(self, synset):
		return wn.synset(synset).examples

	def getLemmas(self, synset):
		return wn.synset(synset).lemmas

	def getFrameStrings(self, synset):
		frameStrings = list()
		synset = wn.synset(synset)
		for lemma in synset.lemmas:
			frameStrings.extend(lemma.frame_strings)
		return frameStrings

	def getLexname(self, synset):
		return wn.synset(synset).lexname

	#less specific
	def getHypernyms(self, synset):
		root = wn.synset(synset).root_hypernyms()
		hyper = wn.synset(synset).hypernyms()
		root.extend(hyper)
		return root

	#more specific
	def getHyponyms(self, synset):
		hyponyms = list()
		for h in self.getHypernyms(synset):
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
	theList = list()
	for s in syn.structure.keys():
		print type(syn.ontologies(s, -1.5))
		


