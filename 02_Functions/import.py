# import mymodule as m
# n = 4
# print(m.power(n,10))
# print(m.square(n))
# print(m.cube(n))


# import math as m
# def calculate_area(radius):
#     return m.pi * radius**2
# print(calculate_area(5))


# from datetime import datetime
# current_time = datetime.now()
# print("Current Date and Time:", current_time.strftime("%Y-%M-%D  %H:%M:%S"))


# import random 

# def random_number(start, end):
#     return random.randint(start,end)
    
# print(random_number(1,99))


import os

def check_file_exist(path):
    return os.path.exists(path)

path = "C:\\python\\Functions\\random_pass.py"
# path = path.replace('\\',"\\\\")
path1 = "C:\\python\\Functions\\random_pass.py"
# path1 = path1.replace('\\',"\\\\")
print(check_file_exist(path1))
print(check_file_exist(path))
# print(path1)
# print(path)