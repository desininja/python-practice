class Employee:
    company = "HP"
    def __init__(self,name,salary) -> None:
        self.name = name 
        self.salary = salary
    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method
    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company



    

e1 = Employee("Jack", 25)
e2 = Employee("Jill", 56)

# e1.print_info()
# e2.print_info()

# print(e1.sum(20,30))

e2.print_company()
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)

e2.print_company()