# WAP to find the smallest number among 3 numbers

a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))
c = int(input("Enter Number C: "))

if a < b:
    if a < c:
        print("A is the smallest Number")
    else:
        print("C is the smallest Number")
else:
    if b < c:
        print("B is the smallest Number")
    else:
        print("C is the smallest Number")
