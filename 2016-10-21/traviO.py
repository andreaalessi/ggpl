from pyplasm import *


def structure2(distancesPillars,interstoryHeights, pX,pY,bY):

	pillarXValue = []
	interstoryValue = []
	beamsZValue = []
	traviZValue = []
	bX = 0		
	tY = 0

	"""calcola lunghezza trave"""
	for e in distancesPillars: 
		bX = bX + abs(e) + pX
	bX = bX + pX

	"""calcola lunghezza traveIncrocio"""
	for e in distancesPillars: 
		tY = pX + abs(e) + pX
	tY = tY + pX

	for e in interstoryHeights:
		beamsZValue.append(-e)
		beamsZValue.append(bY)

	"""calcola altezza traviIncrocio"""
	for e in interstoryHeights:
		traviZValue.append(-e)
		traviZValue.append(pX)

	for e in distancesPillars:
		pillarXValue.append(pX)
		pillarXValue.append(e)

	pillarXValue.append(pX)

	for e in interstoryHeights:
		interstoryValue.append(e)
		interstoryValue.append(-bY)


	traviX = QUOTE(pillarXValue)
	traviY = QUOTE([tY])
	traviXY = PROD([traviX, traviY])

	travi = PROD([traviXY, QUOTE(traviZValue)])


	rtravi = STRUCT([travi])

	return rtravi


