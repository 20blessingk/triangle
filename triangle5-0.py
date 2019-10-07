#made by Kyle Blessing
import random

choices = ["XYZ","XZY","YXZ","YZX","ZYX","ZXY"]

def angle(angle1,angle2):
    return ("Angle " + str(angle1) + " = Angle " + str(angle2))
def seg(side1,side2, side3,side4):
    return (side1 + side2 + " = " + side3 + side4)

def triangle():
    a,b,c = "A","B","C"
    x,y,z = "X","Y","Z"
    val = random.choice(choices)
    if val == choices[0]:
        a1 = angle(a,x)
        b1 = angle(b,y)
        c1 = angle(c,z)
        x1 = seg(a,b,x,y)
        y1 = seg(a,c,x,z)
        z1 = seg(b,c,y,z)
        list1 = [a1,b1,c1,x1,y1,z1]
        opt1 = random.sample(list1,6)
        print(*opt1, sep = "\n" )
        return "XYZ"
    if val == choices[1]:
        a2 = angle(a,x)
        b2 = angle(b,z)
        c2 = angle(c,y)
        x2 = seg(a,b,x,z)
        y2 = seg(a,c,x,y)
        z2 = seg(b,c,z,y)
        list2 = [a2,b2,c2,x2,y2,z2]
        opt2 = random.sample(list2,6)
        print(*opt2, sep = "\n" )
        return "XZY"
    if val == choices[2]:
        a3 = angle(a,y)
        b3 = angle(b,x)
        c3 = angle(c,z)
        x3 = seg(a,b,y,x)
        y3 = seg(a,c,y,z)
        z3 = seg(b,c,x,z)
        list3 = [a3,b3,c3,x3,y3,z3]
        opt3 = random.sample(list3,6)
        print(*opt3, sep = "\n" )
        return "YXZ"
    if val == choices[3]:
        a4 = angle(a,y)
        b4 = angle(b,z)
        c4 = angle(c,x)
        x4 = seg(a,b,y,z)
        y4 = seg(a,c,y,x)
        z4 = seg(b,c,z,x)
        list4 = [a4,b4,c4,x4,y4,z4]
        opt4 = random.sample(list4,6)
        print(*opt4, sep = "\n" )
        return "YZX"
    if val == choices[4]:
        a5 = angle(a,z)
        b5 = angle(b,y)
        c5 = angle(c,x)
        x5 = seg(a,b,z,y)
        y5 = seg(a,c,z,x)
        z5 = seg(b,c,y,x)
        list5 = [a5,b5,c5,x5,y5,z5]
        opt5 = random.sample(list5,6)
        print(*opt5, sep = "\n" )
        return "ZYX"
    if val == choices[5]:
        a6 = angle(a,z)
        b6 = angle(b,x)
        c6 = angle(c,y)
        x6 = seg(a,b,z,x)
        y6 = seg(a,c,z,y)
        z6 = seg(b,c,x,y)
        list6 = [a6,b6,c6,x6,y6,z6]
        opt6 = random.sample(list6,6)
        print(*opt6, sep = "\n" )
        return "ZXY"

def end():

    play = True
    while play:
        act = triangle()
        ans = input("Triangle ABC is congruent to Triangle > ")
        if ans == act:
            print("Correct") 
        else:
            print(f"Wrong, the answer is triangle {act}.")

        again = input("Try again? (y/n) > ")
        if again.lower() in "yes":
            continue
        else:
            play = False
            exit(0)

if __name__ == "__main__":
    end()
