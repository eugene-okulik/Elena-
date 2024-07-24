def finish_me(func):

    def wrapper():
        func()
        print("finished")
    return wrapper


@finish_me
def example():
    print('print me')


example()
