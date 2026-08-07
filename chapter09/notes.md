# Learning Classes
1. class in Python is a blueprint or template for creating objects, which bundle data (attributes) and behavior (methods) together.
2. Objects created from the same class share the same methods (behavior), but each object usually stores its own attribute values (state).
3. When we define a new object in the class, it automatically gets the behaviour of the class.
4. Making an object from a class is called instantiation, and we work with instances of a class.
5. A function that’s part of a class is a method.
6. Variables that are accessible through instances are called attributes.
7. Dot notation is used often in Python for accessing attributes. Python looks at the instance created and then finds the attribute associated with the class. This is the same attribute referred to as self.attribute_name in the class.
8. To call a method, give the name of the instance  and the method(function inside class) you want to call, separated by a dot.
9. We can create/update new attributes (variables) in a class with 3 ways.<br>
&nbsp; First is declaring self.attribute_name = 0 inside init function, then it can be &nbsp;accessed from outside.<br>
&nbsp; Second is directly accessing from a function after an object instance is created.<br>
&nbsp; Third is directly accessing attributes from function and then changing it.



# Learning init
1. The __init__() method is a special method that Python runs automatically whenever we create a new instance based on the class.
2. This method has two leading underscores and two trailing underscores, a convention that helps prevent
Python’s default method names from conflicting with our method names.
3. We define the __init__() method to have any number of parameters. The self parameter is required in the method definition, and it must come first, before
the other parameters.
4. self must be included in the definition because when Python calls this method later (to create an instance of class), the method call will automatically pass the self argument.
5. Every method call associated with an instance automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.

# Learning Inheritance
1. We don’t always have to start from scratch when writing a class. If the class we are writing is a specialized version of another,we can use inheritance.
2. When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class.
3. The child class can inherit any or all of the attributes and methods of its parent class,
but it’s also free to define new attributes and methods of its own.
4. For the child class created, we need to inherit the properties of parent class by mentioning parent class name in () of child class initialisation.
5. The super() function is a special function that allows you to call a method from the parent class.
6. The name super comes from a convention of calling the parent class a superclass and the child
class a subclass.
7. We can override any method from the parent class that does not fit what we are trying to
model with the child class. 
8. To do this, we define a method in the child class with the same name as the method we want to override in the parent class. 

# Importing Classes
1. Python lets us store classes in modules and then import the classes we need into main program.
2. Simply we call class that needs to be called from the .py file where the class is stored, and use the functionality by creating the instances.
3. There are several ways to modify instance attributes, we see 3 here, first is importing only the class required from the file, something like "from file_name import class_name".
4. We can also import every class needed from the py file by mentioning class values as csv, something like"from file_name import class_name1,class_name2" and so on with other classes.
5. Second is importing the whole file and then making instances, something like Car.car().
6. Finally, importing everything from the given file by doing "from file_name import *" this imports everything from that file, but it is not recommended.
