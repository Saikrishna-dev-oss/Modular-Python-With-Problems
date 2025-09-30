class Employee:
    def __init__(self,name,salary):
        self.name  = name
        self.salary = salary
    @property
    def first_name(self):
        l =  self.name.split(" ")
        return l[0]
    @first_name.setter
    def first_name(self,first):
        l =  self.name.split(" ")
        new_name = self.name.replace(l[0],first) 
        self.name = new_name

e1 = Employee("Jack Doe",69955)
# print(e1.first_name())
# e1.set_first_name("sai")
# print(e1.name)

print(e1.first_name)
e1.first_name = "john"
print(e1.name)