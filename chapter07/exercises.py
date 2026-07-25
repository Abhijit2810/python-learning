# 7.1
message = input('Name the car that you want to rent? ')
print(f'okay, lets check if there is a {message}.')

# 7.2
people = int(input("Hello, May I know how many people are here for dinner? "))
if people > 8:
    print('Sorry, we are currently full for the family table, could you please wait.')
else:
    print('Sure, Here is your table, Enjoy your meal')

# 7.3
num = int(input("Enter your number: "))
if num > 0 and num % 10 == 0:
    print(f'{num} is a multiple of 10')
else:
    print(f'{num} is not a multiple of 10')

# 7.4
message = 'Required toppings for your pizza,\n'
message += "Enter 'quit' if you don't have any: "
active = True
while active:
    text = input(message)
    if text == 'quit':
        active = False
    else:
        print(text)

# 7.5
age = int(input("Enter your age: "))
if age > 0:
    if age < 3:
        print('Congratulations!, you have free entry')
    elif 3 <= age < 12:
        print('Your ticket price is 10$')
    else:
        print('Your ticket price is 15$')
else:
    print('age cannot be negative')

# 7.6 already done in prev examples

# 7.7 - commenting whole exercise as this is infinite loop
# x = 1
# while x <= 5:
#     print(x)

# 7.8
orders_remaining = [11,12,13,16,19]
orders_remaining.sort(reverse=True)
orders_completed = [14,15,17,18]
print(f'Remaining orders : {orders_remaining}')
print(f'Orders completed : {orders_completed}')
while orders_remaining:
    order = orders_remaining.pop()
    print(f'Your order is done - {order}')
    orders_completed.append(order)

print('\nAll orders done')
print(f'Remaining orders : {orders_remaining}')
print(f'Orders completed : {sorted(orders_completed)}')

# 7.9
# issue with number 17
nums = [17, 11, 12, 17, 17, 13, 16, 19, 17]
print(nums)
while 17 in nums:
    nums.remove(17)
print(f"All 17's removed: {nums}")

# 7.10 already done
