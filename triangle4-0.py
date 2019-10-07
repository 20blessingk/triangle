#made by Kyle Blessing
import random

choices = ["XYZ","XZY","YXZ","YZX","ZYX","ZXY"]

def angle(angle1,angle2):
    print("Angle " + str(angle1) + " = Angle " + str(angle2))
def seg(side1,side2, side3,side4):
    print(side1 + side2 + " = " + side3 + side4)

def triangle():
    a,b,c = "A","B","C"
    x,y,z = "X","Y","Z"
    val = random.choice(choices)
    if val == choices[0]:
        angle(a,x)
        angle(b,y)
        angle(c,z)
        seg(a,b,x,y)
        seg(a,c,x,z)
        seg(b,c,y,z)
        return "XYZ"
    if val == choices[1]:
        angle(a,x)
        angle(b,z)
        angle(c,y)
        seg(a,b,x,z)
        seg(a,c,x,y)
        seg(b,c,z,y)
        return "XZY"
    if val == choices[2]:
        angle(a,y)
        angle(b,x)
        angle(c,z)
        seg(a,b,y,x)
        seg(a,c,y,z)
        seg(b,c,x,z)
        return "YXZ"
    if val == choices[3]:
        angle(a,y)
        angle(b,z)
        angle(c,x)
        seg(a,b,y,z)
        seg(a,c,y,x)
        seg(b,c,z,x)
        return "YZX"
    if val == choices[4]:
        angle(a,z)
        angle(b,y)
        angle(c,x)
        seg(a,b,z,y)
        seg(a,c,z,x)
        seg(b,c,y,x)
        return "ZYX"
    if val == choices[5]:
        angle(a,z)
        angle(b,x)
        angle(c,y)
        seg(a,b,z,x)
        seg(a,c,z,y)
        seg(b,c,x,y)
        return "ZXY"

triangle = triangle()

ans = input("Triangle ABC is congruent to Triangle > ")
if ans == triangle:
    print("Correct") #--------------------------------------something is wrong here
else:
    print(f"Wrong, the answer is triangle {triangle}.")
