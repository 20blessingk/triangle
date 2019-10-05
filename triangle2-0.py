#definitely NOT made by Kyle but its pretty helpful 
def cong_sas(s1, s2, a1, a2):  
       
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2] 
    a1 = [float(i) for i in a1] 
    a2 = [float(i) for i in a2] 
       
    s1.sort() 
    s2.sort() 
    a1.sort() 
    a2.sort() 
       
    # Check for SAS 
       
    # angle b / w two smallest sides is largest. 
    if s1[0] == s2[0] and s1[1] == s2[1]: 
           
        # since we take angle b / w the sides. 
        if a1[2] == a2[2]:          
            return 1
               
    if s1[1] == s2[1] and s1[2] == s2[2]: 
        if a1[0] == a2[0]: 
            return 1
               
    if s1[2] == s2[2] and s1[0] == s2[0]: 
        if a1[1] == a2[1]: 
            return 1
       
    return 0
      
# Function for ASA congruency 
def cong_asa(s1, s2, a1, a2):  
       
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2] 
    a1 = [float(i) for i in a1] 
    a2 = [float(i) for i in a2] 
       
    s1.sort() 
    s2.sort() 
    a1.sort() 
    a2.sort() 
       
    # Check for ASA 
       
    # side b / w two smallest angle is largest. 
    if a1[0] == a2[0] and a1[1] == a2[1]: 
           
        # since we take side b / w the angle. 
        if s1[2] == s2[2]:          
            return 1
               
    if a1[1] == a2[1] and a1[2] == a2[2]: 
        if s1[0] == s2[0]: 
            return 1
               
    if a1[2] == a2[2] and a1[0] == a2[0]: 
        if s1[1] == s2[1]: 
            return 1
       
    return 0
      
# Function for AAS congruency 
def cong_aas(s1, s2, a1, a2):  
       
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2] 
    a1 = [float(i) for i in a1] 
    a2 = [float(i) for i in a2] 
       
    s1.sort() 
    s2.sort() 
    a1.sort() 
    a2.sort() 
       
    # Check for AAS 
       
    # side other two smallest angle is smallest or 2nd smallest. 
    if a1[0] == a2[0] and a1[1] == a2[1]: 
           
        # since we take side other than angles. 
        if s1[0] == s2[0] or s1[1] == s2[1]:          
            return 1
               
    if a1[1] == a2[1] and a1[2] == a2[2]: 
        if s1[1] == s2[1] or s1[2] == s2[2]: 
            return 1
               
    if a1[2] == a2[2] and a1[0] == a2[0]: 
        if s1[0] == s2[0] or s1[2] == s2[2]: 
            return 1
       
    return 0
   
# Function for HL congruency 
def cong_hl(s1, s2):  
       
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2]  
    s1.sort() 
    s2.sort()  
       
    # Check for HL 
    if s1[2] == s2[2]: 
        if s1[1] == s2[1] or s1[0] == s2[0]: 
            return 1
       
    return 0
      
# Function for SSS congruency 
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
s1 = [3, 4, 5] 
s2 = [4, 3, 5] 
           
a1 = [90, 60, 30] 
a2 = [60, 30, 90] 
   
# function call for SSS congruency 
sss = cong_sss(s1, s2)  
   
# function call for SAS congruency  
sas = cong_sas(s1, s2, a1, a2)  
  
# function call for ASA congruency  
asa = cong_asa(s1, s2, a1, a2)  
   
# function call for AAS congruency 
aas = cong_aas(s1, s2, a1, a2) 
  
# function call for HL congruency 
hl = cong_hl(s1, s2, )  
   
# Check if triangles are congruent or not  
if sss or sas or asa or aas or hl :  
    print("Triangles are congruent by ")
    if sss: print("SSS")
    if sas: print("SAS") 
    if asa: print("ASA")
    if aas: print("AAS")
    if hl: print("HL") 
else: print ("Triangles are not congruent")