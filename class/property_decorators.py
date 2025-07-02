class Car:
    total_cars = 0

    def __init__(self,brand,model):
        self.__model = model
        self.__brand = brand
        Car.total_cars += 1
        # self.total_cars += 1

    def get_full_name(self):
        print(f"{self.__brand} {self.__model}")

    def get_brand(self):
        return self.__brand

    def get_fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def get_total_cars():
        return f"Total number of cars are {Car.total_cars}"

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def get_fuel_type(self):
        return "Electric charge"

tesla = ElectricCar("Tesla","Model S","85kWh")
# tesla.model = "Model L"
print(tesla.get_full_name())
print(tesla.get_fuel_type())
print(tesla.model)

toyota = Car("Toyota","Fortuner")
print(toyota.get_fuel_type())
print(isinstance(tesla,Car))