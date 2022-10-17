class CarCompany:
    def method1(self, car_company):
        self.car_company = car_company
        print(self.car_company)

class VehicleType:
    def method2(self, veh_type):
        self.typ = veh_type
        print(self.typ)

class TouristCar(CarCompany,VehicleType):
    def method3(self,c_name):
        self.c_name = c_name
        print(self.c_name)

    def details_of_car(self):
        print(" --- Details of Car --- ")
        print("Company name: ",self.c_name)
        print("Vehicle Type: ",self.typ)
        print("Car name: ",self.c_name)

c1 = TouristCar()
c1.method3("Ertiga")
c1.method2("Four Wheeler")
c1.method1("Suzuki")
c1.details_of_car()
