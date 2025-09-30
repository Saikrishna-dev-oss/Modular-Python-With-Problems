class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #Vector Addition
    def __add__(self,other):
        # print (f"{self.x + v2.x} + {self.y+v2.y}i")
        if isinstance(other,Vector):
            return Vector(self.x + other.x,self.y+other.y)
        else :
            raise TypeError("Operand Must be of Vector Form")
        
    #Scalar Multiplication
    def __mul__(self,scalar):
        if isinstance(scalar,(int,float)):
            return Vector(self.x * scalar,self.y *scalar)
        else :
            raise ValueError("Enter a Scalar value i.e Number")
    
    # To print Vector or Scalar
    def __repr__(self):
        return f"Vector({self.x} ,{self.y})"

v1 = Vector(1,2)
v2 = Vector(2,3)
v_add = v1 + v2
v_mul = v1*3
print(v_add)
print(v_mul)
# print(f"{v3.x} + i{v3.y}")