from car import Car
from eletric_car import ElectricCar as ec

my_car = Car("Toyota", "Hillux", "2020")
print(my_car.get_descriptive_name())

my_ecar = ec("Tesla", "i20", "2020")

my_car.update_odometer(23)
my_car.read_odometer()