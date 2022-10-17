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



# example 3

class car:
    def __init__(self,carname,company):
        self.carname = carname
        self.company = company

    def carinfo(self):
        print("--- Details of car ---")
        print("Car Name:",self.carname)
        print("Company:",self.company)

class Update_info(car):
    def __init__(self, carname, company):
        super().__init__(carname, company)

    def update_car_info(self,carname,company):
        self.carname = carname
        self.company = company
        print("--- details are updated ---")

class Add_info(Update_info):
    def __init__(self, carname, company):
        super().__init__(carname, company)

    def add_car_info(self,mfgyear,fuel):
        self.mfgyear = mfgyear
        self.fuel = fuel

    def carinfo_all(self):
        super().carinfo()
        print("Manufacturing Year:",self.mfgyear)
        print("Fuel Type:",self.fuel)






car1 = car("Ertiga","Suzuki")
car1.carinfo()

car1 = Update_info("Ertiga","Suzuki")
car1.update_car_info("Scorpio","Mahindra")
car1.carinfo()

car1 = Add_info("Scorpio","Mahindra")
car1.add_car_info("2019","Diesel")
car1.carinfo_all()

car1.update_car_info("classic 350","Royal Enfield")
car1.add_car_info("2018","Petrol")
car1.carinfo_all()




