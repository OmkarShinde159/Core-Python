'''
li = [20,31,32,31,56,15]

# built in 
print(max(li))
print(min(li))
print(sum(li))

x = -9
print(abs(x))


# user defined func 
# create a calculator using functions for two input numbers

def add():
    print("In add function")
    a = int(input("Enter num: "))
    b = int(input("Enter num: "))
    add = a+b
    print(add)

def sub():
    print("In sub function")
    a = int(input("Enter num: "))
    b = int(input("Enter num: "))
    sub = a-b
    print(sub)

def div():
    print("In div function")
    a = int(input("Enter num: "))
    b = int(input("Enter num: "))
    add = a/b
    print(div)

def mul():
    print("In mul function")
    a = int(input("Enter num: "))
    b = int(input("Enter num: "))
    add = a*b
    print(mul)

def perc():
    print("In perc function")
    a = int(input("Enter num: "))
    b = int(input("Enter num: "))
    add = a+b/200*100
    print(perc)


print("1.addition")
print("2.subtraction")
print("3.division")
print("4.multiplication")
print("5.percentage")

ch = input("Enter choice: ")
if ch =='1':
    add()
elif ch == '2':
    sub()
elif ch == '3':
    div()
elif ch == '4':
    mul()
elif ch == '5':
    perc()

'''
# values that we pass along with finction call are called as parameters
# parameters are act as a input in functions
# functions are created for reusability of code
# def func_name(parameter_name):

def findSq(a):
    x = a**2
    print("Squared values of,",a,"is,",x)

#x = int(input("Enter num to find square: "))
#findSq(x)
#findSq(5)


def sayHello(name):
    print("Hello",name,",How are you?")

sayHello("Pooja")

def ptr(x):
    for i in range(x):
        for j in range(i+1):
            print("+",end=" ")
        print()

def absolute(a):
    if a>0:
        print("absolute value is: ",a)
    else:
        print("absolute value is: ",-a)

#absolute(-6)
    

ptr(5)

def findEvenOdd(num):
    if num>0 and num%2 == 0:
        print(num,", is Even Number")
    else:
        print(num,", is Odd Number")

#num = int(input("Enter the num to check even or odd: "))
#findEvenOdd(num)
        
#findEvenOdd(3)
#findEvenOdd(4)

def per(ob,t):
    if ob <= t:
        p = ob/t*100
        print("Percentage is: ",p)
    else:
        print("---Obaining marks should be less or equal to total marks---")

ob = int(input("Enter Obtaining marks: "))
t = int(input("Enter Total Marks: "))
per(ob,t)
per(350,400)


# when we devide two integers then then the data type of its quotient is float


    


