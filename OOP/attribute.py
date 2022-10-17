'''
what is attributes ?
attribute is nothing but a variable in oops
attributes are responsible for behavious of the method of the class

Types of attributes are
1. Instnace attributes
2. local attributes
3. class attributes or static attribute
4. global attributes
'''
# Instance is object
#1. Instance attribute
#
# define, access, update, delete
# self.attribute_name = value (inside the class)
# instance_name.attribute_name = value (outside the class)

class person:
    def __init__(self,name) -> None:
        self.n = name       # defining an instance attribute

    def display(self):
        print("Person name: ", self.n)   # accessing instance attribute

    def update(self,name):
        # variable_name = value
        # variable_name - new_value
        self.n = name
        print("updated successfully")

    def add(self,location):
        self.loc = location 
        print("Add successfully")

manisha = person("Manisha")
manisha.display()
manisha.update("Manisha jadhav")
manisha.display()
print()
pooja = person("Pooja")
pooja.display()

# accessing instance attribute outside the class without self
print(pooja.n)
print(manisha.n)

# updating instance attribute
pooja.n = "pooja saste"
pooja.display()

# adding new instance attribute to object'
pooja.age = 25
print(pooja.age)
manisha.age = 29
print(manisha.age)

# self
pooja.add("Mumbai")
print(pooja.loc)

manisha.add("Navi mumbai")
print(manisha.loc)
print()


#2. local attribute
class person:
    def __init__(self,name):
        global na 
        na = name

    def display(self):
        print("person name: ", na)
    
    def update(self):
        global na
        na = "Python"

manisha = person("Manisha")
manisha.display()

pooja = person("Pooja")
pooja.display()

manisha.update()
manisha.display()
print()

'''
#3. class attribute or static attribute

# statis attributes are defined inside the class and outside the method
# we can access statis attribute by using 
# 1. self(inside the method)
# 2. oject name (outside the class)
# 3. using class name (inside and outside)
# 4. and we can directly access statis or class attribute
class person:
    salary = 10000    # static attribute
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)
        print(salary)

p = person("Python")
p.display()
'''
class student:
    school_name = "google"  
    print(school_name)
    def __init__(self,name,roll_no )-> None:
        self.name = name
        self.roll_no = roll_no
        
    def info(self):
        print("student info")
        print("Name is: ",self.name)
        print("roll no",self.roll_no)
        print("using self: ", self.school_name)    # using self
        print("using class: ", student.school_name)   # using class name

class s1(student):
    def info(self):
        super().info()
        print(student.school_name)
        print(self.school_name)


s = s1("abc",88)
s.info()
# print(school_name)
# print(self.school_name)
print(student.school_name)    # access using base class name
s1 = student("omkar",1)
s1.info()
print()

s2 = student("pooja",2)
s2.info()
print()

# updating static attribute
student.school_name = "Google chrome"
s1.info()
s2.info()

# by using object name
s1.school_name = "update by object"
s1.info()

'''
#4. global attribute

company_name = "Squad"
class person:
    print(company_name)
    def __init__(self,name) -> None:
        self.name = name
    def display(self):
        print(self.name)
        print(company_name)

p = person("Python")
p.display()

'''
salary = 20000
print(salary)
# global attriubute an access anywhere
class Employee:
    def __init__(self,name,age) -> None:
        self.name = name # instance attributes
        self.age = age

    def display(self):
        print("1. name :",self.name)
        print("2. age :",self.age)
        print("3. Salary :",salary)  # accessing global attribute
        

    def update_sal(self,sal):
        global salary      # decclare as a global inside local scope of method
        salary = sal
e1 = Employee("Python",34)
e2 = Employee("java",67)
e1.display()
print()
e2.display()
print()

e3 = Employee("pooja",20)
e3.update_sal(35000)
e3.display()
print()
e2.display()
print(salary)
# del salary
salary = 67000   # update outside the class
print(salary)











