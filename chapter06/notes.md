# Dictionaries
1. A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.<br>
2. A key’s value can be a number, a string, a list, or even another dictionary.<br>
3. In Python, a dictionary is wrapped in braces ({}) with a series of key-value pairs inside the braces.<br>
4. A key-value pair is a set of values associated with each other. When you provide a key, Python returns the value associated with that key.<br> 
5. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. We can
store as many key-value pairs as you want in a dictionary.<br>
6. Example, dict_name = {'key1' : value, 'key2' : value}<br>
7. Dictionaries retain the position in which they were added ro defined.<br>
8. In Dictionaries, we can modify values of the keys, but not the keys itself.<br>
9. for looping in dictionary, we do something like<br>
for k,v in dict_name.items():<br>
&nbsp; code to be executed<br>
10. .items() is important because it gives out all key,value pairs present in the dictionary, only keeping dict_name gives out only keys.<br>
11. .keys() if only keys are needed, while .values() if only values are needed.<br>
12. 


# Dictionary functions
1. get(): Normally in dictionary,if the key you ask for doesn’t exist, you’ll get an error. To avoid that error, we use get() function.<br>
2. The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist.<br>
3. example, var_name = dict_name.get('key_name', 'What to do if key doesn't exist').<br>
4. If second argument is not passed, and key is not present, python by default return None.<br>