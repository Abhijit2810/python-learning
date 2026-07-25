alien1 = {'color':'green', 'points':5}
print(alien1)
print(alien1['color'])
print(alien1['points'])

points = alien1['points']
print(f'You earned {points} points for shooting alien 1')

# adding items to dictionary
alien1['x-coord'] = 0
alien1['y-coord'] = 25
print(alien1)

# adding to empty dict
alien2 = {}
print(alien2)
alien2['color'] = 'blue'
alien2['points'] = 10
print(alien2)

# modifying values - we can change only values, not keys
alien2['color'] = 'red'
print(alien2)

# workflow
alien3 = {'color': 'orange', 'speed': 'fast', 'x_pos':10, 'y_pos':20}
# Alien movement
if alien3['speed'] == 'slow':
    alien3['x_pos'] = alien3['x_pos'] + 5
    alien3['y_pos'] = alien3['y_pos'] + 10
elif alien3['speed'] == 'medium':
    alien3['x_pos'] = alien3['x_pos'] + 10
    alien3['y_pos'] = alien3['y_pos'] + 20
else:
    alien3['x_pos'] = alien3['x_pos'] + 15
    alien3['y_pos'] = alien3['y_pos'] + 30

print(alien3['speed'])
print(alien3)

# deleting pairs - just key is required
del alien3['y_pos']
print(alien3)

# dictionary of similar objects
languages = {
    'Abhi': 'C',
    'Joshi': 'Cpp',
    'Kollampally': 'Python',
    'Jit': 'Python'
}

for key,value in languages.items():
    print(f'The favorite langauge of {key} is {value}.\n')

# using get
print(alien3)
y_ord = alien3.get('y-pos', 'No key named y-pos')
print(y_ord)

# loops
user_1 = {
    'userid': 'user123',
    'pass': 'pass123'
}
for key, value in user_1.items():
    print(key)
    print(value)

# only looping through keys
for keys in user_1.keys():
    print(keys)

# only values
for values in user_1.values():
    print(values)

# sorted keys
for keys in sorted(languages.keys()):
    print(keys)

# for duplicates - duplciates are removed by using set
for values in languages.values():
    print(values)

for values in set(languages.values()):
    print(values)


