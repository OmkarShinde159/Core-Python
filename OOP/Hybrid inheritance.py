# hybrid inheritance
# combination of two or more inheritances

# example 1 : multiple and hirarchial inheritance

print(" ........ Exampl 1 .........")
class GParent:
    def m1(self):
        print("Grand Parent")

class Child1(GParent):
    def m2(self):
        print("child 1")

class Child2(GParent):
    def m3(self):
        print("child 2")

class Gchild(Child1,Child2):
    def m4(self):
        print("grand child")

g = Gchild()
g.m4()
g.m3()
g.m2()
g.m1()
print()



# example 2 : 
print(" ........ Exampl 2 .........")
class Grand_father:
    def __init__(self):
        self.gname = "Grand Parent"
        self.gage = 73
        print("GP")
    def m1(self):
        print(" grandfather details: ")
        print("name: ",self.gname)
        print("age: ",self.gage)


class mother(Grand_father):
    def __init__(self):
        super().__init__()         # Note
        self.mname = "mother"
        self.mage = 47
        print("M")
    def m2(self):
        print(" grandfather details: ")
        print("name: ",self.mname)
        print("age: ",self.mage)

class father(Grand_father):
    def __init__(self):
        super().__init__()          # Note
        self.fname = "father"
        self.fage = 53
        print("F")
    def m3(self):
        print(" grandfather details: ")
        print("name: ",self.fname)
        print("age: ",self.fage)

class son(mother,father):
    def __init__(self):
        super().__init__()          # Note
        self.sname = "Son"
        self.sage = 23
        print("S")
    def m4(self):
        print(" grandfather details: ")
        print("name: ",self.sname)
        print("age: ",self.sage)

# Note : to access the properties of parent class , we need to use super().__init__() in every child class
s = son()
s.m1()
s.m2()
s.m3()
s.m4()
print()

# MRO - method resolution order
print(" ........ MRO concept .........")
class a:
    def __init__(self,name) -> None:
        self.name = name
    def display(self):
        print("         ",self.name)

class b(a):
    def display1(self):
        print(self.name)

b1 = b("omkar")
b1.display()

# multiple

class A(object):
    def __init__(self) -> None:
        print("A")
        super().__init__()

class B:
    def __init__(self) -> None:
        print("B")

class C(A,B):
    def __init__(self) -> None:
        print("C")
        super().__init__()

c = C()

# view MRO
# child_class_name.__mro__
# child_class_name.mro()

print(C.__mro__)      # tuple form
print(C.mro())        # list form
print()


# example 3
# vehicle - car - racing car - xyz
print(" ........ Exampl 3 .........")
class Vehicle:
    def __init__(self, vehicletype) -> None:
        self.vehicle = vehicletype
        print("Vehicle")

class Car(Vehicle):
    def __init__(self,vehicletype,carname,Racing_type) -> None:
        super().__init__(vehicletype,Racing_type)
        self.carname = carname
        print("Car")

class Racing_car(Vehicle):
    def __init__(self, vehicletype, Racing_type) -> None:
        super().__init__(vehicletype)
        self.racingtype = Racing_type
        print("Racing")

class xyz(Car,Racing_car):
    def __init__(self, vehicletype, carname, Racing_type,carnumber) -> None:
        super().__init__(vehicletype, carname,Racing_type)
        self.carnumber = carnumber
        print("car Number")

    def display(self):
        print(f"1. {self.vehicle}")
        print(f"2. {self.carname}")
        print(f"3. {self.racingtype}")
        print(f"4. {self.carnumber}")

c = xyz("Highspeed vehicle","laborghini","F1 Racing","UGX 004")
c.display()
print(xyz.mro())
print()



# example 4
# university - course - branch - student
print(" ........ Exampl 4 .........")
class University:
    def __init__(self,univ_name) -> None:
        self.univ_name = univ_name

class Course(University):
    def __init__(self, univ_name, course,branch) -> None:
        super().__init__(univ_name,branch)
        self.course = course

class Branch(University):
    def __init__(self, univ_name,branch) -> None:
        super().__init__(univ_name)
        self.branch = branch

class Student(Course,Branch):
    def __init__(self, univ_name, course, branch,student_name) -> None:
        super().__init__(univ_name, course, branch)
        self.student = student_name

    def info(self):
        print("----student info-----")
        print("Student name: ",self.student)
        print("Course name: ",self.course)
        print("Branch name: ",self.branch)
        print("University name: ",self.univ_name)

s = Student("Mumbai-university","Engineering","Software developer","Student A")
print(Student.__mro__)
s.info()
print()
    
# example 5
# company - developer - tester - project
print(" ........ Exampl 5 .........")
class Company:
    def __init__(self) -> None:
        self.com_name = "xyz"
        self.com_location = "thane"
        self.tot_emp = 106
    def display(self):
        print("cpmpany details")
        print("company name: ",self.com_name)
        print("company locaton: ",self.com_location)
        print("company employee: ",self.tot_emp)

class developer(Company):
    def __init__(self) -> None:
        super().__init__()
        self.dev_name = "abc"
        self.dev_id = "d_123"
    def dev_display(self):
        print("developer details")
        print("developer name: ",self.dev_name)
        print("developer id: ",self.dev_id)

class tester(Company):
    def __init__(self) -> None:
        super().__init__()
        self.test_name = "jkl"
        self.test_id = "t_123"
    def test_display(self):
        print("tester details")
        print("tester name: ",self.test_name)
        print("tester id: ",self.test_id)
       
class Project(developer,tester):
    def __init__(self) -> None:
        super().__init__()
        self.project_name = "Project"

    def proj_display(self):
        print("Project name: ", self.project_name)
       
p = Project()
p.proj_display()
print()
p.test_display()
print()
p.dev_display()
print()
p.display()
print(Project.__mro__)
print()

# using parameterized constructor
print(" ........ Exampl 5 : using parameterized constructor.........")

class Company:
    def __init__(self,com_name,com_location,tot_emp) -> None:
        self.com_name = com_name
        self.com_location = com_location
        self.tot_emp = tot_emp
    def display(self):
        print("cpmpany details")
        print("company name: ",self.com_name)
        print("company locaton: ",self.com_location)
        print("company employee: ",self.tot_emp)

class developer(Company):
    def __init__(self, com_name, com_location, tot_emp,dev_name,dev_id,test_name,test_id) -> None:
        super().__init__(com_name, com_location, tot_emp,test_name,test_id)
        self.dev_name = dev_name
        self.dev_id = dev_id
    def dev_display(self):
        print("developer details")
        print("developer name: ",self.dev_name)
        print("developer id: ",self.dev_id)

class tester(Company):
    def __init__(self, com_name, com_location, tot_emp,test_name,test_id) -> None:
        super().__init__(com_name, com_location, tot_emp)
        self.test_name = test_name
        self.test_id = test_id
    def test_display(self):
        print("tester details")
        print("tester name: ",self.test_name)
        print("tester id: ",self.test_id)
       
class Project(developer,tester):
    def __init__(self, com_name, com_location, tot_emp, dev_name, dev_id, test_name, test_id,project_name) -> None:
        super().__init__(com_name, com_location, tot_emp, dev_name, dev_id, test_name, test_id)
        self.project_name = project_name

    def proj_display(self):
        print("Project name: ", self.project_name)
       
p = Project("Company","thane",106,"developer","dev-1","tester","test-1","new-project")
p.proj_display()
print()
p.test_display()
print()
p.dev_display()
print()
p.display()

