# hierarchial inheritance

class Parent:
    def __init__(self, pname):
        self.name = pname

class Child1(Parent):
    def c1(self, c1name):
        print("Name is:",c1name)
        print("Parent name:",self.name)

class Child2(Parent):
    def __init__(self, pname,c2name):
        super().__init__(pname)
        self.c2name = c2name

    def display(self):
        print("Parent name:",self.name)
        print("Child name:",self.c2name)

java = Child1("programming")
java.c1("Language")
print()
python = Child2("programming","language")
python.display()
        
# examples
# person - student, employee, doctor, engineer
# vehicle = car, truck, auto
# school = squad, abc, xyz

# Example 2
class Person:
    def __init__(self,name,age,contact,location,email):
        self.name = name
        self.age = age
        self.contact = contact
        self.location = location
        self.email = email

    # display common methods 

    def per_info(self):
        print("Name :",self.name)
        print("Age is:",self.age)
        print("Contact Number:",self.contact)
        print("Location is",self.location)
        print("Email Id is:",self.email)

class Student(Person):
    def __init__(self, name, age, contact, location, email,schoolname,std):
        super().__init__(name, age, contact, location, email)
        self.schoolname = schoolname
        self.std = std

    def std_info(self):
        print(" ---- student details ---- ")
        super().per_info()
        print("School Name is:",self.schoolname)
        print("Std is:", self.std)

class Employee(Person):
    def __init__(self, name, age, contact, location, email,empid,department):
        super().__init__(name, age, contact, location, email)
        self.empid = empid
        self.department = department

    def emp_info(self):
        print(" ---- Employee Details ---- ")
        super().per_info()
        print("Employee ID:",self.empid)
        print("Employee Department:", self.department)

python = Student("Python",15,'9999999999',"Thane","python.org","Squad","1")
python.std_info()

print("----------------------------------")

java = Employee("Java",15,'99000099999',"Thane","python.org","Squad","2")
java.emp_info()

print()
# Example 3 : vehicle = car, truck, auto

class Vehicle:
    def __init__(self,type,wheels,seats,airbags,fueltype) -> None:
        self.type = type
        self.wheels = wheels
        self.seats = seats
        self.airbags = airbags
        self.fueltype = fueltype

    def veh_info(self):
        print("Type of vehicle:",self.type)
        print("No of wheels:",self.wheels)
        print("no of seats:",self.seats)
        print("No. of airbags:",self.airbags)
        print("Fuel Type:",self.fueltype)

class Hatchbag(Vehicle):
    def __init__(self, type, wheels, seats, airbags, fueltype,average) -> None:
        super().__init__(type, wheels, seats, airbags, fueltype) 
        self.average = average

    def hatch_info(self):
        super().veh_info()
        print("Average:",self.average)

class SUV(Vehicle):
    def __init__(self, type, wheels, seats, airbags, fueltype,groundclearance) -> None:
        super().__init__(type, wheels, seats, airbags, fueltype)
        self.clearance = groundclearance

    def suv_info(self):
        super().veh_info()
        print("Ground clearance:",self.clearance)


swift = Hatchbag("car","Four","5 seater",4,"Petrol","25 kmpl")
swift.hatch_info()

print()

scorpio = SUV("Jeep","Four","9 Seater",6,"Diesel",180)
scorpio.suv_info()
    

# example 4 : school = squad, abc, xyz

class School:
    def __init__(self,schoolname,location,board,standardsupto,medium):
        self.schoolname = schoolname
        self.lcoation = location
        self.board = board
        self.standardsupto = standardsupto
        self.medium = medium

    def school_info(self):
        print(" [--- Details of school --- ]")
        print("School name:-",self.schoolname)
        print("Location of school:",self.lcoation)
        print(f"School belongs to {self.board} board")
        print("School medium is:",self.medium)

class ZP(School):
    def __init__(self, schoolname, location, board, standardsupto, medium,ishighschool,multilanguage):
        super().__init__(schoolname, location, board, standardsupto, medium)
        self.ishighschool = ishighschool
        self.multilanguage = multilanguage

    def ZP_school_info(self):
        super().school_info()
        print("School has highschool ?",self.ishighschool)
        print("School has muultilanguage ?",self.multilanguage)

class DB(School):
    def __init__(self, schoolname, location, board, standardsupto, medium,isinternational,fees):
        super().__init__(schoolname, location, board, standardsupto, medium)
        self.isinternational = isinternational
        self.fees = fees

    def DB_school_info(self):
        super().school_info()
        print("School is international ?",self.isinternational)
        print("School fees ?",self.fees)

s1 = ZP("Bhavika vidyalay","kharegaon","maharashtra","10th","marathi","No","No")
s1.school_info()
s1.ZP_school_info()

s2 = DB("ST.JOHN","THANE","DELHI","10th","CONVENT","YES","75000")
s2.school_info()
s2.DB_school_info()



