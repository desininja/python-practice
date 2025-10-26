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