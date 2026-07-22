# Conditional statements
## if conditional
1. If statements executes by checking the condition given, if the condition turns out to be True then if gets executed, otherwise it wont, this checking is called as conditional test. Format below<br>
2. if (condition):<br>
&nbsp; code to be executed<br>
remaining code<br>
3. Most important thing, = stands for assigning, == checks for equality, this is important as this can cause changes or throw error.<br>
4. While checking conditionals, note uppercase and lowercase, for instance 'audi' is not equal to 'Audi'.<br>
5. for checking conditions, any number other than 0, even negative, are considered True, only 0 is considered False.<br>
6. Indentation plays a major role, like in for loops.<br>

## if-else conditionals
1. same as if, but if condition fails, code under else gets executed.<br>
2. if (condition):<br>
&nbsp; code to be executed<br>
else:<br>
&nbsp; code to be executed<br>
remaining code
3. Remember, else needs no condition explicitly, if all conditions fail else directly acts.<br>

## if-elif-else conditionals
1. This is used for checking multiple conditions, satisfying any one of the conditions will result in executing that code, otherwise else.<br>
2. There can be as many as elif statements.<br>
3. if (condition):<br>
&nbsp; code to be executed<br>
elif (condition):<br>
&nbsp; code to be executed<br>
else:<br>
&nbsp; code to be executed<br>
remaining code<br>
4. elif only works when previous if or elif conditions are failed, and its particular condition is satisfied.<br>

*Else is not mandatory to be provided.<br>*

# if in lists
1. When the name of a list is used in an if
statement, Python returns True if the list contains at least one item; an empty list
evaluates to False.<br>

# Frequently used Conditionals
1. in: in is used whether to check some parameter/value is present in given list/tuple/any DS.<br>
2. It return True or False.<br>
3. Same with not in, it returns true if the asked value is not present.<br>

# Simultaneous Conditions
1. and: if you can make the conditional statements work only when all the conditions are met, we use and, we connect statements using 'and' between statements in the code.<br>
2. or: if you can make the conditional statements work only if one of the conditions are met, we use or, we connect statements using 'or' between statements in the code.<br> 