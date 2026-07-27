#8.1
def display_message():
    print('Hey Everyone, iam learning python functions.')


display_message()


# 8.2
def favorite_book(book_name='The Mahabharata'):
    print(f'One of my favorite books was "{book_name.title()}".')


# book = input('Enter your favorite book name: ')
favorite_book()


# 8.3, 8.4
def tshirt_printing(size='large', text='I Love Python'):
    print(f'The required t-shirt size is {size} and message to be printed is "{text}".')


tshirt_printing('XL', "Don't Care")
tshirt_printing()


# 8.5
def cities(city, country='India'):
    print(f'{city.title()} is in {country.title()}.')


cities('Hyderabad', 'India')
cities('hyderabad')
cities('Tokyo', 'China')
cities('Sydney', 'Australia')


# 8.6
def city_country(city, country):
    return f'{city.title()}, {country.title()}.'


print(city_country('Hyderabad', 'India'))
print(city_country('Tokyo', 'China'))
print(city_country('Sydney', 'Australia'))


#8.7
def music_album(singer, song):
    album = {song: f'This song is sung by "{singer}".'}
    return album


print(music_album('AR Rahman', 'Luka Chuppi'))
print(music_album('Sid Sriram', 'Arerey Manasa'))
print(music_album('SP Bala Subramanyam', 'Jabilli Kosam'))


# 8.8
flag = True
print('If you want to exit from the loop, enter quit in song')
while flag:
    song = input('Enter the song: ')
    if song.lower() == 'quit':
        print('Loop exited!')
        flag = False
        break
    singer = input('Enter the name of the singer: ')
    print(music_album(singer,song))


# 8.9, 8.10, 8.11
def message_print(texts):
    sent_messages = []
    while texts:
        message = texts.pop()
        print(message)
        sent_messages.append(message)
    sent_messages.reverse()
    return sent_messages


messages = ['Hi', 'Hello', 'Namaste']
result = message_print(messages[:])
print(result == messages)


# 8.12
def sandwich_toppings(*tops):
    print('Adding toppings to sandwich: ')
    for top in tops:
        print(top.title())
    print('Sandwich Ready!\n')


sandwich_toppings('tomato', 'onion', 'cucumber', 'capsicum', 'mayonnaise')


# 8.13, 8.14
# def user_profile(first, last, **others):
#     others['first_name'] = first.title()
#     others['last_name'] = last.title()
#     return others
#
#
# print(user_profile('kollampally abhijit', 'joshi', age=21, gender='Male', college='ISI Kolkata'))


# 8.15, 8.16
# all the different methods of importing
import function_file_importing
import function_file_importing as ffi
from function_file_importing import user_info
from function_file_importing import *
from function_file_importing import user_info as ui
print(ui('kollampally abhijit', 'joshi', age=21, gender='Male', college='ISI Kolkata'))




