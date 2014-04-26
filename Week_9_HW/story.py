import sys
from WordGenerator import WordGenerator

c = False
if sys.argv[1] == 'True':
	c = True
structure = ['noun.group', 'verb.contact', 'adj.all']
story = list()
wg = WordGenerator(c)

for s in structure:
	 s = wg.lexicals(s)
	 w = wg.newWord()
	 story.append(w)

print " ".join(story)

#tweak the lex_names to word list script to stay within pos and!
#to use path_similarity.

#pull seeds for lex_names script from source text based on limited
#number of senses - for example something like run is not best replaced
#because it is probably defining the sense of the sentence.
