class Car:
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")
    
class Toyota(Car):
    def __init__(self,brand):
        self.brand = brand

class Car(Toyota):
    def __init__(self,type,brand):
        self.type = type
        super().__init__(brand)

c1 = Car("Petrol","BMW")
print(dir(c1))