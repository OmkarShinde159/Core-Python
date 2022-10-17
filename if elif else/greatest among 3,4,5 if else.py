# WAP to find the greatest number among 4 numbers

a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))
c = int(input("Enter Number C: "))
d = int(input("Enter Number D: "))

if a>b:
    if a>c: 
        if a>d:
            print("A is greatest Number")
        else:
            print("D is greatest Number")
    else:
        if c>d:
            print("C is greatest number")
        else:
            print("D is greatest number")

else:
    if b>c:
        if b>d:
            print("C is greatest number")
        else:
            print("D is greatest number")
    else:
        if c>d:
            print("C is greatest number")
        else:
            print("D is greatest number")

#------------------------------------------------------------------------------


# WAP to find the largest number among 3 numbers

a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))
c = int(input("Enter Number C: "))

if a > b:
    if a > c:
        print("A is the greatest Number")
    else:
        print( C is the greatest Number")
else:
    if b > c:
        print("B is the greatest Number")
    else:
        print("C is the greatest Number")

#-------------------------------------------------------------------------------

# wap to find largest amont 5
a = input()
b = input()
c = input()
d = input()
e = input()

if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("A is max")
            else:
                print("E is max")
        else:
            if d>e:
                print("D is max")
            else:
                print("E is max")
    else:
        if c>d:
            if c>e:
                print("C is max")
            else:
                print("E is max")
        else:
            if d>e:
                print("D is max")
            else:
                print("E is max")
                
                
else:
    if b>c:
        if b>d:
            if b>e:
                print("B is max")
            else:
                print("E is max")
        else:
            if d>e:
                print("D is max")
            else:
                print("E is max")
    else:
        if c>d:
            if c>e:
                print("C is max")
            else:
                print("E is max")
        else:
            if d>e:
                print("D is max")
            else:
                print("E is max")
