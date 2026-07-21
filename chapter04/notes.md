# Learning loops
1. For loops:A for loop iterates over every element of an iterable (list, string, tuple, range, etc.) and executes the loop body once for each element. The code goes something like:<br>
for variable in list_name/string_name/DS_name:<br> &emsp; - task needs to be done, like printing, updating etc.<br>
2. This code makes the task to run on each entry of the DS given.<br>


# For loop Working
1. First, the temporary variable in the loop takes the first element from the DS provided, it means it refers to the element, then it does the task with first element.<br>
2. Then, the variable gets assigned to second value and third and so on to the last.<br>
3. It is very important to know about indentation, not giving indentation or unnecessarily give more indentation can give indentation errors.<br>
4. And also the colon, without colon python interpreter doesnt understand what are we trying to do, it raises syntax error as : is missing.<br>

# Learning Tuples
1. Tuples are immutable. They are used when we dont want to change data present in it. once a tuple is created, its values or inputs cant be changed.<br>

# Learning Built in Functions
1. range(): range is used to generate numbers. it has 3 inputs (start, end, jump), by default start=0, jump=1 and end number is not included.<br>
2. for example if we give range(5), then python interprets it as range(0,5,1) and processes it.<br>
3. Another important point, we cant give step size without giving start and end, if we give only 1 input python assumes it as end and calculates, only 2 inputs, then start and end, only 3 would give step size.<br>
4. Example, range(11,2) doesnt print even numbers upto 12, assuming start=0, it assumes start=11, end=2, step=1 and does calculation and return empty list as its not possible. so we need to specifically mention (0,11,2) for that.<br>
5. min(), max, sum, functions like these output their respective works on numeral lists.<br>

## List Slicing Functions:
1. list_name[start:end:step], works same as range, its slices the list from start to end-1 (end not included) with step size of step.<br>
2. Default of start=0, end=last, step=1.<br>
3. we can also do something like list[:], this prints whole list.<br>

## List comprehension:
1. A concise way to construct a new list. Its an easy way of writing simple lists instead of spending 3-4 lines for that list.