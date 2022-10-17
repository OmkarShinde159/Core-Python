# Basic calculation
# 1. addition
# 2. sub
# 3. mul
# 4. div
# 5. per

print("1 - addition")
print("2 - subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Percentage")

ch = input("Enter Your Choice: ")

if ch >= 1 and ch <= 4:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

if ch == '1' or ch=='Addition' or ch=='ADDITION' or ch=='addition' or ch=='ADD' or ch=='Add' or ch=='add':
    add = num1 + num2
    print("Addition is: ",add)
elif ch == '2' or ch=='Subtraction' or ch=='SUBTRACTION' or ch=='subtraction' or ch=='SUB' or ch=='Sub' or ch=='sub:
    sub = num1 - num2
    print("Subtraction is: ",sub)
elif ch == '3' or ch=='Multiplication' or ch=='MULTIPLICATION' or ch=='multiplication' or ch=='MUL' or ch=='Mul' or ch=='mul':
    mul = num1*num2
    print("Multiplication is: ",mul)
elif ch == '4' or ch=='Division' or ch=='DIVISION' or ch=='division' or ch=='DIV' or ch=='Div' or ch=='div':
    div = num1/num2
    print("Division is: ",div)    
elif ch == 5 or ch=="Percentage" or ch=="PERCENTAGE" or ch=="percentage" or ch=="PER" or ch=="Per" or ch=="per":
    num1 = int(input("Enter marks of sub1: "))
    num2 = int(input("Enter marks of sub2: "))
    per = ((num1+num2)/200)*100
    print("Percentage is: ",per)
else:
    print("----INVALID NUMBER----(ENTER NUMBER BETWEEN 1-5)----")
    
               

