#workshop 9: parametric roof

from larlib import *
import csv
import math
from itertools import *


def makeU(alist):
    uList = []
    [uList.append(obj) for obj in alist if obj not in uList]
    return uList

def polyA(x, y):
    area = 0.0
    for i in xrange(-1, len(x) - 1):
        area += x[i] * (y[i + 1] - y[i - 1])
    return area / 2.0

def polygonCentroid(p):
	area = polyA(*zip(*p))
	X = 0
	Y = 0
	N = len(p)
	p = cycle(p)
	x1, y1 = next(p)
	for i in range(N):
		x0, y0 = x1, y1
		x1, y1 = next(p)
		c = (x0 * y1) - (x1 * y0)
		X += (x0 + x1) * c
		Y += (y0 + y1) * c
	X /= (area * 6.0)
	Y /= (area * 6.0)
	return (X, Y)

def orderClockwise(pList):
	firstP = pList[0]
	centreId = [firstP[0],firstP[1]+0.0000001]
	print centreId
	firstL = distance(centreId,firstP)
	newP = []

	while len(pList)>0:
		cos = 400
		for j in range(len(pList)):
			cos2 = findAngle(pList[j],centreId)
			
			if cos2 < cos:
				cos = cos2
				p = pList[j]
		newP.append(p)
		for t in range(len(pList)):
			if pList[t] == p:
				el = t
		pList.pop(el)
		
	return newP 

def distance(p1,p2):
	return float(math.sqrt(math.pow((p1[0] - p2[0]), 2)+math.pow((p1[1] - p2[1]), 2)))

def findAngle(p1,p2):
	return math.atan2(p1[1]-p2[1],p1[0]-p2[0])

def createRoof(nameFile):
	j=0
	s=0
	t=0
	firstS = []
	falde = []
	topS = []
	pol= []
	pol2 = []
	with open("lines/"+nameFile+".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		polylineList = []
		reader2 = reader
		row1=next(reader2)
		px = row1[0]
		py = row1[1]
	with open("lines/"+nameFile+".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		for row in reader:
			firstS.append([float(row[0])-float(px),float(row[1])-float(py)])
			firstS.append([float(row[2])-float(px),float(row[3])-float(py)])
	centreId = polygonCentroid(firstS)
	[x,y] = centreId
	centreId = [x,y]

	for f in range(len(firstS)):
		firstS[f][0]=firstS[f][0]-centreId[0]
		firstS[f][1]=firstS[f][1]-centreId[1]
	while j<len(firstS):
		pol.append(POLYLINE([firstS[j],firstS[j+1]]))
		j=j+2
	pol = STRUCT(pol)

	for i in range(len(firstS)):
		topS.append([firstS[i][0]/2.0,firstS[i][1]/2.0])

	firstS = makeU(firstS)

	topS = makeU(topS)
	topS= orderClockwise(topS)
	firstS = orderClockwise(firstS)
	topS = topS + [topS[0]]
	while t<len(topS)-1:
		pol2.append(POLYLINE([topS[t],topS[t+1]]))
		t=t+1

	plan = SOLIDIFY(STRUCT(pol2))
	plan = T(3)(4)(plan)
	firstS = firstS+ [firstS[0]]
	for p in range(len(firstS)):
		firstS[p]=firstS[p]+[float(0)]
	for k in range(len(topS)):
		topS[k]=topS[k]+[float(4)]

	while s<len(makeU(firstS)):
		falde.append(MKPOL([[firstS[s],firstS[s+1],topS[s],topS[s+1]],[[1,2,3,4]],None]))
		s = s+1
	falde = STRUCT(falde)
	roof = STRUCT([falde,plan])
	roof = T([1,2])([centreId[0],centreId[1]])(roof)
	return roof

