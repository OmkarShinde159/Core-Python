# OOP - Object Oriented Programming
# Object - class
# create user definied classes


# POP - Procedure Oriented Programming
# function
# create user defined functions

s = 'string'
print(type(s))

'''
creating class and objects

class class_name:
    body
    
object_name = class_name()

difference between class and object
1. class is blueprint or structure for object
2. object is instance of the class

terms in oops
variable - data members  or attributs
function - member function or methods

# object is an instance of a class
# object is real world entity

data member - state (eg. name, age, contact)
methods - behaviour (eg.speak, travel, bark)


'''
class hello:
    print('hello world')

h = hello()
h1 = hello()

class hello1:
    x = 10
    y = 9
    print(x + y)
h = hello1()
print(h.x)  # access the x using h object

# methods
'''
without parameter
def method_name(self):
    body
    
with parameter
def methods_name(self,p1_name,p2_name):
    body
    
# self - supporting variable
'''
class m_name:
    def m1(self):
        print("Hello world")

c = m_name()
# print(c)
# access the function using object c
# object_name.method_name()
# string_name.join()   # str - join method 
c.m1()
c1 = m_name()
c1.m1()

# we can not share data from one function to another
# but in oop we can share data from one method to another

'''
case 1

def add():
    a = 90
    print(a)
add()
def sub():
    b = 9
    print(a-b) # a is not defined i.e we cannot access/ use 'a' from above function
sub()
'''
'''
case 2

class ex:
    def m1(self):
        a = 9
    def m2(self):
        b = 90
        print(a+b)  # here also a is not defined because we did not use self
e = ex()
e.m1()
e.m2()
'''
# self - current object - reference(memory address)
class ex:
    def m1(self):
        self.a = 9
    def m2(self):
        self.b = 90
        print(self.a + self.b)  # here also a is not defined because we did not use self
e = ex()
e.m1()
e.m2()
# e.a = 89
print(e.a)

e2 = ex()
# print(e2)
e2.m1()
e2.m2()
print(e2.a)
print(e2.b)

# state of object / attributes / data members
# acces through object
# self is use stored the values of states inside the object
# so that we can access the stored values using object
# self is used for data share within methods

# constructor
# constructor is a special methods because it automatically get called
# which is get called when object of our class is created
# constructor is used to initialize the data member of the class
# constructor in python is defined using __init__() name.
# syntax:
# def __init__(self):
# types : default , parameterized

# default ocnstructor
class person:
    def __init__(self) -> None:
        self.name = "Python"
        self.addr  = "Memory"
    def info(self):
        print("Name :",self.name)
        print("Address :",self.addr)

p = person()
p.info()

# parameterized method
class Person:
    def info(self,name,address):
        self.name = name
        self.addr = address
        print(self.name,self.addr)

p = Person()
p.info("omkar","thane")


# parameterized constructor
class person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.addr = address
        print(self.name, self.addr)

    def info(self):
        print("Name :",self.name)
        print("Address :",self.addr)

p = person("Omkar","Thane")
p.info()