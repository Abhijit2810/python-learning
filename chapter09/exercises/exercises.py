# 9.1, 9.10
from Restaurant import Restaurant
from user_and_admin import User, Admin
from random import randint, choice

# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.hotel_name = name
#         self.cuisine = cuisine_type
#         self.served = 0
#
#     def describe_restaurant(self):
#         print(self.hotel_name, self.cuisine)
#
#     def set_number_served(self):
#         print(f'Number of customers served are {self.served}')
#
#     def increment_number_served(self, increment):
#         self.served += increment
#         print(f'Number of Customers served is {self.served}')
#
#     def open_restaurant(self):
#         print(f'{self.hotel_name} Restaurant is open.')


restaurant = Restaurant('Mehfil', 'South_Indian')
print(restaurant.hotel_name, restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2
restaurant1 = Restaurant('Bawarchi', 'North Indian')
restaurant2 = Restaurant('Shadab', 'South Indian')
restaurant3 = Restaurant('Paradise', 'Continental')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9.3
# class User:
#     def __init__(self, first_name, last_name, **kwargs):
#         self.first = first_name
#         self.last = last_name
#         self.years = kwargs.get('age')
#         self.college = kwargs.get('university')
#         self.location = kwargs.get('Area')
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f'{self.first}, {self.last}, {self.years}, {self.college}, {self.location}')
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         print(f'Login attempts : {self.login_attempts}')
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print(f'Login attempts reset : {self.login_attempts}')
#
#     def greet_user(self):
#         print(f'Hello {self.first} {self.last}')


user1 = User('Abhijit', 'Joshi', age=21, university='ISI')
user2 = User('Kollampally', 'Abhijit', age=22)
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

# 9.4
restaurant4 = Restaurant('Balaji', 'All Indian')
restaurant4.served = 500
# print(restaurant4.served)
restaurant4.set_number_served()
restaurant4.increment_number_served(100)

# 9.5
user3 = User('Tom', 'Holland', age=23)
for i in range(10):
    user3.increment_login_attempts()
user3.reset_login_attempts()


# 9.6
class Icecream(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = ['mango', 'butterscotch', 'chocolate', 'vanilla']

    def display_flavours(self):
        print(f'Available flavours are:\n{self.flavours}')


ice_cream = Icecream('Baskin Robins', 'Bakers')
ice_cream.display_flavours()

# 9.7
# class Privileges:
#     def __init__(self):
#         self.available_privileges = ['can post', 'can delete', 'can ban', 'can remove']
#
#     def show_privileges(self):
#         print(f'The privileges available for admin are\n{self.available_privileges}')
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, **kwargs):
#         super().__init__(first_name, last_name, **kwargs)
#         self.privileges = Privileges()


# admin1 = Admin('Abhijit', 'Joshi', age=21)
# admin1.show_privileges()

# 9.8, 9.11, 9.12
admin1 = Admin('Abhijit', 'Joshi', age=21)
admin1.privileges.show_privileges()


# 9.9 - done


# 9.13
class Dice:
    def __init__(self, sides=6):
        self.num_sides = sides

    def roll_dice(self):
        return randint(1, self.num_sides)


# dice_int = Dice(6)
# for i in range(10):
#     print(dice_int.roll_dice())

# dice_10 = Dice(10)
# for i in range(10):
#     print(dice_10.roll_dice())

dice_20 = Dice(20)
for i in range(10):
    print(dice_20.roll_dice())

# 9.14, 9.15
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
print('4 lucky winners are:')
for i in range(4):
    print(choice(lottery))
