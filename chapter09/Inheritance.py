class Car:
    def __init__(self, make, model, year):
        self.car_company = make
        self.car_model = model
        self.manufacture_year = year
        self.odometer_reading = 0
        self.fuel = 50

    def description(self):
        return f'{self.car_company.title()} {self.car_model.title()} {self.manufacture_year}'

    def odometer_read(self):
        print(f'The car has {self.odometer_reading} kms on it.')

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
            return mileage
        else:
            print('Odometer cant be over rolled')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fuel_capacity(self):
        print(f'The fuel capacity of the car is {self.fuel}')


# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        print(f'This {self.car_company} {self.car_model} car has a battery of size {self.battery_size}-KWH')

    def fuel_capacity(self):
        print('Electric cars dont run on fuel.')


fuel_car = Car('Audi', 'A8', 2026)
# here we get the fuel capacity because it is described in the overall class Car
fuel_car.fuel_capacity()


my_car = ElectricCar('Nissan', 'leaf', 2024)
print(my_car.description())
my_car.describe_battery()
# here we overrode the method fuel capacity as electric cars dont have them
my_car.fuel_capacity()




