# OOP concepts
# inheritance : use to reuse the data again and again

# class - parent/base class
# class1 - child/sub class

# Types of inheritance 
# single
# multi-level : ex. grandfather - father - child
# multiple 
# hirerachial
# hyrbrid 

# single inheritance
# syntax:
'''
class parent_class_name:
    body
class child_class_name(parent_class_name):
    body

# to accesss
child_class_object = child_class_name()

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
        print("Age : ",abc.age)
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

# multiple inheritance
'''
class parent1:
    body
class parent2:
    body
class child(parent1,parent2):
    body
'''
class mother:
    def m(self,m_name):
        self.m_name = m_name
        print(self.m_name)
class father:
    def f(self,f_name):
        self.f_name = f_name
        print(self.f_name)
class child(father,mother):
    def c(self,c_name):
        self.c_name = c_name
        print(self.c_name)

    def name(self):
        print(self.f_name,self.m_name,self.c_name)

ch = child()
ch.c("Python")
ch.f("Programming")
ch.m("Language")
ch.name()

ch1 = child()
ch1.c("Java")
ch1.f("Programming")
ch1.m("Language")
ch1.name()


# 3 multilevel inheritance

# grandparent - parent - child
class G_parent:
    def __init__(self,grandparent):
        self.grandparent = grandparent
        print("grandparent")
    
class parent(G_parent):
    def __init__(self,parent_name,grandparent):
        super().__init__(grandparent)
        self.parent_name = parent_name
        print("parent")

class child(parent):
    def __init__(self,child_name,parent_name,grandparent):
        super().__init__(parent_name,grandparent)
        self.child_name = child_name
        print("child")

    def show(self):
        print("-----ended------")

c = child("Python","Programming","Language")
c.show()
# c.show1()
# c.show2()


class user:
    def __init__(self,name,age,location) -> None:
        self.name = name
        self.age = age
        self.location = location

    def show_user_info(self):
        print("--- Details of user ---")
        print("Name is: ",self.name)
        print("Age is: ", self.age)
        print("Location is: ",self.location)

# python = user("Python",30,"Memory")
# python.show_user_info()

class update_user(user):
    def __init__(self, name, age, location) -> None:
        super().__init__(name, age, location)

    def update_user_info(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
        print(" --- Details updated ---")

# python = update_user("Python",310,"Memory")
# python.show_user_info()
# print()
# python.update_user_info("Python",30,"language")
# python.show_user_info()

class Add_info(update_user):
    def __init__(self,name,age,location):
        super().__init__(name,age,location)

    def add_user_info(self,contact,qualification):
        self.contact = contact
        self.qualification = qualification

    def show_all_info(self):
        super().show_user_info()
        print("Contact number: ",self.contact)
        print("qualification: ",self.qualification)

python = Add_info("python","78","mumbai")
python.show_user_info()
print()
python.add_user_info("9999999999","HSC")
python.show_all_info()
print()
python.update_user_info("python",34,"Thane")
python.show_all_info()


