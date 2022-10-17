# is a relationship  (inheritance)
# has a relationship (composition)

# parent
# child (object of parent class)
# example 1
class ABC:
    def __init__(self) -> None:
        print("constructor of class A") 
    def method(self):
        print("hello, I am of ABC class")


class XYZ:
    def __init__(self) -> None:
        print("Constructor of xyz")
    def method1(self):
        abc = ABC()  # object of ABC class inside class XYZ
        abc.method()
        print(" In method 1")

obj_xyz = XYZ()
obj_xyz.method1()

# example 2
class Person:
    def __init__(self,name) -> None:
        self.name = name 
    def  c_method(self):
        print("Name is: ", self.name)

class Student:
    def __init__(self,name) -> None:
        self.comp = Person(name)  # object of component class
        print("Constructor of comp class")

    def c1_method(self,age):
        self.comp.c_method()
        print("Age is: ", age)

c = Student("Python")
c.c1_method(45)
print()
c.comp.c_method()

# example 3
class friend:
    car = "Maruti"
    def has_a_car(self):
        print("friend has a car", friend.car)

class person:
    bike = "classic 350"
    f = friend()   # state orr class type attribute
    def has_a_bike(self):
        print("Person has a bike",person.bike)

p = person()
p.f.has_a_car()
person.f.has_a_car()
p.has_a_bike()

# example 4

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def display(self):
        print("Name is:",self.name)
        print("age is: ",self.age)

class student_details:
    def __init__(self,address,roll_no,obj_per) -> None:
        self.address = address
        self.roll_no = roll_no
        self.obj_per = obj_per

    def display_details(self):
        self.obj_per.display()
        print("Address is: ",self.address)
        print("Roll no: ", self.roll_no)

p1 = Person("pooja",21)
pooja = student_details("Mumbai",23,p1)
pooja.display_details()




           
