from car_details import Car

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