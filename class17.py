class MyClass:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"
    
    def myfunc(self):
        """
        This Function will print a HEllo message with object name
        """
        print(f"Hello, {self.name}")

obj1= MyClass("John",20)
print(obj1)
obj1.myfunc()

obj2 = MyClass("Himanshu",28)
obj2.myfunc()