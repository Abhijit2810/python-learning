#6.1
person = {
    'first_name': 'Tejaswi',
    'last_name': 'Hegde',
    'City': 'Sirsi',
    'Age': 22
}

for key,value in person.items():
    print(f'{key} : {value}')

# 6.2
fav_nums = {
    'abhi': 28,
    'virat': 18,
    'rohit': 45,
    'sachin': 10,
    'abd': 17
}

for key,value in fav_nums.items():
    if key!='abd':
        print(f'Favorite number of {key.title()} is {value}')
    else:
        print(f'Favorite number of {key.upper()} is {value}')

# 6.3
meanings = {
    'print': 'print is a keyword in python used for printing',
    'for': 'for is a keyword used for looping',
    'del': 'del is a keyword used to delete'
}

for keywords, mean in meanings.items():
    print(f'{keywords} : {mean}')

# 6.4 already done in prev exercises

# 6.5
rivers = {
    'Telangana': 'Krishna',
    'Andhra': 'Godavari',
    'Karnataka': 'Kaveri',
    'Tamil': 'Kaveri'
}
for key,value in rivers.items():
    print(f'{value} flows in {key}')

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)

# 6.6
poll_taken = {
    'Abhi': 'C',
    'Joshi': 'Cpp',
    'Kollampally': 'Python'
}

polling_people = ['Abhi', 'Vishnu', 'Rama', 'Joshi', 'Krishna', 'Kollampally', 'Hanuman']

for people in polling_people:
    if people in poll_taken.keys():
        print(f'Thank you for polling, {people}.')
    else:
        print(f'Please poll, {people}.')
print('\n')

# 6.7
persons = {
    'Tejaswi':{
        'first_name': 'Tejaswi Vinayak',
        'last_name': 'Hegde',
        'City': 'Sirsi',
    },

    'Abhijit': {
        'First_name': 'Kollampally Abhijit',
        'Last_name': 'Joshi',
        'Location': 'Hyderabad'
    },

    'Krishna':{
        'First_name': 'Krishna Kasheenath',
        'Last_name': 'Pujari',
        'Location': 'Vijayapura'
    }
}

for key,value in persons.items():
    print(f'Information regarding {key}:')
    for k,v in value.items():
        print(f'{k} is {v}.')
    print('\n')

