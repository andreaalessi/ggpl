import csv
from pyplasm import *
from hw import workshop_03
from hw import workshop_07
from hw import workshop_09

def svg2house(extWalls,intWall,windows,intDoors,extDoors,intDoors2floor,windows2floor,cortile,holeStair):

	def svg2houseWindows(Xw,Yw,Zw,occupancyw):

		def svg2houseDoors(Xd,Yd,Zd,occupancyd):

	# backyard with green
	
			with open("lines/cortile.lines", "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				cortileList = []
				for row in csvReader :
					cortileList.append(POLYLINE([[float(row[0]),float(row[1])],[float(row[2]),float(row[3])]]))
			cortile = STRUCT(cortileList)
			xVal = 16/SIZE([1])(cortile)[0]
			yVal = 16/SIZE([2])(cortile)[0]
   	    		cortile = S([1,2])([xVal,yVal/2])(cortile)
   	    		cortile = T([1,2])([-6,-25])(cortile)
			
			prato = SOLIDIFY (cortile)
			prato = TEXTURE("texture/prato.jpg")(prato)
		
			cortile = OFFSET([.3,.3])(cortile)
			cortile = PROD([cortile,Q(.5)])
			cortile = TEXTURE("texture/muro.jpg")(cortile)
		
			#external walls with intDoors2floor					

			with open("lines/muriEsterni.lines", "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				extWallsList = []
				for row in csvReader :
					extWallsList.append(POLYLINE([[float(row[0]),float(row[1])],[float(row[2]),float(row[3])]]))
			extWalls = STRUCT(extWallsList)
			xVal = 16/SIZE([1])(extWalls)[0]
			yVal = 16/SIZE([2])(extWalls)[0]
			extWalls = S([1,2])([xVal,yVal])(extWalls)
			
			floor = SOLIDIFY (extWalls)
			floor= PROD([floor,Q(.07)])
			floor = TEXTURE("texture/parquet.jpg")(floor)
			secondFloor= T(3)(3.5)(floor)	


			extWalls = OFFSET([.3,.3])(extWalls)
			extlWallsH = PROD([extWalls,Q(3.5)])

			#create roof with hw9
			roof = workshop_09.createRoof("tetto")
			roof = T([1,2])([float(row[0]),float(row[1])])(roof)
			roof = S([1,2])([xVal,yVal])(roof)
			roof = TEXTURE("texture/tegole.jpg")(roof)	

			#internal walls 
			with open("lines/muriInterni.lines", "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				intWallsList = []
				for row in csvReader :
					intWallsList.append(POLYLINE([[float(row[0]),float(row[1])],[float(row[2]),float(row[3])]]))
			intWalls = STRUCT(intWallsList)
			intWalls = S([1,2])([xVal,yVal])(intWalls)
			intWalls = OFFSET([.2,.2])(intWalls)
			intWalls = PROD([intWalls,Q(3)])
				

			#windows 

			with open("lines/finestre.lines", "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				windowsHolesList = []
				windowsCompList = []
				cList = []
				cont = 0
				for row in csvReader:
					cont += 1
					cList.append([float(row[0])*xVal,float(row[1])*yVal])
					if cont <=2:
						if 	round(float(row[0]),1) == round(float(row[2]),1):
							yDifference = abs(float(row[3]) - float(row[1]))
						elif round(float(row[1]),1) == round(float(row[3]),1):
							xDifference = abs(float(row[2]) - float(row[0]))
					if cont == 4:
						windowsHolesList.append(MKPOL([cList,[[1,2,3,4]],None]))
						base = MKPOL([cList,[[1,2,3,4]],None])
						base = OFFSET([.1,.1])(base)
						base = PROD([base,Q(1.5)])
						cList = []
						cont = 0
						if xDifference < yDifference:
							window = workshop_07.window(Xw,Yw,Zw,occupancyw)(yDifference*yVal+.7,1,.6)
							window = R([1,2])(3*PI/2)(window)
							window = T([1,2,3])([float(row[0])*xVal+.7, float(row[1])*yVal,1])(window)
						else:
							window = workshop_07.window(Xw,Yw,Zw,occupancyw)(xDifference*xVal+.4,1,.6)
							window = T([1,2,3])([float(row[0])*xVal, float(row[1])*yVal-.2,1])(window)
					
						windowsCompList.append(window)

			windows = STRUCT(windowsHolesList)
			windows = OFFSET([0.05,0.05])(windows)
			windows = PROD([windows,Q(1.5)])
			windows = T(3)(1)(windows)
			windowsComp = STRUCT(windowsCompList)

			#windows 2nd floor
			#changed the svg file and its .lines so as to add windows on the second floor

			with open("lines/finestreSecondo.lines", "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				windows2FloorHolesList = []
				windows2FloorCompList = []
				cList = []
				cont = 0
				for row in csvReader:
					cont += 1
					cList.append([float(row[0])*xVal,float(row[1])*yVal])
					if cont <=2:
						if 	round(float(row[0]),1) == round(float(row[2]),1):
							yDifference = abs(float(row[3]) - float(row[1]))
						elif round(float(row[1]),1) == round(float(row[3]),1):
							xDifference = abs(float(row[2]) - float(row[0]))
					if cont == 4:
						windows2FloorHolesList.append(MKPOL([cList,[[1,2,3,4]],None]))
						base = MKPOL([cList,[[1,2,3,4]],None])
						base = OFFSET([.1,.1])(base)
						base = PROD([base,Q(1.5)])
						cList = []
						cont = 0
						if xDifference < yDifference:
							window2Floor = workshop_07.window(Xw,Yw,Zw,occupancyw)(yDifference*yVal+.7,1,.6)
							window2Floor = R([1,2])(3*PI/2)(window2Floor)
							window2Floor = T([1,2,3])([float(row[0])*xVal+.7, float(row[1])*yVal,1])(window2Floor)
						else:
							window2Floor = workshop_07.window(Xw,Yw,Zw,occupancyw)(xDifference*xVal+.4,1,.6)
							window2Floor = T([1,2,3])([float(row[0])*xVal, float(row[1])*yVal-.2,1])(window2Floor)
						
						windows2FloorCompList.append(window2Floor)	

			windows2Floor = STRUCT(windows2FloorHolesList)
			windows2Floor = OFFSET([0.05,0.05])(windows2Floor)
			windows2Floor = PROD([windows2Floor,Q(1.5)])
			windows2Floor = T(3)(1)(windows2Floor)
			windows2Comp = STRUCT(windows2FloorCompList)	

			#doors 

			with open("lines/porte.lines", "rb") as csvfile:		

				csvReader = csv.reader(csvfile,delimiter=",")
				intDoorsHolesList = []
				cList = []
				cont = 0
				xDoors = 0
				yDifference = 0
				intDoorsCompList = []
				for row in csvReader:
					cont += 1
					cList.append([float(row[0])*xVal,float(row[1])*yVal])
					if cont <=2:
						if 	round(float(row[0]),1) == round(float(row[2]),1):
							yDifference = abs(float(row[3]) - float(row[1]))
						
						elif round(float(row[1]),1) == round(float(row[3]),1):
							xDifference = abs(float(row[2]) - float(row[0]))	

					if cont == 4:
						intDoorsHolesList.append(MKPOL([cList,[[1,2,3,4]],None]))
						cList = []
						door = []
						cont = 0
						if xDifference < yDifference:
							door = workshop_07.door(Xd,Yd,Zd,occupancyd)(yDifference*yVal+.2,.7,1.1)
							door = T([2])([.4])(door)
							door = R([1,2])(3*PI/2)(door)
							door = T([1,2])([float(row[0])*xVal+.2,float(row[1])*yVal+.1])(door)
						else:
							door = workshop_07.door(Xd,Yd,Zd,occupancyd)(xDifference*xVal+.2,.7,1.1)
							door = T([1,2])([float(row[0])*xVal+.1,(float(row[1])*yVal)-.2])(door)
						intDoorsCompList.append(door)	

			intDoorsHoles = STRUCT(intDoorsHolesList)
			intDoorsHoles = OFFSET([.2,.15])(intDoorsHoles)
			intDoorsHoles = PROD([intDoorsHoles,Q(3)])
			intDoorsComp = STRUCT(intDoorsCompList)	

			#external doors

			with open("lines/porteEsterne.lines","rb") as csvfile:
				csvReader = csv.reader(csvfile, delimiter=",")
				extDoorsHolesList = []
				cList = []
				cont = 0
				xDifference = 0
				yDifference = 0
				extDoorsCompList = []
				for row in csvReader:
					cont += 1
					cList.append([float(row[0]) * xVal, float(row[1]) * yVal])
					if cont <= 2:
						if round(float(row[0]), 1) == round(float(row[2]), 1):
							yDifference = abs(float(row[3]) - float(row[1]))
						elif round(float(row[1]), 1) == round(float(row[3]), 1):
							xDifference = abs(float(row[2]) - float(row[0]))
					if cont == 4:
						extDoorsHolesList.append(MKPOL([cList, [[1, 2, 3, 4]], None]))
						cList = []
						door = []
						cont = 0
						if xDifference < yDifference:
							door = workshop_07.door(Xd,Yd,Zd ,occupancyd)(yDifference * yVal+.2, 2.8,1.2)
							door = R([1, 2])(PI/2)(door)
							door = T([1, 2])([float(row[0]) * xVal+.25, (float(row[1]) * yVal)-2.3])(door)
						else:
							door = workshop_07.door(Xd,Yd,Zd ,occupancyd)(xDifference * xVal, 2.5,1.2)
							door = T([1, 2])([float(row[0]) * xVal, float(row[1]) * yVal])(door)
						extDoorsCompList.append(door)
				
			extDoorsHoles = STRUCT(extDoorsHolesList)
			extDoorsHoles = OFFSET([0,.15])(extDoorsHoles)
			extDoorsHoles = PROD([extDoorsHoles,Q(2.5)])
			extDoorsComp = STRUCT(extDoorsCompList)	
			
			#doors 2nd floor

			with open("lines/porteSecondo.lines", "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				intDoors2HolesList = []
				cList = []
				cont = 0
				yDifference = 0
				intDoorsSecondCompList = []
				for row in csvReader:
					cont += 1
					cList.append([float(row[0])*xVal,float(row[1])*yVal])
					if cont <=2:
						if 	round(float(row[0]),1) == round(float(row[2]),1):
							yDifference = abs(float(row[3]) - float(row[1]))
					
						elif round(float(row[1]),1) == round(float(row[3]),1):
							xDifference = abs(float(row[2]) - float(row[0]))

					if cont == 4:
						intDoors2HolesList.append(MKPOL([cList,[[1,2,3,4]],None]))
						cList = []
						door2Floor = []
						cont = 0
						if xDifference < yDifference:
							door2Floor = workshop_07.door(Xd,Yd,Zd,occupancyd)(yDifference*yVal+.2,.7,1)
							door2Floor = T([2])([.4])(door2Floor)
							door2Floor = R([1,2])(3*PI/2)(door2Floor)
							door2Floor = T([1,2])([float(row[0])*xVal+.2,float(row[1])*yVal+.1])(door2Floor)
						else:
							door2Floor = workshop_07.door(Xd,Yd,Zd,occupancyd)(xDifference*xVal+.2,.7,1)
							door2Floor = T([1,2])([float(row[0])*xVal+.1,(float(row[1])*yVal)-.2])(door2Floor)
						intDoorsSecondCompList.append(door2Floor)	

			intDoorsSecondHoles = STRUCT(intDoors2HolesList)
			intDoorsSecondHoles = OFFSET([.2,.15])(intDoorsSecondHoles)
			intDoorsSecondHoles = PROD([intDoorsSecondHoles,Q(3)])
			intDoorsSecondComp = STRUCT(intDoorsSecondCompList)	

			#spiral staircase
			#I modified the HW3 to create a spiral parametric scale put in the house

			with open("lines/holeStair.lines", "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				stairList = []
				for row in csvReader :
					stairList.append(POLYLINE([[float(row[0]),float(row[1])],[float(row[2]),float(row[3])]]))
			stair = STRUCT(stairList)
			xVal = 2/SIZE([1])(stair)[0]
			yVal = 2/SIZE([2])(stair)[0]
			stair = S([1,2])([xVal,yVal])(stair)
			scala = workshop_03.createLadder(4.,.20,.04)
			scala = T([1,2])([9,6])(scala)
			hole = SOLIDIFY (stair)
			hole = PROD([hole,Q(.1)])
			hole = T([1,2,3])([-.5,1,3.5])(hole)
			
			#final assembly	

			extWalls = DIFFERENCE([extlWallsH,windows])
			extWalls = DIFFERENCE([extWalls,extDoorsHoles])
			extWalls = TEXTURE("texture/muro.jpg")(extWalls)
			extWalls = STRUCT([extWalls,windowsComp])
			extWalls = STRUCT([extWalls, extDoorsComp])

			extWallsSecondFloor = DIFFERENCE([extlWallsH,windows])
			extWallsSecondFloor = TEXTURE("texture/muro.jpg")(extWallsSecondFloor)
			extWallsSecondFloor = STRUCT([extWallsSecondFloor,windows2Comp])

			intWalls = DIFFERENCE([intWalls,intDoorsHoles])
			intWalls = TEXTURE("texture/workshop_10_texture_muro_interno.jpg")(intWalls)
			intWallsSecondFloor = STRUCT([intWalls,intDoorsSecondComp])
			intWalls = STRUCT([intWalls,intDoorsComp])

			walls = STRUCT([intWalls,extWalls])
			wallsSecondFloor = STRUCT([intWallsSecondFloor,extWallsSecondFloor])

			roofHole= DIFFERENCE([secondFloor,hole])
			roofHole = TEXTURE("texture/parquet.jpg")(roofHole)
			house = STRUCT([walls,floor,prato,cortile,roofHole,scala])

			houseSecondFloor = STRUCT([wallsSecondFloor,wallsSecondFloor])
			houseFinished = STRUCT([house,T(3)(3.5)(houseSecondFloor)])

			#VIEW(houseFinished) #house without roof

			finishedHouseRoof = STRUCT([houseFinished,T(3)(7),roof])

			return finishedHouseRoof

		return svg2houseDoors

	return svg2houseWindows

def main():
	#VIEW(svg2house())

	if __name__ == '__main__':
		main()
