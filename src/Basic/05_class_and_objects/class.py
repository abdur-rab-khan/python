class Car:
    def __init__(self,model,brand):
        self.model = model
        self.__brand = brand

    def get_full_name(self):
        print(f"{self.__brand} {self.model}")

    def get_brand(self):
        return self.__brand

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


toyota = Car("Toyota","Fortuner")
my_tesla = ElectricCar("S 2","Tesla","85Kwh")

print(my_tesla.get_brand())

# toyota.get_full_name()
# my_tesla.get_full_name()
