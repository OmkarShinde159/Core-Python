print("Pattern 1")
'''
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * *
'''
c=1
i=6
while c<=i:
    spc=1
    while spc<=i-c:
        print(" ",end=" ")
        spc+=1
    k=1
    while k<=c:
        print("*",end=" ")
        k+=1
        
    print()
    c+=1

print("Pattern 2")
'''
          1 
        2 2 
      3 3 3 
    4 4 4 4 
  5 5 5 5 5 
6 6 6 6 6 6
'''

c=1
n=6
while c<=n:
    spc=1
    while spc<=n-c:
        print(" ",end=" ")
        spc+=1

    row=1
    while row<=c:
        print(c,end=" ")
        row+=1
        
    print()
    c+=1

print("Pattern 3")
'''
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
1 2 3 4 5 6

'''

c=1
n=6
while c<=n:
    spc=1
    while spc<=n-c:
        print(" ",end=" ")
        spc+=1

    row=1
    while row<=c:
        print(row,end=" ")
        row+=1
        
    print()
    c+=1

print("Pattern 4")
'''
          6 
        5 5 
      4 4 4 
    3 3 3 3 
  2 2 2 2 2 
1 1 1 1 1 1
'''

c=1
r=6
n=6
while c<=n:
    spc=1
    while spc<=n-c:
        print(" ",end=" ")
        spc+=1

    row=1
   
    while row<=c:
        print(r,end=" ")
        row+=1
        

    print()
    c+=1
    r-=1

print("Pattern 5")
'''
          6 
        6 5 
      6 5 4 
    6 5 4 3 
  6 5 4 3 2 
6 5 4 3 2 1
'''

c=1
n=6
while c<=n:
    spc=1
    while spc<=(n-c):
        print(" ",end=" ")
        spc+=1

    row=1
    r=6
    while row<=c:
        print(r,end=" ")
        row+=1
        r-=1

    print()
    c+=1


    



















