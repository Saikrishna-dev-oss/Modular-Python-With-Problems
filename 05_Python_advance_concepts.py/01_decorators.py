
def decorator(func):
    def wrapper():
        print("I am about to Execute a function!")
        func()
        print("Function is Executed")
    return wrapper
@decorator
def say_hello():
    print("Hello!")

say_hello()

