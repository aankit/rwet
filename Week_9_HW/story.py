from WordGenerator import WordGenerator

structure = ['noun.body', 'verb.motion', 'noun.event']
story = list()
wg = WordGenerator(True)

for s in structure:
	 s = wg.lexicals(s)
	 w = wg.newWord()
	 story.append(w)

print " ".join(story)
