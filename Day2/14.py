#from math import *  -- it is bad practice, use it for small class (modules)
from math import factorial # good way to do it - import what is requored
import math


g1=90
g2=400

def abc():
    loca1=32
    loca2=34
    print(locals())
    print(globals())

abc()
