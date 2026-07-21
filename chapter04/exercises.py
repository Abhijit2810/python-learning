# 4.1
pizza = ['cheese', 'corn', 'margherita', 'farmhouse']
for fav in pizza:
    print(fav)
    print(f"Its a {fav} pizza\n")

print('I really dont like pizza afterall, its just that i dont have other options to eat\n')


# 4.2
animals = ['cat', 'tiger', 'cheetah', 'leopard', 'lion']
for animal in animals:
    print(f"A {animal} is a wild animal")

print('All these animals are 4-legged omnivores')

# 4.3
for num in range(1,21):
    print(num)

# 4.4
run = int(input("Your permission for printing upto 1M : "))
if run:
    for num in range(1,1000001):
        print(num)

# 4.5 - can take large space so just commenting
# numbers = list(range(1,1000001))
# print(f'The min of 1M is {min(numbers)}')
# print(f'The max of 1M is {max(numbers)}')
# print(f'The sum of 1M is {sum(numbers)}')

# 4.6
print('Odd numbers upto 20 are \n')
for num in range(1,20,2):
    print(num)

# 4.7
muls_3 = list(range(3,31,3))
print(muls_3)

# 4.8
for num in range(1,11):
    print(f'The cube of {num} is {num**3}')

# 4.9
cubes = [value**3 for value in range(1,11)]
print(cubes)

# 4.10
print(f'The first 4 muls of 3 are {muls_3[:4]}')
print(f'The middle 3 muls of 3 are {muls_3[4:7]}')
print(f'The last 3 muls of 3 are {muls_3[7:]}')

# 4.11
friend_pizza = pizza[:]
pizza.append('peppy paneer')
friend_pizza.append('veggie max')
print(pizza)
print(friend_pizza)

# 4.12
num=1
for pizza_name in pizza:
    print(f"{pizza_name} pizza is number {num}")
    num=num+1

# 4.13
menu = ('idli', 'dosa', 'vada', 'puri', 'upma')
for item in menu:
    print(item)

# menu[3] = 'pulav'
# menu[4] = 'mini-idli', this cant be done, as tuples are immutable, raises error

menu_updated = ('idli', 'dosa', 'vada', 'pulav', 'mini-idli')
for item in menu_updated:
    print(item)

