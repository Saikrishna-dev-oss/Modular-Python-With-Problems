class Student:
    college_name = "ABC COLLEGE"
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks

    @staticmethod
    def hello():
        print("Helllo") 

        
    def get_avg(self):
        sum = 0;
        for i in self.marks :
            sum += i
        print("Hi ",self.name, "Avg is",sum/3)     

        
s1 = Student("Krish",[98,99,97]) 
s1.get_avg()
s1.name = "Ssss"
s1.get_avg()

 