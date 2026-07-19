# Creating Lists
names = ['Abhijit', 'Joshi', 'Kollampally', 10]
# they can have multiple data types in it
print(names)

# indexing
print(names[0])

# string operations on list items
print(names[0].upper())

# last element
print(names[-1])

# using list elements in f strings
print(f"{names[0]} is in ISI Kolkata")

# modifying elements in list
print(names)
names[0] = 20 # can reassign to other data type too
print(names)

# appending elements
names.append(30)
print(names)
names.insert(2, 'Abhijit')
# names.insert(10, "Abhijit") works by putting element at last, but it is bad practice
print(names)

# adding to empty lists
cars = []
cars.append('BMW')
cars.append('Mercedes')
cars.append("Ford")
print(cars)

# deleting elements
del names[0]
print(names)
last_ele = names.pop() # pop removes last element of the list
print(last_ele)
print(names)
print(f"The last element in names list was {last_ele}")
names.pop(0) # index removes particular element
print(names)
# names.pop(10) if index is greater than length of list, it again throws indexerror
names.remove(10) # remove is used to remove element directly
print(names)
# names.remove('hgdhgdh'), if element is not in list, it throws value error saying that its not in the list

# sorting
# bikes = ['honda', 'suzuki', 'bmw', 50, 7, 16] while sorting we cant have multiple Data type elements in list
bikes = ['honda', 'suzuki', 'bmw']
print(bikes)
bikes.sort()
print(bikes)
bikes.sort(reverse=True) #reverses the order
print(bikes)
nums = [56,99,24]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True) #reverses the order
print(nums)


# temporary sorting
values = ['z','b','c']
print(values)
print(sorted(values))
print(values)
print(sorted(values, reverse=True))

# reversing the list
values.reverse()
print(values)

# finding length of list
print("The length of values list is", len(values))