def square(lst):
    my_lst = list(map(lambda x:x**2 ,filter(lambda x:x%2==0,lst)))
    
    print(my_lst)
numbers = [1,2,3,4,5,6,7,8]
square((numbers))