#5.1
car = 'subaru'
print("is car=='subaru' ? I predict True")
print(car == 'subaru')

print("is car='audi'? I predict False")
print(car == 'audi')

# 5.2
car = 'BMW'
print(car == 'bmw')
print(car.lower() == 'bmw')

num = 15
print(num >= 10)
print(num < 10)

# 5.3
alien_color = 'yellow'
if alien_color == 'green':
    print('player earned 5 points')

# 5.4
if alien_color == 'green':
    print('player earned 5 points')
else:
    print('Player earned 10 points')

# 5.5
if alien_color == 'green':
    print('player earned 5 points')
elif alien_color == 'red':
    print('player earned 10 points')
else:
    print('Player earned 15 points')

# 5.6
# age = int(input('Enter age of person : ')) not doing this, as not taught yet
age = 54
if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('toddler')
elif 4 <= age < 13:
    print('kid')
elif 13 <= age < 20:
    print('teenager')
elif 20 <= age < 65:
    print('Adult')
else:
    print('Elder')

# 5.7
fruits = ['mango', 'pineapple', 'watermelon']
if 'mango' in fruits:
    print("Yeah!")
if 'guava' in fruits:
    print("Yes")
if 'pineapple' in fruits:
    print('Yes, it is')

# 5.8
users = ['Admin', 'Abhi', 'Joshi', 'Kollampally']
for user in users:
    if user == 'Admin':
        print(f'Hello {user}, would you like a status report?')
    else:
        print(f'Hello {user}, Welcome back!')

# 5.9
# users=[]
if users:
    for user in users:
        if user == 'Admin':
            print(f'Hello {user}, would you like a status report?')
        else:
            print(f'Hello {user}, Welcome back!')
else:
    print('We need to find some users.')

# 5.10
new_users = ['Adam', 'Eve', 'Abhi', 'Joshi', 'Peter']
for user in new_users:
    if user in users:
        print(f'The username {user} is already in use, please try another username.')
    else:
        print(f'Username {user} is available')

# 5.11
nums = list(range(1,10))
for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')

# 5.12