# Importing classes

# from car_module import Car, ElectricCar, Battery
from car_module import *

my_car = Car('Audi', 'A8', 2025)
print(my_car.description())
my_car.odometer_reading = 100
my_car.odometer_read()

my_new_car = ElectricCar('MG', 'Hector', 2023)
print(my_new_car.description())
my_new_car.battery_description.describe_battery()
my_new_car.battery_description.get_range()

# Another way
# import car_module
# my_car = car_module.Car('Audi', 'A8', 2025)
# print(my_car.description())
# my_car.odometer_reading = 100
# my_car.odometer_read()
#
# my_new_car = car_module.ElectricCar('MG', 'Hector', 2023)
# print(my_new_car.description())
# my_new_car.battery_description.describe_battery()
# my_new_car.battery_description.get_range()