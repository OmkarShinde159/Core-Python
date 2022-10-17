'''
def std(f,l):
    print("First Name is: ",f)
    print("Last Name is: ",l)

std("Python","Developer")
std("Omkar","shinde")

first = input("Enter your first name: ")
last= input("Enter your last name: ")
std(first,last)

# argument = in calling functiong
# parameter - in defining function

def greeting(name1,name2,name3):
    print("Hello",name1,",",name2,",",name3)

# Hello name1,name2,name3
greeting("Pooja","Manisha","Omkar")

# int,string, float, list, tuple, set

l = [45,56,65,89,74]
t = (50,55,60,88,47)
s = {4,5,5,9,7}

print(sum(l))
print(sum(t))
print(sum(s))

def lst(l):
    print("Sequence data is: ",l)

lst(l)
lst(t)
lst(s)

def itr(l):
    for i in l:
        print(i)
print("List items: ")
itr(l)
print("tuple items: ")
itr(t)
print("set items: ")
itr(s)
'''

# return statement
# syntax : return expression
# by default None type object

def fun():
    return
x = fun()
print(x)
print(type(x))

# Example
def fun1():
    print("Hello")
    return      # no expression with return so return None value
    print("Hello") # anything assign after return statement will not be printed

print(fun1())

# Example

def fun1():
    return 2        # 2 work as expression so return int datatype
print(fun1())
print(type(fun1()))

# Example
def fun2():
    return 2*2
x = fun2()
print(x)
print(type(x))

# we can access this value of x outside the function also
add = x+x
print(add)

# Example
def fun3():
    return True
f = fun3()
print(f)
print(type(f))

# Example

def add():
    a = 4
    b = 5
    c = 9
    ad = a+b+c
    print("Addition is: ",ad)
z = add()
print(z)
print(type(add()))

# Example
def add():
    a = 4
    b = 5
    c = 9
    return a+b+c
    
z = add()
print(z)
print(type(add()))

# Example of multiple values

def mul_v():
    return 5,6,7,8
print(mul_v())
print(type(mul_v())) 

# Return statement with prameters
# single parmeter diff datatype
def fun(a):
    return a

print(fun(10))
print(type(fun(10)))
print(fun(10.3))
print(type(fun(10.3)))
print(fun(True))
print(type(fun(True)))
print(fun("String"))
print(type(fun("String")))

# multiple parmeter default datatype tuple
def fun1(a,b):
    return a+b

a1 = fun1(212,3)
print(a1)
a2 = fun1(0.2,0.1)
print(a2)
a3 = fun1('Pyt','hon')
print(a3)







