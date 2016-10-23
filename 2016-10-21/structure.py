from pyplasm import *


def structureT(distancesPillars, interstoryHeights, pX, pY, bY, bYO):

	pillarXValue = []
	pillarXValueO = []
	interstoryValue = []
	beamsZValue = []
	interstoryValueO = []

	bX = 0

	for element in distancesPillars:
		bX = bX + abs(element) + pX
	bX = bX + pX
    
	for element in interstoryHeights:
		beamsZValue.append(-element)
		beamsZValue.append(bY)

	for element in distancesPillars:
		pillarXValue.append(pX)
		pillarXValue.append(element)

	pillarXValue.append(pX)


	for element in distancesPillars:
		pillarXValueO.append(pX)
		pillarXValueO.append(element)

	pillarXValueO.append(pX)

	for element in interstoryHeights:
		interstoryValueO.append(-element)
		interstoryValueO.append(bY)

	for element in interstoryHeights:
		interstoryValue.append(element)
		interstoryValue.append(-bY)

	beamsOX = QUOTE(pillarXValueO)
	beamsOY = QUOTE([bYO-pX])
	beamsOXY = PROD([beamsOX, beamsOY])

	beamsO = STRUCT([T(2)(pX), PROD([beamsOXY, QUOTE(interstoryValueO)])])
	
	pillarX = QUOTE(pillarXValue)
	pillarY = QUOTE([pY])
	pillarXY = PROD([pillarX, pillarY])

	pillar = PROD([pillarXY, QUOTE(interstoryValue)])

	beamsX = QUOTE([bX])
	beamsY = QUOTE([bY])
	beamsXY = PROD([beamsX, beamsY])

	beams = PROD([beamsXY, QUOTE(beamsZValue)])

	build = STRUCT([pillar, beams, beamsO])

	return build
