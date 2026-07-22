# if else condition
cars = ['audi', 'bmw', 'mercedes', 'ford']
for car in cars:
    # if car = 'bmw': # this is wrong, as this is assigning, not checking
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

vehicle = 'audi'
print(vehicle == 'Audi')
# this gives false, there is difference between uppercase and lowercase

# we can convert if we want - this results true
print(vehicle.title() == 'Audi')

# not equal too
toppings = ['olives', 'onions', 'capsicum', 'corn', 'mushrooms']
for top in toppings:
    if top != 'mushrooms':
        print(f'Add {top} in the pizza.')

# number equality
age,num = 18,18
print(age == num)
print(age is num)

# not equal to
given = 15 # we can also take this from user like below, but its not yet introduced, so not taking
# given = int(input('Enter your answer : '))
answer = 20
if given != answer:
    print('Wrong answer!')
else:
    print('Correct answer!')

# number conditionals
num = 19
print(num>10)
print(num<10)
print(num==10)
# can check <= or >= too

# multiple True conditions
Indian = -1 # everything other than 0 is considered true, even negative numbers too
# putting -1 also runs the code, as it considers true
age = 20
if (age >= 18) and Indian:
    print("Eligible for indian driving license")
else:
    print('Not eligible')

# or condition
Indian_voter_id = False
age = 18
if (age >= 18) or Indian_voter_id:
    print("Eligible for driving license")
else:
    print('Not eligible')

# using in and not in
toppings = ['nuts', 'berries', 'choco syrup']
print('nuts' in toppings)
print('choco chips' in toppings)
if 'choco chips' not in toppings:
    toppings.append('choco chips')
print(toppings)

# Basic voting
age = 17 # can be user input too, not taught yet, so not taking, i know how to take user input
if age >= 18:
    print('You are eligible to vote.')
    print('Have you casted your vote?')
else:
    print('Sorry you are not eligible to vote.')
    print('Please register as soon as you turn 18.')

# Ticketing prices - if elif else
age = 75 # again user input can be taken
if age <= 10:
    print('Child Ticket Price')
elif age >= 60:
    print('Senior Citizen ticket')
else:
    print('Adult ticket')

# using variables
age = 18 # again can be user
if age <= 4:
    price = 0
elif age > 60:
    price = 10
else:
    price = 20
print(f"The price for your age {age} is {price}")

# checking all conditions
pizza_tops = ['corn', 'cheese', 'olives']
if 'corn' in pizza_tops:
    print('Adding corn')
if 'olives' in pizza_tops:
    print('Adding olives')
# these check every statement, not exiting when one is satisfied.



