# Learning Functions
1. Let's say we want to run some task on some given inputs, instead of writing the same code for every given value, we could write the code for task once and then run for every value, easy right!, This way of storing a certain task/code are known as functions.<br>
2. Functions are defined something like this using def keyword.<br>
def function_name(arguments):<br>
&nbsp; code to execute<br>
Arguments need not be single, we can pass multiple arguments too.<br>
3. We need to call the function for it to run by providing arguments if any required for the function, something like this.<br>
function_name(arguments)
4. Immutable objects (int, float, str, tuple, bool) behave like copies because you cannot modify them.
Mutable objects (list, dict, set) can be modified inside the function, and those changes are visible outside unless you pass a copy.<br>
5. The order in which arguments are sent matters, not going by the positional arguments can cause errors in the code or change the meanings of the output.<br>
6. We can directly assign values to arguments while calling functions, but we need to make sure we are giving values to the correct argument names given.<br>
function_name(argument1 = value1, argument2 = value)<br>
7. We can also assign default values to the arguments, if in case they are not provided, they use default values.<br>
8. While function call if arguments are required and we don't give arguments or insufficient number of arguments it raises an error.<br>
9. Functions needn't always display the output, it can return the values, values can be anything like boolean,number,list,tuple anything, return is executed with return keyword.<br>
10. Remember, when the function reaches a stage where it's executing the code line having 'return' in it, it exits directly from there by returning the value.<br>
11. Sometimes, we don't know how many arguments to pass, in that case we do *args(meaning arguments) so that we can give as many arguments as you want, it goes in as tuple.<br>
12. and sometimes we don't know how many key value pairs we need, in that case **kwargs(meaning key value arguments).<br>
13. We can import functions in python, so that the underlying code of that imported function is not visible, we only get a high level view.<br>
14. We can also import specific function from a module and use it and can use aliases too.<br>
15. Format would be something like:<br>
from module_name import function_name as fn.<br.
16. from module import * <br>imports all public names (functions, classes, variables). It's generally discouraged because it can make code harder to read and may cause name conflicts. <br>
