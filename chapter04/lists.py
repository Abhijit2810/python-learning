# looping in lists
names = ['Kollampally', 'Abhijit', 'Joshi', 'Abhi']
for name in names:
# print(name) This gives indentation error, as var name is defined inside loop, so it expects indentation
    print(name)

# can do with strings too
for var in names[0]:
    print(var)

# looping
for invitee in names:
    print(f"Hi {invitee.upper()}, Welcome to the party!")
    # can add multiple statements too
    print(f"The party is at 8.00pm, see you there,{invitee}.\n")

# any code outside intendation of for loop only runs once
print('Thank you all for joining the party.')

# Nesting loops
for name in names:
    for letter in name:
        print(letter)

message = 'Hi'
    # print(message) this gives error, because we have given an unnecessary indent
print(message)

# for alpha in message
#     print(alpha), it raises indentation error, as : is missing

# range() function - has 3 inputs (start, end, jump)
for num in range(5):
    print(num)
for num in range(1,5):
    print(num)
for num in range(1,5,2):
    print(num)

# Making list of numbers
nums = list(range(1,6))
print(nums)

# even nums list
nums = list(range(0,11,2))
print(nums, '\n')

# squares of first 10 numbers
squares = []
for num in range(1,11):
    print(f"square of {num} is {num**2}")
    squares.append(num**2)
print(squares)

# functions on numeral lists
print(min(squares))
print(max(squares))
print(sum(squares))

# List comprehension is more like a one liner code for lists
squares = [value**2 for value in range(1,11)]
print(squares)