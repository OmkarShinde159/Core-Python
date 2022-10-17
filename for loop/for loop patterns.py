

print("----Pattern 1----")
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

print("----Pattern 2-----")
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
    
print("----Pattern 3----")
for i in range(1,6):
    for j in range(1,1+i):
        print(j,end=" ")
    print()

print("----Pattern 4----")
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

print("----Pattern 5----")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("----Pattern 6----")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

print("----Pattern 7----")
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()

print("----Pattern 8----")
for i in range(5,0,-1): #5 4 3 2 1    
    for j in range(i,0,-1): #i=5 i=4 i=3 i=2 i=1
        print(j, end=" ")
    print()


for i in range(1,9):
    for j in range(1,9):
        print("*",end=" ")
    print()


n = int(input("Pattern: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

n = int(input("Pattern: "))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()


n = int(input("Pattern: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()


n = int(input("Pattern: "))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()





















