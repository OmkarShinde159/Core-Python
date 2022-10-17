# inner class or nested class
# one class inside the another class is known as nested.

# syntax
'''
class outer_class:
    class inner_class:   # nested class
        inner_class body

    outer_class_body
'''
'''
# Example
# remote - battery
# car - engine
#cpu = mothreboard
# human - brain
# college - department

class Human:  # outer class
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.b = self.Brain()  # object of inner class(Brain)

    class Brain:  # inner class
        def walk(self):
            print("Walking.....")

        def talk (self):
            print("Talking.....")

    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("1. walk \n2.Talk")
        c=input("enter your choice:")
        if c =="1":
            self.b.walk()   # self.inner_class_object_name.inner_class_method  # self- outer class reference

        elif c == "2":
            self.b.talk()

        else:
            print("Invalid choice")

person=Human("python",23)
person.display()

# inside the outer class
# self.inner_class_object_name= self.inner_class_name()

# Example

class outer_class:
    def __init__(self):
        self.i =self.inner_class()

    def method(self):
        self.i.display("python","python is a programming language")

    class inner_class:
        def display(self,name,msg):
            print(name)
            print(msg)

o=outer_class()
o.method()

############

class outer_class:
    def __init__(self):
        self.i =self.inner_class()

    def method(self,msg):
        self.i.display("python",msg)

    class inner_class:
        def display(self,name,msg):
            print(name)
            print(msg)

o=outer_class()
o.method("pyhton is a object oriented programming language")

# outside the class calling inner class method
# syntax
#outer_class_object,inner_class_object.inner_class_method()
# outer_class_object.inner_class_object.inner_class_method(parameters)

o.i.display("python","learning python")


# 2 way

o1=outer_class()  # outer_class_object= outer_class_name()
i1=o1.inner_class()  # inner_class_object = outer_class_object.inner_class_name()
i1.display("java","program") # inner_class_object.inner_class_method_name()

# 3 way

outer_class().inner_class().display("python", "is a programming language")
'''


# Homework

class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.a=self.engine()

    class engine:
        def model(self):
            print("Engine model is A4244")

        def price(self):
            print("Engine price is 5000")
            

    def info(self):
        print("Car name is:",self.name)
        print("Car price is:",self.price)
        print("1.model \n2.price")
        p=input("enter your choice")
        if p =='1':
            self.a.model()

        elif p =="2":
            self.a.price()

        else:
            print("Invalid choice")

c=car("Range Rover","3cr")
c.info()








'''

#Example 2

class Remote:
    def __init__(self,c_name):
        self.c_name=c_name
        self.b=self.battery()

    class battery:
        def power(self):
            self.b.display()
            print("power is: 3 wh")

    def display(self):
        print("Remote company name :",self.c_name)
        
a=Remote("Hopin")
a.display()

'''


# multilevel class

'''
outer:
    inner:
        inner:
'''
# syntax
'''
class outerclass:
    def __init__(self):
        # inner class object as a instance attribute

    class inner_class:
        def __init__(self):
            # objectof inner class of inner class

        class inner_class_of_inner_class:
            def __init__(self):
                pass

'''

class outer_class:
    def __init__(self,name):
        self.n=name
        self.inner1 = self.inner_class(24)

    def display_name(self):
        return "Name is :" + self.n

    class inner_class:
        def __init__(self,age):
            self.a=age
            self.inner2 =self.inner_class_2("pune")

        def display_age(self):
            return "Age is :" + str(self.a)

        class inner_class_2:
            def __init__(self,location):
                self.l=location
                print("All constructor get calld")

            def display_location(self):
                return "Location is : "+self.l


outer = outer_class("pooja")
print(outer.display_name())

inner_1=outer.inner1
print(inner_1.display_age())

# print(outer.inner1.display_age())

print(outer.inner1.inner2.display_location())

print(outer_class("sayali").inner_class("20").inner_class_2("tasgon").display_location())


###########

class outer_class:
    def __init__(self,name,age,location):
        self.n=name
        self.inner1 = self.inner_class(age,location)

    def display_name(self):
        return "Name is :" + self.n

    class inner_class:
        def __init__(self,age,location):
            self.a=age
            self.inner2 =self.inner_class_2(location)

        def display_age(self):
            return "Age is :" + str(self.a)

        class inner_class_2:
            def __init__(self,location):
                self.l=location
                print("All constructor get calld")

            def display_location(self):
                return "Location is : "+self.l


print()
outer=outer_class("sayali","21","pune")
print(outer.display_name())
print(outer.inner1.display_age())
print(outer.inner1.inner2.display_location())

















































            


            
            
        
        
        



























            
