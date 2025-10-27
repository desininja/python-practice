"""
Before using setter and getter
"""

# class Employee:
#     def __init__(self,name,salary) -> None:
#         self.name = name
#         self.salary = salary

#     def first_name(self):
#         l = self.name.split(" ")
#         return l[0]
    
#     def show_salary(self):
#         return f"Salary of {self.name} is {self.salary}."
    
#     def update_first_name(self,first):
#         l = self.name.split(" ")
#         new_name = f"{first} {l[1]}"
#         self.name = new_name
    
#     def update_salary(self, percentage):
#         new_salary = self.salary*(1+(percentage/100))
#         self.salary = new_salary

# e = Employee("Jack Doe", 20000)

# print(e.first_name())
# print(e.show_salary())
# e.update_first_name("Heman")
# e.update_salary(100)
# print("After update")
# print(e.first_name())
# print(e.show_salary())




"""
After using setter and getters
"""


class Employee:
    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary = salary
    
    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @property
    def emp_salary(self):
        return f"Salary of {self.name} is {self.salary}."
    
    @first_name.setter
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

    @emp_salary.setter
    def emp_salary(self, percentage):
        new_salary = self.salary*(1+(percentage/100))
        self.salary = new_salary

e = Employee("Jack Doe", 20000)

print(e.first_name)
print(e.emp_salary)
e.first_name = "Heman"
e.emp_salary = 50
print("After update")
print(e.first_name)
print(e.emp_salary)