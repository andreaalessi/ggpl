from pyplasm import * 
from hw import workshop_10 as w10
from hw import workshop_09 as w09
from hw import tree
import csv


def suburban_neighborhood(filename):
	with open("lines/"+filename + ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		street = []
		for line in reader:
			street.append([float(line[0]),float(line[1])])
			street.append([float(line[2]),float(line[3])])

	streets = []
	curve = []
	cont = 0
	for i in range(len(street)):
		curve.append(street[i])
		cont += 1
		if cont == 2:
			strada = MAP(BEZIER(S1)(curve))(INTERVALS(1)(5))
			curve = []
			streets.append(strada)
			cont= 0

	#create from file .lines the street with the curve

	streets = STRUCT(streets)
	streetsB=streets
	streets = OFFSET([10,10])(streets)
	streetsB = OFFSET([15,15])(streetsB)
	streets = PROD([QUOTE([3]),streets])
	streetsB = PROD([QUOTE([1]),streetsB])
	streets = R([1,3])(-PI/2)(streets)
	streetsB = R([1,3])(-PI/2)(streetsB)

	#create box

	box = BOX([1,2])(streets)
	boxUp = OFFSET([0,0,10])(box)
	box = OFFSET([0,0,40])(box)
	streets = T(3)(52)(streets)
	streetsB = T([1,2,3])([-2,-2,51])(streetsB)
	boxUp = T(3)(40)(boxUp)
	streets = MATERIAL([.01,.01,.01,1,  106/255.0,101/255.0,97/255.0,1,  0,0,0,1, 0,0,0,1, 1]) (streets)
	boxUp = TEXTURE("texture/prato1.jpg")(boxUp)
	box = TEXTURE("texture/redWood.jpg")(box)
	box = STRUCT([box,boxUp])
	boxStreets= STRUCT([box,streets,streetsB])
	boxStreets = T(3)(-51)(boxStreets)
	#VIEW(boxStreets)
	
	#add the houses

	house = w10.MultistoreyHouse()
	house = R([1,2])(PI/2)(house)
	house = S([1,2,3])([(SIZE([1])(streets)[0])/(17*SIZE([1])(house)[0]),(SIZE([2])(house)[0])/(0.5*SIZE([2])(house)[0]),(SIZE([3])(streets)[0])/(.1*SIZE([3])(house)[0])]) (house)
	house2 = T(2)(-50)(house)
	house3 = T(2)(-100)(house)
	house4 = T(2)(-150)(house)

	complex1 = STRUCT([house,house2,house3,house4])
	complex1 = T([1,2])([660,280])(complex1)
	complex2 = R([1,2])(PI)(complex1)
	complex2 = T([1,2])([590*2,230*2])(complex2)
	r1r2 = STRUCT([complex1,complex2])
	r3r4 = T([1,2])([250,-320])(r1r2)
	r3r4 = R([1,2])(PI/9)(r3r4)

	complex5 = R([1,2])(PI)(complex1)
	complex5 = T([1,2])([550*3,100])(complex5)
	complex5 = R([1,2])(PI/9)(complex5)


	houseB = w10.MultistoreyHouse()
	houseB = S([1,2,3])([(SIZE([1])(streets)[0])/(15*SIZE([1])(houseB)[0]),(SIZE([2])(houseB)[0])/(0.4*SIZE([2])(houseB)[0]),(SIZE([3])(streets)[0])/(.07*SIZE([3])(houseB)[0])])(houseB)
	houseB = R([1,2])(-PI/2)(houseB)
	house2 = T(2)(-60)(houseB)
	house3 = T(2)(-60)(house2)
	house4 = T(2)(-60)(house3)
	house5 = T(2)(-60)(house4)
	house6 = T(2)(-60)(house5)
	house7 = T(2)(-60)(house6)
	house8 = T(2)(-60)(house7)
	house9 = T(2)(-60)(house8)
	house10 = T(2)(-60)(house9)

	res1=STRUCT([houseB,house2,house3,house4,house5,house6,house7,house8,house9,house10])
	res1 = T([1,2])([650,700])(res1)
	res1 = R([1,2])(PI/9)(res1)

	h1c =  w10.MultistoreyHouse()
	h1c = S([1,2,3])([(SIZE([1])(streets)[0])/(14*SIZE([1])(h1c)[0]),(SIZE([2])(h1c)[0])/(0.4*SIZE([2])(h1c)[0]),(SIZE([3])(streets)[0])/(.07*SIZE([3])(h1c)[0])])(h1c)
	h1cr1 = R([1,2])(-PI/2)(h1c)
	h1cr2= R([1,2])(PI/9)(h1cr1)
	h1cr = R([1,2])(-PI/9)(h1cr1)
	h1c = T([1,2])([670,400])(h1cr)
	h2c = T([1,2])([670,560])(h1cr)

	h11c = T([1,2])([770,380])(h1cr)
	h12c = T([1,2])([770,480])(h1cr)

	h3c	= T([1,2])([970,420])(h1cr2)
	h4c = T([1,2])([970,490])(h1cr2)
	h5c = T([1,2])([940,550])(h1cr2)
	h6c = T([1,2])([900,630])(h1cr2)

	h7c= T([1,2])([250,320])(h1c)
	h8c= T([1,2])([250,400])(h1c)
	h9c= T([1,2])([250,480])(h1c)
	h10c= T([1,2])([250,560])(h1c)

	h1=w10.MultistoreyHouse()
	h1 = S([1,2,3])([(SIZE([1])(streets)[0])/(14*SIZE([1])(h1)[0]),(SIZE([2])(h1)[0])/(0.4*SIZE([2])(h1)[0]),
		 (SIZE([3])(streets)[0])/(.07*SIZE([3])(h1)[0])])(h1)
	h1 = T([1,2])([-20,720])(h1c)
	h2 = T([1,2])([60,0])(h1)
	h3 = T([1,2])([130,0])(h1)
	h4 = T([1,2])([220,0])(h1)
	h5 = T([1,2])([290,0])(h1)


	hdx1 = T([1,2])([-150,-100])(h1)
	hdx2 = T([1,2])([-70,120])(hdx1)

	ho1=w10.MultistoreyHouse()
	ho1b = S([1,2,3])([(SIZE([1])(streets)[0])/(14*SIZE([1])(ho1)[0]),(SIZE([2])(ho1)[0])/(0.4*SIZE([2])(ho1)[0]),
		 (SIZE([3])(streets)[0])/(.07*SIZE([3])(ho1)[0])])(ho1)
	ho1= T([1,2])([800,360])(ho1b)
	ho1 = R([1,2])(PI/9)(ho1)
	ho2= T([1,2])([100,70])(ho1)

	h13c = R([1,2])(PI)(ho1b)
	h13c = T([1,2])([750,850])(h13c)
	h14c = T([1,2])([-100,100])(h13c)
	h15c = T([1,2])([100,0])(h14c)
	h16c = T([1,2])([-40,-100])(h14c)

	# add trees
	
	treesList = [tree.albero()]
	for i in range(3):
		treesList.append(T([1,2])([(2*i)+i,(2*i)])(tree.albero()))
	trees = STRUCT(treesList)
	trees = S([1,2,3])([(SIZE([1])(streets)[0])/(3.5/2*SIZE([1])(house)[0]),(SIZE([1])(streets)[0])/(3.5/2*SIZE([1])(house)[0]),(2*SIZE([3])(streets)[0])/(0.03*SIZE([3])(house)[0])]) (trees)
	treesrp = R([1,2])(1.50)(trees)
	treesrm = R([1,2])(-2)(trees)
	#quadrante centrale
	tree0 = T([1,2])([620,590])(treesrp)
	tree1 = T([1,2])([640,670])(treesrm)
	tree6 = T([1,2])([820,690])(treesrm)
	tree7 = T([1,2])([850,690])(treesrm)
	tree8 = T([1,2])([620,490])(treesrm)

	#quadrante altodx
	tree2 = T([1,2])([450,270])(treesrm)
	tree3 = T([1,2])([460,370])(treesrm)
	tree4 = T([1,2])([450,480])(treesrm)
	tree5 = T([1,2])([460,590])(treesrm)

	#quadrante sx
	tree9 = T([1,2])([950,180])(treesrp)
	#quadrante dx
	tree10 = T([1,2])([1000,900])(treesrm)

	#combine the various elements

	neighborhood=STRUCT([boxStreets,r1r2])
	neighborhood=STRUCT([neighborhood,r3r4])
	neighborhood=STRUCT([neighborhood,complex5])
	neighborhood=STRUCT([neighborhood,res1])
	neighborhood=STRUCT([neighborhood,h1c,h2c,h3c,h4c,h5c,h6c,h7c,h8c,h9c,h10c,h11c,h12c])
	neighborhood=STRUCT([neighborhood,h1,h2,h3,h4,h5])
	neighborhood=STRUCT([neighborhood,hdx1,hdx2])
	neighborhood=STRUCT([neighborhood,ho1,ho2])
	neighborhood=STRUCT([neighborhood,h13c,h14c,h15c,h16c])
	neighborhood=STRUCT([neighborhood,tree0,tree1,tree2,
		tree3,tree4,tree5,tree6,tree7,tree8,tree9,tree10])


	return neighborhood


def main():
	VIEW(suburban_neighborhood("street"))
if __name__=='__main__':
	main()
