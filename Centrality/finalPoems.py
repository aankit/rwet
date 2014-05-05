from wnQuery import Syns
import BellCurve
import nonsensenator
import sys, numpy, random, operator

# -- functiones ---
def select_weighted_uni(d, min, max):
	target = random.uniform(min, max)
	winner = ''
	# closest = 5
	sortedProb = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
	for k, v in sortedProb:
		if target < v:
			winner = k
	# for k, v in d.items():
	# 	if abs(target-v) < closest:
	# 		closest = abs(target-v)
	# 		winner = k		
	return winner

def pickSynset(x):
	prob = dict()
	for k,v in curves.items():
		prob[k] = v.probability(x)
	maxProb = max(prob.iteritems(), key=lambda foo:foo[1])[1]
	# print max(prob.iteritems(), key=lambda foo:foo[1])[0]
	# print maxProb
	return select_weighted_uni(prob, 0, maxProb)

def getWords(x, k):
	v = curves[k]
	sd = v.stdev(x)
	if sd<nonsense and sd>-nonsense:
		w = s.ontologies(k, sd)
		return n.giveMeNonsense(cleanOntology, len(w)/2, True)
	else:
		return s.ontologies(k, sd)

# def getWords(k, sd):
	

#				 ||   __/\				
# ______________{..}__(^/^)_________________
# ______|______|______|______|______|______|
# ___|______|______|______|______|______|___


#quick's the word, sharp's the action...and remember, surprise is on our side
n = nonsensenator.Nonsensenator()
s = Syns(sys.argv[1], sys.argv[2])
curves = dict()
varScalar = 1.2
nonsense = .25
sourceOntology = list()
cleanOntology = list()

#generate variance of each synset's distribution, create the curve, 
#and pull the full ontology for nonsensenator
for k,v in s.structure.items():
	sv = varScalar*v
	bc = BellCurve.BellCurve(v, sv)
	curves[k] = bc
	sourceOntology.extend(s.ontoList(k))

#clean up the sourceOntology to be a list of individual words, that's all
#nonsensenator will accept
for item in sourceOntology:
	if type(item) == list:
		for i in item:
			i = i.strip()
			i_words = i.split(' ')
			for w in i_words:
				if w.lower() != 'something' and w.lower() != 'somebody':
					cleanOntology.append(w)
	else:
		item = item.strip()
		item_words = item.split(' ')
		for w in item_words:
			if w.lower() != 'something' and w.lower() != 'somebody':
				cleanOntology.append(w)

# poem and line length adjusters
numLines = 20
minWords = 12

#main loop, can adjust the linspace min and max to calibrate the poem
xAxis = numpy.linspace(-.5,1.25, num=numLines)
for x in numpy.nditer(xAxis):
	line=list()
	totalWords = 0
	diff = minWords - totalWords
	words = ''
	while diff>0:
		# get the synset & the word
		synset = pickSynset(x)
		word = getWords(x, synset)
		# add words to the running list for the line
		line.append(word)
		# perform check on line length
		words += " " + word
		countWords = words.split(" ")
		for word in countWords:
			totalWords += 1
		diff = minWords - totalWords
	if line:
		toPrint = " ".join(line)
	else:
		toPrint = line[0]
	toPrint = toPrint.strip()
	print toPrint




