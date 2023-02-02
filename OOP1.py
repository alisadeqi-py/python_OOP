class Employee:
    name = 'ali' #class variable 


    def __init__(self):
        self.age = 29


emp1 = Employee()

print(emp1.name , emp1.age)
print(Employee.name)
print(Employee.age)

