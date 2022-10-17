# difference between syntax error and exception
# try and except statement 

# 
# case 1 : simple runtime error handling
a = [1,2,3]
try:
    print("Second element = %d"%(a[1]))
    print("Forth element = %d"%(a[3]))

except:
    print("an error occured")


# case 2 : catching specific exception
def fun(a):
    if a < 4:
        b = a/(a-3)
    print("value of b is",b)

try:
    # fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError and Handled")

except NameError:
    print("NameError and handled")


# case 3 : Try with else

def abc(a,b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("Result of a/b is 0")
    else:
        print(c)

abc(2,2)
abc(4,3)

# case 4 : using finally keyword
try:
    k = 5//0
    print(k)
except ZeroDivisionError:
    print("Can't be devide by zero")
finally:
    print("This is always executed")

# case 5 : depict raising exception

try:
    raise NameError("Hi There")
except NameError:
    print("An Exception")
    # raise

# case 6 : try - except

def divide(x,y):
    try:
        result = x//y
        print("Yeah ! The answer is :",result)
    except ZeroDivisionError:
        print("Sorry, You are dividing by zero")

divide(3,2)
divide(3,0)

# case 7 : try - except - else
def abc(a,b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("Can not divide by zero")
    else:
        print(c)

print()
abc(1,1)
abc(2,1)

# case 8 : try - except - else - finally

def abcd(a,b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("Can not divide by zero")
    else:
        print(c)
    finally:
        print("Always executed")
print()
abcd(1,1)
abcd(2,1)

# case 9 : raising an exception for predefined condition
try:
    amount = 2999
    if amount < 2999:
        raise ValueError("Please add money in your account")
    else:
        print("you are eligible")
except TypeError as e:
    print(e)

