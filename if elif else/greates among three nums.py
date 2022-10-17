#WAP to find greatest number from 3 numbers given by user
# using if elif else

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
# num4 = int(input("Enter number4: "))

if num1>num2 and num1>num3: 
    print("Num1 is greatest")
elif num2>num1  and num2>num3: 
    print("Num2 is greatest")
else:
    print("Num3 is greatest")




#WAP to find greatest number from 4 numbers given by user
# using if elif else

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
num4 = int(input("Enter number4: "))

if num1>num2 and num1>num3 and num1>num4:
    print("Num1 is greatest")
elif num2>num1  and num2>num3 and num2>num4:
    print("Num2 is greatest")
elif num3>num1  and num3>num3 and num3>num4:
    print("Num3 is greatest")
else:
    print("Num4 is greatest")
