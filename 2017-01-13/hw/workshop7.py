from pyplasm import *

glassColor = Color4f([.57,.85,.84])


def door(X,Y,Z,occupancy):
    section1 = PROD([QUOTE([0]),QUOTE([0])])
    section2= PROD([QUOTE([0]),QUOTE([0])])
    
    for iz in range(0,len(Z)):
        
        for ix in range(0,len(X)):
            if occupancy[iz][ix] == 0:
                if X[ix] > 0:
                    X[ix] = -(X[ix])
            elif occupancy[iz][ix] == 1:
                    if X[ix] < 0:
                        X[ix] = -(X[ix])
        #Creo le strutture
        x = QUOTE(X)
        z = QUOTE([Z[iz]])

        #Creo un livello della struttura
        level1 = PROD([x,z])

        #Creo un livello della struttura vuota
        j=0
        for k in range(0,iz):
            j = j+Z[k]
        section1 = STRUCT([section1,T(2)(j),level1])
        
        pos = 0
        for i in range(0,len(X)):
            X[i] = -(X[i])
            if X[i]>0:
                pos = pos+1
                
        if pos>0:
            level2X = QUOTE(X)
            level2 = PROD([level2X,z])
            section2 = STRUCT([section2,T(2)(j),level2])
            

    #aggiungo spessori
    section1 = PROD([section1,QUOTE([Y[0]])])
    section2 = PROD([section2,QUOTE([Y[1]])])
    
    #Trasla e ruota le strutture sul giusto piano
    section1 = STRUCT([R([2,3])(PI/2),section1])
    section2= STRUCT([T(2)(-Y[0]/5),R([2,3])(PI/2),section2])
    
    #coloro
    section2 = TEXTURE(["texture/rosa.jpg"])(section2)
    section1 =  TEXTURE(["texture/wood.jpg"])(section1)

    part1 = T(3)(.15)(CUBOID([.05,.02,.05]))
    part2 = CUBOID([.05,.02,.05])
    part3 = CUBOID([.03,.01,0.2])
    #handler = TEXTURE("texture/metal.jpg")(STRUCT([part1, part2, part3]))
    #handler = T([1,2,3])([dx/3,-.12,.9])(handler)

    
    #Metto insieme gli elementi
    section12 = STRUCT([section1,section2])
    
    def door(dx,dy,dz):
        resizeStructure = STRUCT([S([1,2,3])([dx,dy,dz]),section12])
        return resizeStructure
    
    #Ritorno l'output
    return door

from pyplasm import *

glassColor = Color4f([.57,.85,.84])

def window(X,Y,Z,occupancy):
    fullSection = PROD([QUOTE([0]),QUOTE([0])])
    emptySection = PROD([QUOTE([0]),QUOTE([0])])
    
    for iz in range(0,len(Z)):
        
        for ix in range(0,len(X)):
            if occupancy[iz][ix] == 0:
                if X[ix] > 0:
                    X[ix] = -(X[ix])
            elif occupancy[iz][ix] == 1:
                    if X[ix] < 0:
                        X[ix] = -(X[ix])
        #Creo le strutture
        x = QUOTE(X)
        z = QUOTE([Z[iz]])

        #Creo un livello della struttura
        level = PROD([x,z])

        #Creo un livello della struttura vuota
        j=0
        for k in range(0,iz):
            j = j+Z[k]
        fullSection = STRUCT([fullSection,T(2)(j),level])
        
        pos = 0
        for i in range(0,len(X)):
            X[i] = -(X[i])
            if X[i]>0:
                pos = pos+1
                
        if pos>0:
            emptyX = QUOTE(X)
            emptyLevel = PROD([emptyX,z])
            emptySection = STRUCT([emptySection,T(2)(j),emptyLevel])
            

    #aggiungo spessori
    fullSection = PROD([fullSection,QUOTE([Y[0]])])
    emptySection = PROD([emptySection,QUOTE([Y[1]])])
    
    #Trasla e ruota le strutture sul giusto piano
    fullSection = STRUCT([R([2,3])(PI/2),fullSection])
    emptySection = STRUCT([T(2)(-Y[0]/2),R([2,3])(PI/2),emptySection])
    
    #coloro
    emptySection = TEXTURE(["texture/glass.jpg"])(emptySection)
    fullSection = TEXTURE(["texture/white.jpg"])(fullSection)

    fullEmpty = STRUCT([fullSection,emptySection])
    
    def window(dx,dy,dz):
        scaledStructure = STRUCT([S([1,2,3])([dx,dy,dz]),fullEmpty])
        return scaledStructure
    
    #Ritorno l'output
    return window
