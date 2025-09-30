# MAP

# num = [1,2,5,4]
# a = list(map(lambda x : x*x,num))
# print(a)


#Filters

# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else :
#         return False

# a = [1,33,44,69,9,8,10]
# new = sorted(list(filter(lambda x:x>9,a)))
# print(new)
# Reduce 
from functools import reduce

numbers = [1,2,3,4,5,6]
def sum(a,b):
    return a+b

c = reduce(sum,numbers)
print(c)