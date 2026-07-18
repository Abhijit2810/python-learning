'This is a string being written'
"This is also a string, nothing matters between single and double quotes"
'writing only these strings, run this code, it shows no errors'

# this below format helps us with printing quotes inside a string when they are printed
'I told myself "I am going to ISI M-tech QROR"'

name = 'KollampaLLY AbhIJit JoSHi'
print(name.title())
print(name.upper())
print(name.lower())

# f-strings
first_name = "Kollampally Abhijit"
last_name = "Joshi"
full_name = f"{first_name} {last_name}"
print(full_name)

# you can use methods on them too
print("Hello " f"{first_name} {last_name}")

# We can also assign variables to it
text = f"Hi {first_name} {last_name}, we are learning f-strings in python"
print(text)

# \t for tab space, \n for new line
print("\t Hello")
print("\n hello")

# can also use tab spaces in that along with going to next line
print("Languages: \nEnglish \nHindi \nTelugu")
print("Languages: \n\tEnglish \n\tHindi \n\tTelugu")

# removes left and right spaces, lstrip for left, rstrip for right, strip for both
fav_lang = "     Telugu "
print(fav_lang)
fav_lang = fav_lang.strip()
print(fav_lang)

# for removing prefixes
url = "https://google.com"
print(url)
url = url.removeprefix("https://")
print(url)

# if you want apostrophes to be printed, try using '' outside and "" inside or vice versa
print('I told myself "I am going to ISI M-tech QROR"')