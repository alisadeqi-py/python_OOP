class Employee:
    salary = 3000 #class variable 


    def __init__(self , name,age=None):
        self.age = age
        self.name = name

emp1 = Employee(30)

print('before' , emp1.name , emp1.age , emp1.salary)
Employee.salary = Employee.salary *2 
print('after' , emp1.name , emp1.age , emp1.salary)

