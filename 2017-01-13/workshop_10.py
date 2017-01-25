
from larlib import *

from hw import workshop8

def MultistoreyHouse():

	extWalls = "lines/muriEsterni.lines"
	intWalls = "lines/muriInterni.lines"
	windows = "lines/finestre.lines"
	intDoors = "lines/porte.lines"
	intDoors2floor = "lines/porteSecondo.lines"
	extDoors = "lines/porteEsterne.lines"
	cortile = "lines/cortile.lines"
	windows2floor = "lines/finestreSecondo.lines"
	holeStair = "lines/holeStair.lines"

	#window parameters
	#I changed the hw7 changing measures and style
	Xw = [.15,.03,.02,.39,.02,.03,.15]
	Yw = [.3,.1]
	Zw = [.15,.3,1.62,.3,.15]
	occupancyw = [[1,1,1,1,1,1,1],
				[1,0,1,0,1,0,1],			
				[1,0,1,0,1,0,1],
				[1,0,1,0,1,0,1],
				[1,1,1,1,1,1,1]]

	#door parameters
	#I changed the hw7 changing measures and style
	Xd = [.08,.001,.15,.2,.15,.2,.15,.08]
	Yd = [.15,.1]
	Zd = [.2,.2,.02,.40,.02,.15,.15,.02,.4,.02,.15,.25,.02,.2,.02,.1]
	occupancyd = [[0,0,1,1,1,1,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,1,1,1,1,0],
        	    [0,1,1,1,1,1,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,1,1,1,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,0,1,0,1,0],
        	    [0,1,1,1,1,1,1,0],
        	    [0,1,1,1,1,1,1,0],
        	    [0,1,0,0,0,0,0,0]]

	VIEW(workshop8.svg2house(extWalls,intWalls,windows,intDoors,extDoors,
							intDoors2floor,windows2floor,cortile,holeStair)(Xw,Yw,Zw,occupancyw)(Xd,Yd,Zd,occupancyd))

def main():
	MultistoreyHouse()

if __name__ == '__main__':
	main()