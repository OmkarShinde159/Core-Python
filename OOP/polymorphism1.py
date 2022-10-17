# polymorphism

# poly - many
# morph - form

# polymorphism means that one object can take many forms.

#+ (plus oprator)
# * (multiplication oprators)
'''
print(34+58) # addition
print("45"+"76")  # concatination
print("56"*2) # repeatation
print(56*2)  #multplication

# function - len()

s=len("python")
print(s)
print(len((12,34,54,"pooja",45,62)))
print(len([12,34,54,"pooja",45,6]))
print(len({"k1":"

'''
'''
#1. Method overriding

# inheritance concept should be present
#method overriding cannot be done within a class
#The method that is redefine in the child class should have thesame name and
# same signature as in the parent class
# signature is nothing but a number of parameters.

# Example
class marks:
    def __init__(self,m1,m2,m3,m4,m5):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def per(self):
        return(self.m1+self.m1+self.m3+self.m4+self.m5)

class percentage(marks):
    def __init__(self,m1,m2,m3,m4,m5):  # override
        super().__init__(m1,m2,m3,m4,m5)

    def per(self):
        t=marks.per(self)
        return t/500*100

p=percentage(78,89,76,92,88)
print(p.per())

#Example second


class ABC:
    def __init__(self,h1,h2,h3):
        self.h1=h1
        self.h2=h2
        self.h3=h3
    def Avg_hi8(self):
        return self.h1+self.h2+self.h3

class Avrage(ABC):
    def __init__(self,h1,h2,h3):
        super().__init__(h1,h2,h3)

    def Avg_hi8(self):
        h=ABC.Avg_hi8(self)
        return h/3

s=Avrage(5.5,4,6)
print(s.Avg_hi8())

#Example 3

class employee:
    def __init__(self,present_days,perday_sal):
        self.present_days=present_days
        self.perday_sal=perday_sal

    def tot_sal(self):
        return(self.present_days*self.perday_sal)

class Netsalary(employee):
    def __init__(self,present_days,perday_sal,pf):
        super().__init__(present_days,perday_sal)
        self.pf=pf

    def tot_sal(self):
        sal=employee.tot_sal(self)
        return(sal-self.pf)

e=Netsalary(20,1500,2000)
print(e.tot_sal())


class addition:
    def add(self,a,b):
        return a*b

class number(addition):
    def add(self,a,b):
        print(addition.add(self,a,b))
        return a+b
n=number()
print(n.add(10,2))


# Method overriding

# same class
# name will be same and signature (parameter)will be different

# by using default argument

class addition:
    def add(self,n1=0,n2=0,n3=0,n4=0):
        if n1 != 0 and n2 !=0 and n3 != 0 and n4 != 0:
            return n1+n2+n3+n4
        elif n1 != 0 and n2 != 0 and n3 != 0:
            return n1+n2+n3
        elif n1 != 0 and n2 !=0:
            return n1+n2
        elif n1 !=0:
            return n1
        else:
            return 0
        
a=addition()
print(a.add())
print(a.add(15))
print(a.add(5,10,6))
print(a.add(3,6,7,5))

# Example 2
# variable length argument

class concate:
    def con(self,dt=0,*var):
        if dt=="int":
            a=0
            for c in var:
                a= a+c
                return a

        else:
            a = ""
            for c in var:
                a=a+c
                return a
c1=concate()
print(c1.con())
print(c1.con("int",34,67,89))
print(c1.con("int",24,56,778,980,))
print(c1.con("str","str1","python"))

# same class

class method_overloading:
    def area(self,s):
        return 4*s
    def area (self,l,b):
        return l*b
    def area(self,l,b,h):
        return l*b*h

m=method_overloading()
#print(m.area(34))

#multipledispatch

import multipledispatch

#cmd
# pip install multipledispatch




# @classmethod
# @staticmethod

# @dispatch (datatype)

from multipledispatch import dispatch

class Area_cal:
    @dispatch(int)
    def area(self,s):
        return 4*s

    @dispatch(int,int)
    def area(self,l,b):
        return l*b

    @dispatch(int,int,int)
    def area(self,l,b,h):
        return l*b*h

a=Area_cal()
print(a.area(64))
print(a.area(34,6))
print(a.area(3,6,7))



#date - 14 sep 22

# 3.Oprator overloading

#oprator ki functionality ko overloading karna

#addition +
# int +int  # addition
# str + str #concatenation

n=45
print(type(n))

s="45"
print(type(s))

print(n+90)
print("60"+"60")

#print(45+"56")

print(dir(int))


# magic method

x=int.__add__(90,90)
print(x)

#print(dir(str))

s="90"
s1="90"
y=str.__add__("90","90")
print(y)

print(str.__add__(s,s1))

print(dir(list))

#tuple_name.count(90)

# oprator overloading is the ability of a single operator to perform more than__
# one opration based on the class(type)of operand

#(+) __add_(self,other)
#2 operand
#self - 1st operand
# other  - 2nd operand

# for example: 10+20
#10- self
#20 - other

#Example 1

class A:
    def __init__(self,n):
        self.n=n
        
    def __add__(self,other):
        return self.n+other.n
    
class B:
    def __init__(self,n):
        self.n=n

        
a=A(67)
b=B(3)
print(a+b)

# Example 2

class A:
    def __init__(self,n):
        self.n=n
        
    def __add__(self,other):
        return self.n+other.n
    
class B:
    def __init__(self,n):
        self.n=n

    def __add__(self,other):
        return self.n * self.n
    
a=A(67)
b=B(3)
print(10+20)  # 30
print(a+b)
print(b+a)  # multiplication (operator overloading)
print(67*3)

# Example

str(90)
print(type(int.__str__(90)))


# Example( using __sub__)(substraction)

class Add:
    def __init__(self,a):
        self.a=a

    def __sub__(self,other):
        return self.a - other.a

class Add1:
    def __init__(self,a):
        self.a=a
        
    def __sub__(self,other):
        return self.a - other.a

a=Add(12)
b=Add1(10)

print(a -b)  # __sub__(self,other)
print(b-a)


# Example 2

class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __sub__(self,other):
        return (self.a+self.b) - (other.a+other.b)
    

class Add1:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __sub__(self,other):
        return (self.a + self.b) *(other.a+other.b)

a=Add(12,2)
b=Add1(10,3)
print(a-b) #(12+2)-(10+3) => 1
print(b-a)# (12+2)*(10+3) => 182

# Example- 3

class mul:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __sub__(self,other):
        return (self.a - self.b) *(other.a - other.b)

class mult:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __sub__(self,other):
        return (self.a +self.b) /(other.a+other.b)

a=mul(12,4) #(12-4) * (15-5)
b=mult(15,5)#(15+5)/(12+4)

print(a-b)
print(b-a)

print(8*10) #80
print(20/16) #1.25

# Example
# using multipication method
#__mul__()
class mul:
    def __init__(self,n):
        self.n=n

    def __mul__(self,other):
        return self.n * other.n

class mult:
    def __init__(self,n):
        self.n=n

p=mul(5)
q=mult(6)
print(p*q)

# for 3 parametere

class mul:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __mul__(self,other):
        return (self.a+self.b) *(other.a+other.b)
    
class div:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __mul__(self,other):
        return (self.a+self.b) /(other.a+other.b)
    
        
p=mul(4,5)
q=div(3,6)
print(p*q)
print(q*p)
    

#Example
#using 3 parameter

class add:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __add__(self,other):
        return (self.a+self.b+self.c) + (other.a+other.b+other.c)
    
    
class sub:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __add__(self,other):
        return (self.a+self.b+self.c) - (other.a+other.b+other.c)
    
p=add(5,6,7)
q=sub(2,3,4)
print(p+q)
print(q+p)

# 15 sep 22

# len()
print(dir(int))

print(len([9]))
# __len__()

class Num:
    def __init__(self):
        pass
    def __len__(self):
        return 0

n=Num()
print(len(n))

class Num1:
    def __init__(self):
        pass

n1=Num1
#print(len(n1))



# 4. Duck Typing

a=90
a="python"

# In python we follow a principle for duck typing.
# if its walk like a duck,sounds like a duck and looks like a duck then it mustbe a duck
# which means python doesn't care about which class of object it is, if its an object
#and requrired behavior is present for that object thenit will work.
#The type of object is distinguished only run time this is called duck typing.

#method

class Duck:
    def __init__(self):
        pass
    def walk(self):
        print("Its walk like a duck")
class Horse:
    def __init__(self):
        pass
    def walk(self):
        print("Its a horse but its walk like a duck")

d=Duck()
h=Horse()
             
#d.walk()
#h.walk()
def main(obj):
    obj.walk()

main(d)
main(h)
main(Duck())  # object through
print(Duck())
print(d)

### Example 2

class Duck:
    def __init__(self):
        pass
    def walk(self):
        print("Its walk like a duck")

class Horse:
    def __init__(self):
        pass

    def walk(self):
        print("Its a horse but its walk like a duck")

class cat:
    def __init__(self):
        pass

    def sound(self):
        print("Meow meow")

d=Duck()
h=Horse()
c=cat()

#d.walk()
#h.walk()
def main(obj):
    obj.walk()

main(d)
main(h)
main(Duck())  # object through
print(Duck())
print(d)
    
# loop
print("Using loop")

for obj in (d,h):
    obj.walk()

print("Another method")

for obj in [Duck(),Horse()]:
    obj.walk()
    
        
# Ex

s="python"
t=(1,2,3,4)
l=[1,2,3,4,5]
d={"k1":"v1","k2":"v2"}

def length(var):
    l=len(var)
    print(l)

class num:
    def __init__(self):
        pass
    def __len__(self):
        return 0
    
length(s)
length(t)
length(l)
length(d)

#
for i in (s,l,t,d):
    print(len(i))


# Example

class car:
    def __init__(self,name):
        self.name=name
        
    def wheels(self,no):
        self.no=no
        
    def display(self):
        print("Car name:",self.name)
        print("No.of wheels:",self.no)

class auto:
    def __init__(self,name):
        self.name=name

    def wheels(self,no):
        self.no=no

    def display(self):
        print("Auto name:",self.name)
        print("No.of wheels:",self.no)

class cycle:
    def __init__(self,name):
        self.name=name

    def wheels(self,no):
        self.no=no

    def display(self):
        print("cycle name:",self.name)
        print("No.of wheels:",self.no)

c=car("Maruti")
a=auto("Auto")
cy=cycle("cycle")

def fun(object,no):
    object.wheels(no)
    object.display()

# invoke - calling the method or fuction

fun(c,4)
fun(a,3)
fun(cy,2)

print("using loop")

for obj, no in [(c,4),(a,3),(cy,2)]:
    obj.wheels(no)  # c.wheels(4)
    obj.display()


# homework

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hight(self,hi8):
        self.hi8=hi8

    def info(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        print("Hight :",self.hi8)

class B:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hight(self,hi8):
        self.hi8=hi8

    def info(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        print("Hight :",self.hi8)
class C:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hight(self,hi8):
        self.hi8=hi8

    def info(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        print("Hight :",self.hi8)

a=A("xyz",21)
b=B("aps",24)
c=C("pqr",45)

def func(object,hi8):
    object.hight(hi8)
    object.info()

func(a,5)
func(b,5.4)
func(c,5.6)

print()
print("using loop")
for obj,hi8 in [(a,5),(b,5.4),(c,5.6)]:
    obj.hight(hi8)
    obj.info()
    
print()

# Example 2

class company1:
    def __init__(self,com_name):
        self.com_name=com_name

    def dev_salary(self,dev_sal):
        self.dev_sal=dev_sal

    def display(self):
        print("Company name:",self.com_name)
        print("Devloper month salary:",self.dev_sal)
        
class company2:
    def __init__(self,com_name):
        self.com_name=com_name

    def dev_salary(self,dev_sal):
        self.dev_sal=dev_sal

    def display(self):
        print("Company name:",self.com_name)
        print("Devloper month salary:",self.dev_sal)
        
    
a=company1("TATA")
b=company2("Wipro")

def sal(obj,dev_sal):
    obj.dev_salary(dev_sal)
    obj.display()


sal(a,20000)
sal(b,15000)
'''        


























































































        











                
            

























            













    
               

        












