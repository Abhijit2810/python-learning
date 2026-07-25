message = input('Tell me something, and i will repeat it to you: ')
print(message)

# greeting
prompt = "Hello!, Nice to meet you! "
prompt += "\n What's your name? "
text = input(prompt)
print(f'Hi {text}')

# int input
age = int(input('Enter your age? '))
print(f'You are {age} years old')
# here everything looks correct, but it isnt, here age is not considered as number, its considered as string.
print(type(age)) # this gives you class str if we dont add int in the input

# conditionals
age = int(input('Enter your age: '))
if age >= 18:
    print('You are eligible to vote')
else:
    print('You are below 18 years')

# Modulo operator - It outputs remainder of the division
print(5%3)

# even, odd
num = int(input('Enter the number: '))
if num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

# while loop
num = 1
while num <= 5:
    print(num)
    num += 1

# while and input
message = 'Tell me something and i will repeat for you:,\n'
message += "Enter 'quit' for the process to complete\n"
text = ''
while text != 'quit':
    text = input(message)
    if text != 'quit':
        print(text)

# Using flags
message = 'Tell me something and i will repeat for you:,\n'
message += "Enter 'quit' for the process to complete\n"
active = True
while active:
    text = input(message)
    if text == 'quit':
        active = False
    else:
        print(text)

# using break
message = 'Tell me something and i will repeat for you:,\n'
message += "Enter 'quit' for the process to complete\n"
while True:
    text = input(message)
    if text == 'quit':
        break
    else:
        print(text)

# print odd nums using continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)

# lists and while loops
unconfirmed_users = ['abhi', 'joshi', 'kollampally']
confirmed_users = []
while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f'Validating user : {user}')
    confirmed_users.append(user.title())
print(sorted(confirmed_users))

# removing using while
nums = [10,54,67,23,78,54,12,65]
print(nums)
while 54 in nums:
    nums.remove(54)
print(nums)

# adding items in dictionary
users = {}
flag = True
while flag:
    name = input('Enter your name: ')
    age = int(input('Enter your age( greater than 0): '))
    users[name] = age
    add_user = input("Add another user? (yes/no): ")
    if add_user == 'no':
        flag = False
print(users)


