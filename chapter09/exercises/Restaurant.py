class Restaurant:
    def __init__(self, name, cuisine_type):
        self.hotel_name = name
        self.cuisine = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        print(self.hotel_name, self.cuisine)

    def set_number_served(self):
        print(f'Number of customers served are {self.served}')

    def increment_number_served(self, increment):
        self.served += increment
        print(f'Number of Customers served is {self.served}')

    def open_restaurant(self):
        print(f'{self.hotel_name} Restaurant is open.')