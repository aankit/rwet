import sys
from nltk.corpus import wordnet as wn

word = wn.synsets(sys.argv[1])
part = sys.argv[2]

for s in word:
	if s.pos == part:
		print s.name
		print s.definition
		print s.examples
		for l in s.lemmas:
			print 'lemma'
			print l.name
			print l.frame_strings

#what do I do with the definition - how does the definition play into the meaning curve?
#what do I do with examples or lack thereof?