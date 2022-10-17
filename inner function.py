# inner function or nested function

def outer() :
    print("outer function")
    def inner():
        print('inner function')
    inner()
outer()

def fun(n):
    def in_fun():
        print("Hello",n)
    in_fun()
fun("Python")

# return

def add(n):
    def fun():
        return n+6
    print(fun())
add(45)
print(add(80))

def add(n):
    def fun():
        return n+5
    return fun()
print(add(50))

# ex

def func():
    a=12
    def fun1(b):
        a=6     #nonlocal
        print(a+b)
    print(a)
    fun1(23)
    print(a)
func()  # observe the values of a

# nonlocal

def func():
    a=12
    def fun1(b):
        nonlocal a
        a=6
        print(a+b)
    print(a)
    fun1(23)
    print(a)    # value of a updated because of 'nonlocal' a
func()

'''
# global : we cant update global values using nonlocal
# a=78
# def func():
#     global a
#     def fun1(b):
#         nonlocal a  
#         a=6
#         print(a+b)
#     print(a)
#     fun1(23)
#     print(a)
# func()    #no binding of nonlocal a error
'''

def base(n):
    def exp(n1):
        return n**n1
    return exp(2)
print(base(3))

# with 2 nested or inner function
def outer1():
    print('outer function')
    def inner1():
        print("inner function 1")
    def inner2():
        print("inner function 2")
    inner2()
    inner1()
outer1()

def outer1():
    print("outer function")
    def inner1():
        print("inner function 1")
        def inner2():
            print("inner function 2")
        inner2()
    inner1()
outer1()


def num(a):
    x=a
    def fun():
        print(x)
    fun()
num(90)

def fun1():
    def fun2():
        return 12+90
    return fun2()
print(fun1())
# x = fun1()
# x() #int object is not callable
# print(x())

def fun():
    return "hello world"
print(fun)

# return with memory address
def fun1():
    def fun22():
        return 2+90
    return fun22            # no parenthesis
print(fun1())   # returns the memory address

# closure : return function without parenthesis
# return with memory address
closure_obj = fun1()
print(closure_obj())

# ex of closure

def outer_fun(a):
    c=a
    def inner():
        print(c)
    return inner

c_obj = outer_fun(45)
c_obj()

# 34*2
def first(n):
    def second(n1):
        return n*n1
    return second

o = first(34)
print(o(2))

print(first(32)(2))


def f1(a):
    def f2(b):
        return a*b
    return f2
print(f1(56))
print(f1(2)(2))


clo = f1(55)
print(clo(5))

def f3(li):
    def f4():
        return [x for x in li if x%2==0 ]
    return f4
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
clo = f3(li)
print(clo()) 










        












