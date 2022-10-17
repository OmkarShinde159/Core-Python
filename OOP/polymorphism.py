# polymorphism

# poly - many
# morph - form

# polymorphism means that one object take many forms
# + plus operator
# * multiplication operator
print(56+99) # addition
print("56"+"90") # concatenation
print("56"*2) # replication
print(56*2) # multiplication

# function - len()
s = len("Python")
print(s)
print(len((2,5,"om",5.5,True)))
print(len([2,5,"om",5.5,True]))
print(len({1:"key1",2:"Value1"}))

# we can achieve polymorphism by 4 ways
# 1. method overriding
# 2. method overloading
# 3. operator overloading
# 4. duck typing

v1 = 90
v1 = 78
print(v1)  # override

# 1. method override

# inheritance concept should be present
# method overriding cannot be done within a class
# the method that is redefined in a child class should have the same name and same signature in parent class
# signature is nothing but number of parameters

class Marks:
    def __init__(self,m1,m2,m3,m4,m5) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def per(self):
        return (self.m1 + self.m2 + self.m3 + self.m4 + self.m5)

class Percentage(Marks):
    def __init__(self, m1, m2, m3, m4, m5) :   # override
        super().__init__(m1, m2, m3, m4, m5)

    def per(self):
        t = Marks.per(self)
        return t/500*100

p = Percentage(12,23,34,45,56)
print(p.per())

# example 2

class Employee:
    def __init__(self,present_days,per_day_sal) -> None:
        self.present_days = present_days
        self.per_day_sal = per_day_sal

    def tot_sal(self):
        return (self.present_days * self.per_day_sal)


class NetSalary(Employee):
    def __init__(self, present_days, per_day_sal,pf) -> None:
        super().__init__(present_days, per_day_sal)
        self.pf = pf

    def tot_sal(self):
        sal = Employee.tot_sal(self)
        return (sal - self.pf)

e = NetSalary(22,1500,2000)
print(e.tot_sal())

class addition:
    def add(self,a,b):
        print(" in parent class ")
        return a*b
        
class number(addition):
    def add(self,a,b):
        print(addition.add(self,a,b))
        print(" in child class ")
        return a+b

n = number()
print(n.add(12,2))

        

# method overloading
# same class
# name will be same and signature(parameters) will be different

# case 1: using default argument
class Addition:
    def add(self,n1=0,n2=0,n3=0,n4=0):
        if n1!=0 and n2!=0 and n3!=0 and n4!=0:
            return n1+n2+n3+n4
        elif n1!=0 and n2!=0 and n3!=0:
            return n1+n2+n3
        elif n1!=0 and n2!=0:
            return n1+n2
        elif n1!=0:
            return n1
        else:
            return 0

a = Addition()
print(a.add())
print(a.add(13))
print(a.add(13,26))
print(a.add(13,26,39))
print(a.add(13,26,39,52))

# Example 2 : variable length argument
class concate:
    def con(self,dt=0,*var):
        if dt=="int":
            a=0
            for c in var:
                a = a+c
            return a
        else:
            a = ""
            for c in var:
                a = a+c
            return a
c1 = concate()
print(c1.con())
print(c1.con("int",2,5,8))
print(c1.con("Str","python"," java"))    

# same class
class method_overloading:
    def area(self,s):
        return 4*s
    def area(self,l,b):
        return l*b
    def area(self,l,b,h):
        return l*b*h

# m = method_overloading()
# #print(m.area(34))        # raises an error because of method overriding same as value override concept 

# using dispatch decoratpor
# pip install multipledispatch
from multipledispatch import dispatch 
# @dispatch(datatypes)

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

m = Area_cal()
print(m.area(34))
print(m.area(10,20,3))
print(m.area(5,14))

class Veh_details:
    @dispatch(str,int)
    def details(self,type_of_veh,seats):
        print("Type of vehicle is : ", type_of_veh)
        print("No of seats: ",seats)

    @dispatch(str,int,bool)
    def details(self,type_of_veh,seats,has_doors):
        print("Type of vehicle is : ", type_of_veh)
        print("No of seats: ",seats)
        print("has doors ?",has_doors)

    @dispatch(str,int,bool,float)
    def details(self,type_of_veh,seats,has_doors, rating):
        print("Type of vehicle is : ", type_of_veh)
        print("No of seats: ",seats)
        print("has doors ?",has_doors)
        print("Car version: ", rating)
        
c = Veh_details()
c.details("classic 350", 2)
print()
c.details("Baleno",5,True)
print()
c.details("Scorpio",7,True,4.5)

