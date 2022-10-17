
t = int(input("Enter the table number to print: "))
for i in range(1,11):
    print(t,"*",i,"=",t*i)


# find factorial
n = int(input("Enter num to find factorial:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is:",fact)

# factorial with conditions
n = int(input("Enter num to find factorial:"))
if n==0:
    print("Cannot find factorial of",n)
elif n<0:
    print("Enter a positive number")
elif n>0 and n<11:
    fact = 1
    for i in range(n,0,-1):
        fact=fact*i
    print("Factorial of",n,"is:",fact)
else:
    print("Number is Out of range 1-10")
