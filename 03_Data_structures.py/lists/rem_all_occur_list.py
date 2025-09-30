def remove_all_occurences(lst,n):
    
    return [x for x in lst if not (x==n and (type(x) == type(n)))]
     

my_list = [1, "hello", True, 3.14, "world", False, 1.0]
print(my_list)
user_input = input("Enter Element to remove from list: ")

if user_input.isdigit():
    user_input = int(user_input) #Int conversion

elif user_input.replace(".","",1).isdigit():
    user_input = float(user_input)  #Float conversion

elif user_input.lower() in ["true","false"]:
    user_input = user_input.lower() == "true"

else:
    user_input = str(user_input)

new_list = remove_all_occurences(my_list,user_input)
print(new_list)

