# person 
class Person():

    def __init__(self , first_name , last_name ):
        
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return self.first_name + ' ' + self.last_name

# Employee 

class Employee(Person):
    salary = 3000
    
    def __init__(self ,   first_name , last_name ,position):
        #self.position = position this line is over writung the __init__ function 
        super().__init__(first_name , last_name)
        self.position = position
    
    def job(self):

        return f'hi I am {self.first_name} my position is {self.position}'

# cto 

class CTO(Employee):

    salary = 6000

    def job(self):

        return f'hi i am {self.first_name} my position is CTO'
# intern 

class CTO(Employee):

    salary = 1000

    def job(self):

        return  f'hi i am learning new things'