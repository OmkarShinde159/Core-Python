
# calling user defined function using lambda function

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

    # use this functions in lambda without using print() in expression
l = lambda x,y : add(x,y)
print(l(2,5))

    # with using print() in lambda expression
s = lambda x,y : print(sub(x,y))
s(5,2)
print(s(12,3))  # returns extra None value also

l = lambda x,y : print('addition of',x,'and',y,'is:', add(x,y))
st = l(15,12)
print(type(st))     # NoneType object

l = lambda x,y : ('addition of',x,'and',y,'is:', add(x,y))
st = l(15,12)
print(st)
print(type(st))     # Tuple object

def add1(a,b,c):
    return a+b+c
add = lambda : add1(1,2,3)
print(add())


# defining lambda function inside user defined function

def fun(n):
    return lambda a : a+n
x = fun(12)
print(x(3))

def fun1(a,b):
    return lambda a,b: 'a is greater' if a>b else 'b is greater'
maxx = fun1(12,5)
print(maxx(12,5))



# calling lambda function inside user defined function

min = lambda a : a

def fun2():
    print(min(12))
fun2()

def fun3():
    return (min(13))
x = fun3()
print(x)

    # assign parameters and pass arguments
def fun4(l):
    return min(l)
print(fun4(15))

min1 = lambda x,y : 'x is less' if x<y else 'y is less'

def min_fun(a,b):
    return min1(a,b)
print(min_fun(12,23))


# calling lambda function using lambda function

add = lambda a,b: a+b
sub = lambda a,b: a-b

a = lambda x,y: add(x,y)
b = lambda x,y: sub(x,y)

print(a(12,3))
print(b(12,3))

# passing user input to lambda function

# method 1
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

print(add(num1,num2))
print(sub(num1,num2))

# method 2
print(sub(int(input("EN1:")),int(input("EN2:"))))




















