# single inheritance
# syntax:
'''
class parent_class_name:
    body
class child_class_name(parent_class_name):
    body

# to accesss
child_class_objext = child_class_name()

'''
class parent:
    def P_m(self):
        print("Inside Parent Class")
class child(parent):
    def C_m(self):
        print("Inside child class")

c = child()
c.P_m()
c.C_m()

# ex
class Person:
    def initi(abc,name,age):
        abc.name = name
        abc.age = age
class Student(Person):
    def __init__(abc,name,age,roll_no,std):
        # super().__init__()
        abc.r = roll_no
        abc.s = std
    def info(abc):
        print("Information of Student")
        print("Name: ", abc.name)
        print("Age : ",abc.age)
        print("Roll No : ",abc.r)
        print("Standard: ",abc.s)

s = Student("Python",14,10,9)
s.initi("Python",7)
s.info()

# in the above example we cannot access parent class values in child class using __init__

class Person:
    def __init__(abc,name,age):
        abc.name = name
        abc.age = age
class Student(Person):
    def __init__(abc,name,age,roll_no,std):
        super().__init__(name,age)
        abc.r = roll_no
        abc.s = std
    def info(abc):
        print("Information of Student")
        print("Name: ", abc.name)
        print("Age : ", abc.age)
        print("Roll No : ",abc.r)
        print("Standard: ",abc.s)

s = Student("Python",14,10,9)
s.info()
# super()
# super().__init__()
# super().__init__(p1_value,p2_value)

print(s.name)

n = s.name
print(n)

# var_name = var_value
s.name = 'Java'
print(s.name)

s.info()  # updated value of name
# del obj_name # object delete

m = Student("m",12,20,8) # create new class instance 
m.info()
print(m.s)
m.s = 9
m.info() # updated value of std

# del obj_name      # object delete
# del object_name.attrubute     # delete specified attribute of object

del m.s
# print(m.s)
# m.info()
# del m
# m.info()

# example 2

class Animal:
    def __init__(self,type) -> None:
        self.type = type
    
class Dog(Animal):
    def __init__(self, type,name,age,height,food) -> None:
        super().__init__(type)
        self.name = name
        self.age = age
        self.height = height
        self.food = food

    def display(self):
        print("--- Information of Dog ---")
        print("Type of Dog is:",self.type)
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Height is:",self.height)
        print("Dog eats",self.food)

dog1 = Dog("Labrador","Humpy","5 yrs",2.1,"Pedegree")
dog1.display()
