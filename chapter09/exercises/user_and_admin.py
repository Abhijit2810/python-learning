class User:
    def __init__(self, first_name, last_name, **kwargs):
        self.first = first_name
        self.last = last_name
        self.years = kwargs.get('age')
        self.college = kwargs.get('university')
        self.location = kwargs.get('Area')
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first}, {self.last}, {self.years}, {self.college}, {self.location}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Login attempts : {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Login attempts reset : {self.login_attempts}')

    def greet_user(self):
        print(f'Hello {self.first} {self.last}')


class Privileges:
    def __init__(self):
        self.available_privileges = ['can post', 'can delete', 'can ban', 'can remove']

    def show_privileges(self):
        print(f'The privileges available for admin are\n{self.available_privileges}')

class Admin(User):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges()