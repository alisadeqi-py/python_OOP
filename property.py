class Employee():
    salary = 3000
    
    def __init__(self ,   first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
        #self.full_name = '{} {}'.format(self.first_name , self.last_name)
    @property
    def full_name (self):
        return '{} {}'.format(self.first_name , self.last_name)

    @full_name.setter
    def full_name(self , name):
        self.first_name , self.last_name = name.split(' ')
    
    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None

emp_1 = Employee('ali' , 'sadeqi')

print(emp_1.full_name)
emp_1.full_name = 'mahdi najafi'
print(emp_1.full_name)
e