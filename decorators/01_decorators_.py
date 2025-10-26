def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function...")

    return wrapper

'''
Simply calling the function will print Hello
'''
# def say_hello():
#     print("Hello!!!")

#say_hello()


'''
This is explicilly calling decorator method
Behing the scene f() looks somthing like this:
f():
    print("I am about to execute a function....")
    print("Hello!!!")
    print("I have executed this function...")
'''
# f = decorator(say_hello)
# f()



"""
More pythonic way of doing this is to use syntactic sugar @
"""

@decorator
def say_hello():
    print("Hello!!!")


say_hello()