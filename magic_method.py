class Employee:
    salary = 3000 #class variable 

    def __init__(self , name,age=None):
        self.age = age
        self.name = name
    
    def hello(self):
        return f'hello  {self.name}'
    
    def __str__(self):
        return __class__.__name__


emp1 = Employee('ali' , 30)
print(emp1)