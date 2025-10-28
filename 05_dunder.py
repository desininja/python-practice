class Employee:
    company = "HP"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f"The name is {self.name} and the salary is {self.salary}."
    

e = Employee("Ashu", 457685)
print(e.name,e.company)
print(str(e))