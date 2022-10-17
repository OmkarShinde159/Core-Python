# types of methods
# 1. Instance method :- ocject_name.method_name()
# 2. class method
# 3. statis method

# Instance method
# obj_name.method_name()






class Employee:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def details(self):   # instannce method
        print(" information of employee")
        print("Name is: ",self.name)
        print("Age is: ",self.age)

    def update(self,name,age):
        self.name = name
        self.age = age
        print("----updated-----")

    def update_name(self,name):
        self.name = name
        print("Name updated")

    def update_age(self,age):
        self.age = age
        print("Age updated")

e1 = Employee("Python",34)
e1.details()
print()
e1.update("java",56)
# print(e1.name)
e1.details()

# n = input("Enter name: ")
# m = input("Enter age: ")
# e1.update_name(n)
# e1.update_age(m)
# e1.details()


# CLASS METHOD
# decorator
# @classmethod

# classname.classattribute

class Employee:
    salary = 500000   # class attribute
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def info(self):
        print("information")
        print("Name is: ",self.name)
        print("Age is: ",self.age)
        print("Salary is: ", self.salary)
        print("Salary is for all: ", Employee.salary)

    @classmethod
    def update_sal(cls,sal):
        cls.salary = sal


python = Employee("Python",23)
python.info()
python.update_sal(600000)
python.info()
python.salary = 89000
python.info()

java = Employee("java",89)
java.info()
java.update_sal(456899)
java.info()
print()
python.info()

# static method
# @staticmethod

class static:
    def __init__(self) -> None:
        pass

    @staticmethod
    def example():
        print("I am static method")

s = static()
s.example()

class static:
    def __init__(self,n,n1) -> None:
        self.n = n
        self.n1 = n1

    @staticmethod
    def example():
        print("I am static method")

s = static(90,9)
s.example()

###
class Student:
    school_name = "PYTHON"

    def __init__(self,name,age,marks) -> None:
        self.name = name
        self.age = age
        self.marks = marks
    def info(self):
        print(" student information ")
        print("Name is: ", self.name)
        print("Age is: ", self.age)
        print("Marks is : ",self.marks)
        print("School name is: ",self.school_name)
        print("School name is for all : ",Student.school_name)

    @classmethod
    def update_school_name(cls,sname):
        cls.shool_name = sname
        print("--value updated--")

    @staticmethod
    def per(ob,t):
        if ob<=t:
            return ob/t*100
        else:
            return "Enter valid marks"

s = Student("Python",18,450)
s.info()

s.update_school_name("NEW")
s.info()

x = s.per(s.marks,500)
print(x)



       






