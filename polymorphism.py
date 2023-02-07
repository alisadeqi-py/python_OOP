from abc import ABC , abstractmethod

class Language(ABC):

    @abstractmethod
    def say_hello(self):
        pass


class Iranian(Language):
    def say_hello(self):
        print('سلام')


class English(Language):

    def say_hello(self):
        print('hello')  


ali = Iranian()
john = English()

def execute_hello(obj):
    print(obj.say_hello())

execute_hello(ali)
execute_hello(john)