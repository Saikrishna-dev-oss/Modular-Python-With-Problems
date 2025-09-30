class Point:
    def __init__(self,x,y):
          self.x = x 
          self.y = y

    def __add__(self,p):
         return Point((self.x +p.x),(self.y + p.y))
    
    def print_sum(self):
         print(f"X is {self.x} and Y is {self.y}")

p1 = Point(3,5)
p2 = Point(1,2) 

p = p1 + p2
p.print_sum()
print(p.x)
          