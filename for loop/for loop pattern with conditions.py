'''
accepte rows upto 50
if user entered wrong value
ask him to enter correct value again
'''
'''
while True:
    r = int(input("No of rows: "))
    if r<=50 and r>=1:
        for i in range(0,r):
            for j in range(0,i+1):
                print("*", end=" ")
            print()
        break         
    else:
        print("Enter value between 1-50")
print("Thanks for using")


while True:
    pass

if True:
    pass
'''
n = int(input("user input:"))
for row in range (1,n+1):
    for col in range(1,n+1):
        if row==1 or row==n or col==1 or col==n:
            print("* ", end="")
        else:
            print("   ", end="")
    print()
            

