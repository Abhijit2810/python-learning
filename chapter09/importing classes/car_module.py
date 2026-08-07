""" A class that can be used to represent a car"""

class Car:
    def __init__(self, make, model, year):
        self.car_company = make
        self.car_model = model
        self.manufacture_year = year
        self.odometer_reading = 30
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


class Battery:
    def __init__(self, battery_size=40):
        self.battery = battery_size

    def describe_battery(self):
        print(f'This car has a battery size of {self.battery}-KWH')

    def get_range(self, range_kms=0):
        if self.battery == 40:
            range_kms = 150
        elif self.battery == 65:
            range_kms = 225
        print(f'The car has a range of {range_kms} on full charge')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_description = Battery()
