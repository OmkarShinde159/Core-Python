# Abstraction
#Abstraction is the art of representing essential details.
# Abstraction is the process of selecting data to show only the relevent information to the user.
# In simple terms,Abstraction "displays" only the relevent attribute of the object.
#and "hides" the unnessesry details.
# abc - module
# ABC - class -abstact base class

# super - ABC
# sub - abstact_class
# abstact methods - which doesent have any  implementation

# vehicle - wheels,color,breaks,start/stop

from abc import ABC,abstractmethod
class vehicle(ABC):  # abstact class
    
    def __init__(self,t_veh): # constructor in abstaction class
        self.t=t_veh

    @abstractmethod
    def wheels(self): # abstact method
        pass

    def color(self,color):  # concrete method
        self.color=color

class car(vehicle):
    def wheels(self):
        self.n=4

    def details(self):
        print("\nType of vehicle:",self.t)
        print("No.of wheels:",self.n)
        print("color:",self.color)

c=car("car")
c.wheels()
c.color("Red")
c.details()


# v=vehicle() # we cant create object abstact class
# we cant create object abstact class.
# abstact class can not be instantiated.
# Abstract class can have abstact method and concreate method (non-abstact method)
# abstract class can have constructor.
        
# we can define following types of method inside the abstract class

# abstract method
# concreate method
# constructor
# static method

# Example

from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def setrateofintrest(self):  #abstract method
        pass
    
    def __init__(self,name): #constructor
        self.n=name

    @abstractmethod
    def display_name(self):
        pass

    @ abstractmethod
    def getrateofintrest(self):
        pass
class HDFC(Bank):
    def setrateofintrest(self):
        self.r=6
        print("Rate of intrest set successfully")

    def display_name(self):
        return "Name of bank:"+self.n

    def getrateofintrest(self):
        print("Rate of intrest is:",self.r)

class ICICI(Bank):
    def setrateofintrest(self):
        self.r=9
        print("Rate of intrest set successfully")

    def display_name(self):
        return "Name of Bank:" +self.n

    def getrateofintrest(self):
        print("Rate of Intrest is:",self.r)

i=ICICI("ICICI")
i.display_name()
i.setrateofintrest()
i.getrateofintrest()

class Bankdemo:
    def hdfc(self):
        h=HDFC("HDFC")
        h.setrateofintrest()

        print("1.check rate of intrest \n2.check Bank name")
        c=input("Enter your choice:")

        if c=="1":
            h.getrateofintrest()
        elif c=="2":
            print(h.display_name())

        else:
            print('invalid choice')

    def icici(self):
        i=ICICI("ICICI")
        i.setrateofintrest()

        print("1.check rate of intrest \n2.check Bank name")
        c=input("Enter your choice:")

        if c=="1":
            i.getrateofintrest()
        elif c=="2":
            print(i.display_name())

        else:
            print('invalid choice')

print()
b=Bankdemo()

print("1. HDFC \n2.ICICI")
n=input("Enter your choice:")

if n=="1":
    b.hdfc()
elif n=='2':
    b.icici()
else:
    print("Enter valid choice")

###########33
    # shape- rectangle, square,circle
# perimeter and area -method

class Shape(ABC):
    def __init__(self,color): #constructor initilize
        self.c=color

    def shape_details(self):  # concrete method
        #print("Types of shape:",self.s)
        # print("color :"self.c)
        return self.c
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @staticmethod
    def value_of_pi():
        return "value of pi:"+str(3.14159)

class circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.r=radius

    def area(self):
        return 3.14159 * self.r **2

    def perimeter(self):
        return 2* 3.14159 *self.r

    def display(self):
        return "\nshape: circle" + '\ncolor is:' +super().shape_details()+ "\nArea is:" + str(self.area()) +"\ncircumference is:"+str(self.perimeter())


c=circle("Purple",2.5)
print(c.display())
print(c.value_of_pi())

























        
        
    
        
        
    
        





















    
    

        
              
    
























        
    
    
    

    































