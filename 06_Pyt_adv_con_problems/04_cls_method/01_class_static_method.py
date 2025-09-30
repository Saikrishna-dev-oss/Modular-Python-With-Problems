class Gadget:
    count = 0
    total = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Gadget.count +=1
        Gadget.total +=price

    @classmethod
    def get_count(cls):
        return cls.count,cls.total
    
    @classmethod
    def reset_count(cls):
        cls.count,cls.total = 0,0
    
        
g1 = Gadget("Motor",5000)
g2 = Gadget("Bike",40000)
g2 = Gadget("Biscuit",50)
g2 = Gadget("Icecream",150)

count,total = Gadget.get_count()
print(count,total)
Gadget.reset_count()
count,total = Gadget.get_count()
print(count,total)
