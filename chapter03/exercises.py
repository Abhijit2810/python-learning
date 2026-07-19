# 3.1
names = ['cat', 'dog', 'cow']
print(names[0])
print(names[1])
print(names[2])
# print(names[3]) we get a index error

# 3.2
message = 'My pet is a'
print(f"{message} {names[0]}")
print(f"{message} {names[1]}")
print(f"{message} {names[2]}")

# 3.3
vehicles = ['bike', 'scooty', 'car']
print(f"I would love own a BMW {vehicles[2]}")
print(f"I like to own a {vehicles[0]} and also a {vehicles[1]}")

# 3.4
persons = ['Iron Man', 'Dr.Strange', 'SpiderMan', 'Thor']
message = 'Welcome to the party!'
print(f"Hi {persons[0]}, {message}")
print(f"Hi {persons[1]}, {message}")
print(f"Hi {persons[2]}, {message}")
print(f"Hi {persons[3]}, {message}")

# 3.5
print(f"{persons[3]} cant come")
persons[3] = "Captain America"
# new invitations
print(f"Hi {persons[0]}, {message}")
print(f"Hi {persons[1]}, {message}")
print(f"Hi {persons[2]}, {message}")
print(f"Hi {persons[3]}, {message}")

# 3.6
persons.insert(0, "Black Panther")
persons.insert(3, "Ant-Man")
persons.append("Thanos")
print(persons)

# 3.7
text = "The party has been cancelled, sorry for the trouble."
person = persons.pop()
print(f"Hi {person}, {text}")
person = persons.pop()
print(f"Hi {person}, {text}")
person = persons.pop()
print(f"Hi {person}, {text}")
person = persons.pop()
print(f"Hi {person}, {text}")
person = persons.pop()
print(f"Hi {person}, {text}")
print(f"Hi {persons[0]}, {message}")
print(f"Hi {persons[1]}, {message}")

# 3.8
places = ["Puri", "Varanasi", "Prayagraj", "Badrinath", "Kedarnath"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
places.reverse()
print(places)
places.reverse() #reversing the list 2 times regains the original order
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 3.9
print("The length of persons list is", len(persons))
print("The length of list of vehicles is", len(vehicles))
print("The list of places is of length", len(places))

# 3.10
languages = ["Telugu", "Hindi", "Kannada", "Tamil", "Malayalam", "English"]
cities = ["Hyderabad", "Delhi", "Bengaluru", "Chennai", "Cochin", languages]
print(cities)
languages.append(cities)
print(languages)

# 3.11
empty_list = []
# print(empty_list[-1]) this raises error as it has no elements
