# python-practice
This repo is for practicing python


# Advance Python Concepts

1) Decorators: Decorators in python are a powerful and popular design pattern that allows you to modify or enhance a function or class without directly changing its source code. They are essentially functions that take another function (or class ) as an argument, add some functionality, and return the modified function (or class).


Analogy: Think of a decorator like wrapping a present. You arent changing the present inside , but you're adding wrapping, a bow, maybe a card to give it extra features or presentation. 

Key Concepts.
    Syntactic Sugar: Python provides a special syntax using the @symbol for applying decorators, which is cleaner than writing out the function call manually. 

    Callable: Decorators work because functions in Python are first-class objects, meaning they can be treated like any other object (such as integers, strings or lists) and can be passed as arguments to other functions, returned as values and assigned to variables.





# Anonymous inline Functions

Anonymous inline functions in Python are small, single-expression functions that are not formally defined using the standard `def` keyword. They are created using the `lambda` keyword. 

Key characteristics of Lambda Functions
- Anonymous: they do not have a name.
- Inline and Single Expression.


Lambda functions are generally used when you need a small function for a short period of time and as an argument to another higher-order function. They are often used with Python's built-in functional tools:
- map()
- filter()
- sorted()

you should choose lambda function when you need a small, single-expression function that will be used immediately and often only once, typically as a callback or key function. 


🛑 When to Avoid Lambda (The "When Not To"):
- You need multi-line logic.
- You need a docstring
- The logic is complex or reusable


## Getter and Setter in Python

In Python, a getter and setter are methods used to access and update the attributes of a class. These methods provide a way to define controlled access to the attributes of an object, there by ensuring the integrity of the data. 

    - Getter: The getter method is used to retrieve the value of a private attribute, It allows controlled access to the attribute. 
    - Setter: The setter method is used to set or modify the value of a private attribute. It allows you to control how the value is updated, enabling validation or modification of the data before it's actually assigned. 

    @property for getter 
    @<function_name>.setter

    getter and setter should have same name if it is defined for a function. 


    # Class method, Static Method and Instance Method

    Three important types of methods in python.

    Class method in python:
    Class methods are associated with the class rather than instances, they are defined using the @classmethod decorator and take the class itself as teh first parameter, usually names cls. Class methods are useful for tasks that involve the class rather than the instance, such as creating class-specific behaviors or modifying class-level attributes.

    Static Method in Python
Static methods, as the name suggests, are not bound to either the class or its instances. They are defined using the @staticmethod decorator and do not take a reference to the instance or the class as their first parameter. Static methods are essentially regular functions within the class namespace and are useful for tasks that do not depend on instance-specific or class-specific data.


Instance Method in Python
Instance methods are the most common type of methods in Python classes. They are associated with instances of a class and operate on the instance's data. When defining an instance method, the method's first parameter is typically named self, which refers to the instance calling the method. This allows the method to access and manipulate the instance's attributes.


The __init__ method in Python  is a special method, often called a constructor, that is automatically called when a new object (instance) of a class is created. 

## Purpose and Function

The primary purpose of __init__ is to initialize the attributes of the newly created object. 
    - Initializes Attributes: It accepts arguments (if defined) and uses them to set the initial state of the object.

🔑 Key Points
Double Underscores (Dunder): The method name is enclosed in double underscores (__), which signifies that it is a special method (or magic method) in Python.

Execution: It is not called explicitly by the programmer. It's invoked by Python when you use the class name to create an object (e.g., Car(...)).

Return Value: It must not have a return statement that returns a value. Its sole job is setting up the object.