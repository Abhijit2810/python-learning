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