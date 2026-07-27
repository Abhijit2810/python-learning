def pizza_toppings(size, *tops):
    # print(type(tops)) its a tuple
    print(f'Adding toppings for your {size}-inch pizza:')
    for top in tops:
        print(top)
    print('Pizza Ready!\n')