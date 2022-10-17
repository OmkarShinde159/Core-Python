# WAP to create range function

def range1(sv,ev,stp):
    if stp > 0:
        if sv < ev:
            while sv < ev:
                print(sv)
                sv += stp
        else:
            print(None)
            
    elif stp < 0:
        if sv > ev:
            while ev < sv:
                print(sv)
                sv  += stp
        else:
            print(None)
    else:
        print(None)
'''            
range1(1,5,1)
print("-----")

range1(0,8,2)
print("-----")

range1(5,1,-1)
print("-----")

range1(10,1,-3)
print("-----")

range1(2,1,1)
range1(1,2,-1)
range1(-1,-5,-1)
range1(-1,-5,-1)
'''
range1(-3,1,0)



# WAP which accepts the user first name and last name
#and print them in reverse order with space between them

def revName(fname,lname):
    print(lname,fname)

revName("Omkar","Shinde")

def revName1(fname,lname):
    return lname+" "+fname

print(revName("Omkar","Shinde"))

# WAP to define a function that accepts length and breadth and returns area of rectangle

def rectArea(length, breadth):
    Area = length * breadth
    return Area

print( "Area of rectangle is: ",rectArea(8,5))
# print(rectArea(8,5))


# WAP to define a function that accepts roll number and returns whether student is present or absent

def isPresent(rollNo):
    stu_Present = [1,2,3,5,6,7,9,10]
    stu_Absent = [4,8]

    if rollNo in stu_Present:
        return "Present"
    elif rollNo in stu_Absent:
        return "Absent"
    else:
        return "Invalid Roll Number"

print(isPresent(10))
print(isPresent(6))
print(isPresent(4))
print(isPresent(15))

















