class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # def __str__(self):
    #     return f"Name :{self.name}"
    def __repr__(self):
        return f"Name :{self.name}"
    def __len__(self):
        return len(self.name)

e = Employee("Harry",55680)
print(repr(e))
print(len(e))