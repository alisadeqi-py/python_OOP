""" class car():
    def __init__(self):

        self.color = red
        self.speed = 200

    def set_speed(self , new_speed):

        self.speed = new_speed

    def get_speed(self):

        return self.speed



pride = car()
print(pride.speed)
pride.set_speed('500')
print(pride.get_speed())

 """


class Car():

    def __init__(self):

        self.a = 10 
        self._b = 20 #private_variable
        self.__c = 30#private_variable

    def __private_method(slef):
        print('i am private method')


pride =Car()

""" print(pride.a)
print(pride._b)
print(pride.__c) """

private = pride.__private_method()