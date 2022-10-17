
for i in range(6,0,-1):
    for j in range(0,i):
        print(" *", end=" ")
    print()


for i in range (0,6):
    for j in range(6,i+1,-1):
        print("  ", end="  ")
    for k in range(0,i+1):
        print(" *", end=" ")    
    print()


for i in range(0,6):
    for j in range(0,i):
        print("   ", end=" ")
    for k in range(6,i,-1):
        print(" *" , end=" ")     
    print()


for i in range (1,7):
    for j in range (0,i):
        print("*   ", end=" ")
    print()
for k in range (1,6):
    for l in range (6,k,-1):
        print("*   ", end=" ")
    print()


for i in range (0,6):
    for j in range (6,i+1,-1):
        print(" ",end=" ")
    for k in range (0,i+1):
        print("* ", end=" ")
    print()
for a in range (0,5):
    for b in range (0,a+1):
        print(" ",end=" ")
    for c in range (5,a,-1):
        print("* ", end=" ")
    print()


r = int(input("No of rows: "))
for i in range (0,r):
    for s in range (r,i+1,-1):
        print("  ", end=" ")
    for j in range (0,i+1):
        print("*", end=" ")
    for k in range (0,i):
        print("*", end=" ")
    print()
for l in range (0,r-1):
    for sp in range(0,l+1):
        print("  ", end=" ")
    for m in range (r-1,l,-1):
        print("*", end=" ")
    for n in range (r-1,l+1,-1):
        print("*", end=" ")
    print()

r = int(input("No of rows: "))
for i in range (0,r):
    for s in range (r,i+1,-1):
        print(" ", end=" ")
    for j in range (0,i+1,1):
        print("* ", end="  ")
    print() 

for l in range (0,r-1):
    for sp in range(0,l+1):
        print(" ", end=" ")
    for m in range (r-1,l,-1):
        print("* ", end="  ")
    print()


r = int(input("No of rows: "))
for i in range(0,r):
    for j in range(0,i):
        print("   ", end=" ")
    for k in range(r,i,-1):
        print(" *" , end=" ")     
    print()




















