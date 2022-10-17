
if True :
    print("condition is True")

if False :
    print("condition is not True")
    
print("condition is not True")

a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))


#-------------------------------------------------------------------------------

if a < 5 and b > 10:
    print("Values satisfies the condition")
else: 
    print("please enter values less than 5 and greater than 10")

if a == 5 and b != 5:print("Values satisfies the condition")
else: print("Insert different Values")

#-------------------------------------------------------------------------------

# WAP to perform addition of two numbers 
# and print the addition value only if its positive

a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))
if a + b >= 0:
    print("The addition value is: ", a + b)
else:
    print("Addition value is not positive")

#-------------------------------------------------------------------------------


# take 1 number from user and check if that number is 
# greater than 100 or not 
num = int(input("Enter the number: "))
if num > 100:
    print("The number",num,"is greater than 100")
else:
    print("Number is Not greater than 100")
    
    
# take 1 number from user and check if that number is 
# greater than 100 and less than 200 or not  
num = int(input("Enter the number: "))
if num > 100 and num < 200:
    print("The number",num,"is greater than 100 & less than 200")
else:
    print("Number is not between 100 and 200")
