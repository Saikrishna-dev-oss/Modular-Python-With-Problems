class Employee:
    company = "HP"
    def __init__(self,name,salary):
        self.name  = name
        self.salary = salary

    #Instance method
    def print_info(self):
        info = f"The Name is {self.name} and salary is {self.salary}"
        print(info)

    # Static Method
    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_name):
        cls.company = new_name


e1 = Employee("jack",9856)
e2 = Employee("Jill",7845)

e1.print_info()
print(e2.sum(4,11))

e1.print_company()
e1.change_company("Acer")
print(Employee.company)
e2.print_company()
