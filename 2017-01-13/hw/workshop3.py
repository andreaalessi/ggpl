
from pyplasm import *
import math 

def circle(r):
    def c(p):
        return [r*COS(p[0]),r*SIN(p[0])]
    return c

def createStep(stepL,stepW,r):
    min,max = stepW
    diff = (max-min)/2.
    stepPartial = POLYLINE([[0,0],[0,min],[stepL, min+diff],[stepL,-diff]])
    stepPartial = JOIN(stepPartial)
    rB = JOIN(MAP(circle(max/2.))(INTERVALS(PI)(32)))
    rB = R([1,2])(-PI/2)(rB)
    rB = S(1)(.3)(rB)
    rB = T([1,2])([stepL,min/2.])(rB)
    rS = JOIN(MAP(circle(min))(INTERVALS(PI)(32)))
    rS = R([1,2])(-PI/2)(rS)
    rS = T([2])([min/2.])(rS)
    stepPartial = DIFFERENCE([stepPartial, rS])
    step = STRUCT([rB, stepPartial])
    step = PROD([step, Q(r)])
    step = T([2])([-min/2.])(step)
    rPole = CYLINDER([min+(min*0.2),r])(20)
    return STRUCT([step,rPole])

def createLadder(h,interStep,r):
    stepNumber = math.ceil(h/(interStep+r))
    step = TEXTURE("texture/redWood.jpg")(createStep(.8,[.03,.5],.04))
    rail = createRail(.5,.8)
    Rx = R([1,2])(-2*PI/11)
    Ry = T([3])([interStep+r])
    ladder = [step,rail,Rx,Ry]*int(stepNumber)
    p = TEXTURE("texture/redWood.jpg")(CYLINDER([.03,stepNumber*(r+interStep)-interStep])(20))
    ladder = [p] + ladder
    return STRUCT(ladder)

def createRail(l,stepL):
    rail = CYLINDER([0.04,l+l*0.075])(30)
    rail = R([1,2])(PI/2)(rail)
    rail = R([2,3])(PI/2-SIN(l))(rail)
    rail = T([1,2,3])([stepL,l/2.,.7+.05])(rail)
    rail = TEXTURE("texture/redWood.jpg")(rail)
    part1 = CYLINDER([0.02,.7+.05+TAN(SIN(l))*l/4.])(30)
    part1 = T([1,2,3])([stepL,l/2-l/4.,0.01])(part1)
    part1 = TEXTURE("texture/steel.jpg")(part1)
    part2 = CYLINDER([0.02,.7+.05+TAN(SIN(l))*2*l/4.])(30)
    part2 = TEXTURE("texture/steel.jpg")(part2)
    part2 = T([1,2,3])([stepL,l/2-2*l/4.,0.01])(part2)
    part3 = CYLINDER([0.02,.7+.05+TAN(SIN(l))*3*l/4.])(30)
    part3 = TEXTURE("texture/steel.jpg")(part3)
    part3 = T([1,2,3])([stepL,l/2-3*l/4.,0.01])(part3)
    return STRUCT([rail, part1, part2, part3])

#VIEW(createLadder(3,.3,5))