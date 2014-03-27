import sys, random

nfile = open(sys.argv[1])
vfile = open(sys.argv[2])
afile = open(sys.argv[3])
nouns = [noun.strip() for noun in nfile] 
verbs = [verb.strip() for verb in vfile] 
adjs = [adj.strip() for adj in afile]

for x in range(random.randint(5, 10)):
	one = adjs[random.randint(0, len(adjs)-1)]
	two = nouns[random.randint(0, len(nouns)-1)]
	three = verbs[random.randint(0, len(verbs)-1)]
	four = adjs[random.randint(0, len(adjs)-1)]
	five = nouns[random.randint(0, len(nouns)-1)]
	print " ".join([one, two, three, four, five])

