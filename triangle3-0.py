# Function for SSS congruency 
import random

def angle(angle1,angle2):
    print("Angle " + str(angle1) + " = Angle " + str(angle2))
def seg(side1,side2, side3,side4):
    print(side1 + side2 + " = " + side3 + side4)

def cong_sss(s1, s2):  
       
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2]  
    s1.sort() 
    s2.sort()  
       
    # Check for SSS 
    if(s1[0] == s2[0] and s1[1] == s2[1] and s1[2] == s2[2]): 
        return 1   
    return 0
   
# Driver Code  

abc = [3,4,5]
xyz = [4,5,3]
ABC = ["A","B","C"]
XYZ = ["X","Y","Z"]

s1 = random.sample(abc,3)
s2 = random.sample(xyz,3)

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

# function call for SSS congruency 
sss = cong_sss(s1, s2)  
   
# Check if triangles are congruent or not  
if sss:  
    print("Correct!")
else: 
    print ("Wrong. The answer was ")