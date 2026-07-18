# Learning Variables
When we save a file using .py extension, the IDE doesn't execute Python itself. It asks the Python interpreter to execute the .py file. so it recognises which is the code to execute, what to print etc.
Variables as the name suggest, they are used to label some value to it, can be text, numbers, anything, and these variables can be used again and again, remember, variables give reference to that value, they dont store it. Variables can be overwritten(reassigned), it updates to latest entry.
Variables can be named using letters, numbers and underscore, and it cant start with numbers. No keywords like function names and no spacing can be used in naming.
Python interpreter tries to help to solve errors by giving which file, line and even error type and possible solution.

# Learning Strings
A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings.
f-strings are used for string formatting. 
To use a tab space we use \t, for new line \n.

# Learning numbers in python
When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float.
If you mix an integer and a float in any other operation, you’ll get a float as well.
Python defaults to a float in any operation that uses a float, even if the output is a whole number.
Comments are anything written after #, which python doesn't execute, comments are written for simple explanation of what the code or function does.

# Learning Functions
A method is an action that Python can perform on a piece of data. The dot (.) after name in name.method() tells Python to make the method act on the variable name.
The title() method changes each word to title case, where each word begins with a capital letter. This is useful because you’ll often want to think of a name as a piece of information.
name.upper() converts the string into uppercase.
name.lower() converts the string into lowercase.
Python can look for extra whitespace on the right and left sides of a string. To ensure that no whitespace exists at the right side of a string, use the rstrip() method, lstrip for left, for both use just strip.
name.removeprefix() removes prefix

# Learning Errors
Name Error : A name error usually means we either forgot to set a variable’s value before using it, or we made a spelling mistake when entering the variable’s name.