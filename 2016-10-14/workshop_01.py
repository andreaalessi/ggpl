from pyplasm import *

""" pX larghezza pilastro
	pY profondità pilastro 
	bY profondità trave
"""

def structure(distancesPillars, interstoryHeights, pX, pY, bY):

	pillarXValue = []
	interstoryValue = []
	beamsZValue = []
	bX = 0		

	"""calcola lunghezza trave"""
	for e in distancesPillars: 
		bX = bX + abs(e) + pX
	bX = bX + pX

	for e in interstoryHeights:
		beamsZValue.append(-e)
		beamsZValue.append(bY)

	for e in distancesPillars:
		pillarXValue.append(pX)
		pillarXValue.append(e)

	pillarXValue.append(pX)

	for e in interstoryHeights:
		interstoryValue.append(e)
		interstoryValue.append(-bY)
	
	pillarX = QUOTE(pillarXValue)
	pillarY = QUOTE([pY])
	pillarXY = PROD([pillarX, pillarY])

	pillar = PROD([pillarXY, QUOTE(interstoryValue)])

	beamsX = QUOTE([bX])
	beamsY = QUOTE([bY])
	beamsXY = PROD([beamsX, beamsY])

	beams = PROD([beamsXY, QUOTE(beamsZValue)])


	pillarBeams = STRUCT([pillar, beams])

	return pillarBeams

result = structure([-1,-1,-1], [2,2,2,2], .2, .2, .2)
VIEW(result)