# using conditions in lists
toppings = ['corn', 'cheese', 'olives', 'capsicum', 'paneer']
# toppings = []
if toppings: # this ensures code only runs if list exists
    for top in toppings:
        if top == 'capsicum':
            print(f'Sorry, we currently dont have {top}')
        else:
            print(f'Adding {top}')
    print('\nPizza ready\n')
else:
    print('Empty list given!')

# using multiple lists
req_toppings = ['corn', 'pepper', 'cheese']
for req in req_toppings:
    if req in toppings:
        print(f'Adding {req}')
    else:
        print(f'Sorry, we dont have {req}')



