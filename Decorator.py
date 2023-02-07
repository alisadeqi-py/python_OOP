def decor(func):
    func()


def greetings():
    print('hello')


#decor(func=greetings)


@decor
def greetings():
    print('hello')