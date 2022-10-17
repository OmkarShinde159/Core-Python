# Encapsulation

#Encapsulation is a concept of oop(object oriented programming)
#Encapsulation is the process of wrapping or bundling data member and method
#a single unit

#Encapsulation provides security by using access modifier
#Encapsulation can be achived by using access modifier

# Access specifier or access modifier

#1.Public access modifier - accesible anywhere from outside the class
#2. protected access modifier - Accessible within the class and its child class
#3.private access modifier - Accesible within the class

#public attribute
# public method

# private attribute or method
# define by using double underscore(__) before the attribute name

# protected attribute or method
# define by using single underscore(_) before the attribute name

class employee:
    def __init__(self,name,sal,age):
        self.name=name
        self.__sal=sal   # private attribute
        self._age= age   # protect attribute

    def info(self):
        print("NAme is:",self.name,"\nSalary is:",self.__sal,"\nAge is:",self._age)


e=employee("pooja",100000,25)
e.info()
e.age=26
print(e.age)
e.info()


# Access specifier or modifier
#1. Public
#2. Protected
#3. Private

# getter and setter method
# public data member (attribute)

class emp:
    def __init__(self,name,age,location):  # constructor
        self.name = name
        self.age = age
        self.location =location

    def show_info(self): # getter method
        print("Employee details")
        print("Name is:",self.name)
        print("Age is :",self.age)
        print("Location :",self.location)

    def set_info(self,name,age,location):   #setter method
        self.name=name
        self.age=age
        self.location=location
        print("update successfuly")
    
e=emp("Employee",45,"Pune")
e.show_info()
e.set_info("ABC",23,"Mumbai")
e.show_info()


####

class emp:
    def __init__(self,name,age,location):
        self.name=name
        self.age =age
        self.location=location

    def show_info(self):  # getter method
        print("Employee details")
        print("NAme is:",self.name)
        print("Age is:",self.age)
        print("Location is:",self.location)

    def sel_info(self,name,age,location):  # setter method
        self.name=name
        self.age=age
        self.location=location
        print("update successfuly")

class director(emp):
    def __init__(self,name,age,location,sal):
        super().__init__(name,age,location)
        self.sal=sal

    def show_dir(self):
        super().show_info()
        print("Salary is:",self.sal)
        print(" NAME:",self.name)

    def set_sal(self,sal):
        self.sal=sal

d=director("pyhton",45,"pune",100000)
d.show_info()
d.show_dir()
d.show_info()
print(d.name)
d.name="java"
d.show_dir()

d.set_sal(5576865)
d.show_dir()

d.sal=3355968
d.show_dir()



# private attribute
# __(double underscor)

class school:
    def __init__(self,s_name):
        self.__s_name=s_name

    def display(self):
        print("\nschool name is:",self.__s_name)
        
    def set_school_name(self,s_name):   # setter method
            self.__s_name=s_name

s=school("Squad")
s.display()

#print(s.__s_name)
s.set_school_name("Squad,infotech")
s.display()  # by getter method

# Example (by using inherietance)

class school:
    def __init__(self,s_name):
        self.__s_name=s_name

    def display(self):
        print("\nSchool_name is:",self.__s_name)

    def set_school_name(self,s_name):   # setter method
        self.__s_name=s_name

class student(school):
    def __init__(self,s_name,name,roll_no,age):
        super().__init__(s_name)
        self.name=name
        self.roll_no=roll_no
        self.age=age

    def s_display(self):
         print("\n(student details")
         print("Name is :",self.name)
         print("Roll_no is:",self.roll_no)
         print("Age is :",self.age)
         #print("Shool name:",self.__s_name)
         #self.display()
         super().display()

    def set_student_details(self,age):
            self.age=age

java=student("squad","java",45,23)
java.s_display()
java.set_student_details(34)
java.s_display()
java.age=67
java.s_display()

#print(java.__s_name)

java.display()
java.set_school_name("Squad infotech")
java.s_display()


class teacher(school):
    pass


# protected attribute
# _(underscore)
#by using object, protected attributes can be accessible from outside the class

class car:
    def __init__(self,name):
        self._name=name

    def display(self):
        print("car name:",self._name)

c=car("Maruti")
c.display()

print(c._name)
c._name='Thar'
c.display()

################
class vehicle:
    def __init__(self,c_name):
        super().__init__("car")
        self.c_name=c_name

    def display(self):
        #super().display()
        print("vehicle name:",self._name)
        print("car name:",self.c_name)

c=car("shift")
c.display()


class Employee:
    def __init__(self,name,age) -> None:
        self.name = name
        self.__age = age

    def public(self):
        print("Public method")
        print(self.name)
        print(self.__age)


e = Employee("omkar",25)
e.public()


    
    























































        

































































