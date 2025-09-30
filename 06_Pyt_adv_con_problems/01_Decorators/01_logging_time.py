import time as t

def logging_execution_time(func):
    def wrapper(*args,**kwargs):
        print("Hi Logging Time execution is Taking place")
        start = t.time()
        result = func(*args,**kwargs)
        end = t.time()
        print("Completed")
        print(f"{func.__name__} is Exected in {end-start:.4f}")
    return wrapper

@logging_execution_time #Decorator name and calling it
def slow_function():
    t.sleep(1)
    return "done!"

# Function call
slow_function()