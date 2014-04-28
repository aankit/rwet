from wnQuery import Syns
import BellCurve
import nonsensenator
import sys, numpy, random

# -- functiones ---
def select_weighted_uni(d):
	target = random.uniform(0,1)
	winner = ''
	closest = 1
	for k, v in d.items():
		if abs(target-v) < closest:
			closest = abs(target-v)
			winner = k		
	return winner

def pickSynset(x):
	prob = dict()
	for k,v in curves.items():
		prob[k] = v.probability(x)
	return select_weighted_uni(prob)

def getWords(x, k):
	v = curves[k]
	sd = v.stdev(x)
	return s.ontologies(k, sd)

#quick's the word, sharp's the action...and remember, surprise is on our side
n = nonsensenator.Nonsensenator()
s = Syns(sys.argv[1], sys.argv[2])

curves = dict()
senseVariance = dict()

#generate variance of each synset's distribution
for k in s.structure.keys():
	v = random.uniform(0,.5)
	if k not in senseVariance:
		senseVariance[k] = v

for k,v in s.structure.items():
	try:
		bc = BellCurve.BellCurve(v, senseVariance[k])
		curves[k] = bc
	except:
		print 'No variance found for synset'


#				 ||   __/\				
# ______________{..}__(^/^)_________________
# ______|______|______|______|______|______|
# ___|______|______|______|______|______|___

# adjusters
numLines = 20
minWords = 7

#main loop
xAxis = numpy.linspace(0,1, num=numLines)
for x in numpy.nditer(xAxis):
	line=list()
	totalWords = 0
	diff = minWords - totalWords
	while diff>0:
		synset = pickSynset(x)
		words = " ".join(getWords(x, synset))
		# print words
		countWords = words.split(" ")
		for word in countWords:
			totalWords += 1
		
		line.append(words)
		diff = minWords - totalWords
	if len(line)>1:
		toPrint = " ".join(line)

	else:
		toPrint = line[0]
	toPrint = toPrint.strip()
	print toPrint




