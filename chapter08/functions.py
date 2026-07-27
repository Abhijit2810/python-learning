# greeter function
def greeter(user):
    print(f'Hello {user.title()}.')


greeter('Abhijit')


# greeter() this raises an error, as this an argument and we are not providing it


# args in functions
def animal_name(pet_type='dog', pet_name='snoopy'):
    print(f"I have a {pet_type}, the {pet_type}'s name is {pet_name.title()}.")


animal_name('dog', 'chintu bhai')
animal_name('cat', 'tom')
animal_name('mouse', 'jerry')
# animal_name('jerry', 'mouse') - this doesnt give any errors but changes the meaning of output, so,order matters.

animal_name(pet_name='Nandini', pet_type='Cow')
animal_name(pet_type='Cow', pet_name='Nandini')
# in this case order doesnt matter, as we are explictly assigning values to the arguments

animal_name()  # in this case, no arguments are passed, so it takes default values and processes it


# functions with return
def get_formatted(first_name, last_name, middle_name=''):
    if middle_name:
        result = f'{first_name} {middle_name} {last_name}'
        return result.title()
    else:
        result = f'{first_name} {last_name}'
        return result.title()


name = get_formatted('kollampally abhijit', 'joshi')
print(name)


# returning dict
def name_dict(first_name='', last_name='', middle_name='', age=None):
    if middle_name:
        result = {'first': first_name.title(), 'middle': middle_name.title(), 'last': last_name.title(), 'age': age}
        return result
    else:
        result = result = {'first': first_name.title(), 'last': last_name.title(), 'age': age}
        return result


name = name_dict('kollampally abhijit', 'joshi', age=21)
print(name)

# using while loops
names = True


# while names:
#     print('Details of your name: \n')
#     print('enter "q" in first_name to quit the loop')
#     middle_name = int(input("Before that, do you have a middle name (0 for False, anything else True): "))
#     first = input('Enter your first name: ')
#     if first == 'q':
#         names = False
#         break
#     last = input('Enter your last name: ')
#     middle = ''
#     if middle_name:
#         middle = input('Enter your middle name: ')
#     name_formatted = get_formatted(first, last, middle)
#     print(name_formatted)


# passing list in function
def greet_users(users):
    for user in users:
        message = f'Hello {user.title()}!'
        print(message)


users = ['abhijit', 'joshi', 'kollampally']
# greet_users(users) - changes made in users list in permanent here
greet_users(users[:])


# remember, list is directly passed as reference, not a copy, so any changes made are permanent
# to send a copy, it's better to do list_name[:]


# unknown number of inputs
def pizza_toppings(size, *tops):
    # print(type(tops)) its a tuple
    print(f'Adding toppings for your {size}-inch pizza:')
    for top in tops:
        print(top)
    print('Pizza Ready!\n')


# pizza_toppings(12,'cheese')
# pizza_toppings(16, 'corn', 'cheese', 'olives', 'paneer', 'capsicum')


# using arbitrary args
def user_info(first, last, **info_user):
    info_user['first_name'] = first.title()
    info_user['last_name'] = last.title()
    return info_user


print(user_info('albert', 'einstein', location='Princeton', field='physics'))

# importing module
# import pizza
# print('\nPizza module imported!')
# pizza.pizza_toppings(12, 'cheese')
# pizza.pizza_toppings(16, 'corn', 'cheese', 'olives', 'paneer', 'capsicum')

# importing function from a module
# from pizza import pizza_toppings
# print('\nFunction pizza_toppings from Pizza module imported!')
# pizza_toppings(12, 'cheese')
# pizza_toppings(16, 'corn', 'cheese', 'olives', 'paneer', 'capsicum')

# making aliases for functions
from pizza import pizza_toppings as pt
print('\nFunction pizza_toppings from Pizza module imported and aliased!')
pt(12, 'cheese')
pt(16, 'corn', 'cheese', 'olives', 'paneer', 'capsicum')

# importing every function from module
from pizza import *
# this imports every function from pizza




