#Made by Kyle Blessing
### TRIANGLE CONGRUITY CHECKER ###
import random
#from graphics import *

ABC = ["A","B","C"]
XYZ = ["X","Y","Z"]

def angle(angle1,angle2):
    print("Angle " + str(angle1) + " = Angle " + str(angle2))
def seg(side1,side2, side3,side4):
    print(side1 + side2 + " = " + side3 + side4)

def triangle():
    a,b,c = random.sample(ABC,3)
    x,y,z = random.sample(XYZ,3)

    a1,b1,c1 = random.sample(ABC,3)
    x1,y1,z1 = random.sample(XYZ,3)

    angle(a,x)
    angle(b,y)
    angle(c,z)

    seg(a1,b1,x1,y1)
    seg(a1,c1,x1,z1)
    seg(b1,c1,y1,z1) 

#a1 does not always mean a1 = A -----------------------fix this
#need to return the value

    if a1 == x1 and b1 == y1:
        return "XYZ"
    if a1 == x1 and b1 == z1:
        return "XZY"
    if a1 == y1 and b1 == x1:
        return "YXZ"
    if a1 == y1 and b1 == z1:
        return "YZX"
    if a1 == z1 and b1 == y1:
        return "ZYX"
    if a1 == z1 and b1 == x1:
        return "ZXY"

triangle()
ans = input("Triangle ABC is congruent to Triangle > ")
if ans == "XYZ":
    print("Correct") #--------------------------------------something is wrong here
else:
    print("Wrong, the answer is ")




