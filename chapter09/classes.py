# Creating a class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} rolled over!')


# Here we know 2 things are common to any dog, that is name and age, and we know that there are 2 properties which
# are held for any dog, that is it can sit and it can rollover, so we defined those in the class

my_dog = Dog('Max', 6)
print(my_dog.name, my_dog.age)
# accessing methods from class
my_dog.sit()
my_dog.roll_over()

# we can create multiple instances of the class
your_dog = Dog('Rocky', 5)
print(your_dog.name, your_dog.age)
your_dog.sit()
your_dog.roll_over()


# Working with classes and instances
class Car:
    def __init__(self, make, model, year):
        self.car_company = make
        self.car_model = model
        self.manufacture_year = year
        self.odometer_reading = 0

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


my_new_car = Car('bmw', 'm4', 2024)
print(my_new_car.description())

# But odometer is variable which changes with time, so we need to update the variable odometer reading
# there are 3 ways to update a variable
# First is directly through accessing variable from instance

my_new_car.odometer_reading = 23
my_new_car.odometer_read()

# here we see after we update the variable for the instance, we get the updated details
my_new_car.update_odometer(67)
my_new_car.odometer_read()

# adding a particular value to a variable in instance
my_new_car.increment_odometer(100)
my_new_car.odometer_read()








