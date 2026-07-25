alien_0 = {'color': 'green', 'points':10}
alien_1 = {'color': 'blue', 'points': 15}
alien_2 = {'color': 'red', 'points': 20}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# list in dict:
pizza = {
    'Crust': 'Thin',
    'toppings': ['corn', 'cheese', 'paneer']
}

print(f"You ordered a {pizza['Crust']} crust pizza with the following toppings:")
for top in pizza['toppings']:
    print(top)

# looping
languages = {
    'abhi': ['C', 'Python', 'Java'],
    'Joshi': ['Rust', 'Go', 'Sparta'],
    'Kollampally': ['Cpp', 'React.js']
}
for k,v in languages.items():
    print(f'{k.title()} knows:')
    for lang in v:
        print(lang)
    print('\n')

# Nesting dictionaries
users = {
    'Abhijit': {
        'First_name': 'Kollampally Abhijit',
        'Last_name': 'Joshi',
        'Location': 'Hyderabad'
    },

    'Tejaswi': {
        'First_name': 'Tejaswi Vinayak',
        'Last_name': 'Hegde',
        'Location': 'Sirsi'
    }
}

for key,value in users.items():
    print(f'Information regarding {key}:')
    for k,v in value.items():
        print(f'{k} is {v}.')
    print('\n')


