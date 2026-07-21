names = ['Kollampally', 'Abhi', 'Jit', 'Joshi','ISI', 'QROR', 2028]
print(names[1::2])

# looping in sliced lists
for name in names[:4]:
    print(name)

list_copy = names[:]
print(names == list_copy) # return true as they have same values
print(names is list_copy) # return false as they are not refering to same address

# tuples
dims = (200,100,100)
for index in range(3):
    print(dims[index])

# dims[0] = 500 this raises error, as tuples cant be changed once they are created
print(dims)