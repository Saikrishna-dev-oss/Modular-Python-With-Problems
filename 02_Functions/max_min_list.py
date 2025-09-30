def find_max_min(lst,get):

    if not lst:
        raise ValueError("List cannot be Empty")
    elif (get == 'min'or get =='Min'): 
        return min(lst)
    elif (get == 'max'or get =='Max'):
        return max(lst)
numbers = [1,20,55,99,69,58]
print(numbers)
get = str(input("Enter Either Max or Min to Find : "))
max_num = find_max_min(numbers,get)
print(max_num)