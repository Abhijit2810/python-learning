from car_details import Car as C
from electric_car_details import ElectricCar as EC

# my_mustang = Car('Ford', 'Mustang', 2025)
my_mustang = C('Ford', 'Mustang', 2025)
print(my_mustang.description())
my_mustang.update_odometer(500)
my_mustang.odometer_read()

# my_electric_car = ElectricCar('BMW', 'M340i', 2025)
my_electric_car = EC('BMW', 'M340i', 2025)
print(my_electric_car.description())
my_electric_car.battery_description.describe_battery()
my_electric_car.battery_description.get_range()