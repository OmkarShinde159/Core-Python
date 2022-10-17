'''
# find factorial -------------------------------------------

fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
while num >= 1:# 5 4 3 2 1 false
    fact = fact * num
    num -= 1
print("Factorial is : ",fact)

num1 = int(input("Enter Number to find its factorial: "))
fact = 1
i = 1
while i <= num1:
    fact = fact * i
    i += 1
print("Factorial is: ",fact)


fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
if num <= 0:
    print("cant find factorial, enter number greater than 0")
else:
    while num >= 1:# 5 4 3 2 1 false
        fact = fact * num
        num -= 1
    print("Factorial is : ",fact)



fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
if num > 0:
    while num >= 1:# 5 4 3 2 1 false
        fact = fact * num
        num -= 1
    print("Factorial is : ",fact) 
else:  
    print("cant find factorial, enter number greater than 0")

