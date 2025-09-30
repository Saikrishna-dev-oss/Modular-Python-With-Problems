def rotate_lst(lst,n):
    n = n % len(lst)

    return lst[-n:] + lst[:-n] 


my_list = [1,2,2.0,"sai",True,8,9]
n = int(input("Enter Rotation Count:"))
rotated_lst = rotate_lst(my_list,n)
print(rotated_lst)