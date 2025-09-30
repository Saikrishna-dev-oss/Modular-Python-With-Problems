def flatten(lst) :
    flat_list = [] #Final Flat list

    for item in lst:
        if isinstance(item,list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

lst = [[1,2],[3,[8,9]],[6,7]]
flatted_lst = flatten((lst))
print(flatted_lst)
