class Employee:
    name = 'ali' #class variable 


    def __init__(self , age=None):
        self.age = age


emp1 = Employee(30)

print(emp1.name , emp1.age)

