class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self,fname,mname,lname):
        super().__init__(fname,lname)
        self.mname=mname

    def fullname(self):
        print(self.fname,self.mname,self.lname)


obj = Student("John","Hello","Doe")

obj.fullname()
print(obj.fname)
print(obj.mname)
print(obj.lname)