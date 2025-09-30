# list = [1,2,3,3,4,5,5,6]
# list = set(list)
# print(list)


# def is_subset(s1,s2):
#     return s1.issubset(s2)


def unique_elements(set1, set2):
    return set1.symmetric_difference(set2)



a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(unique_elements(a, b))  # Output: {1, 2, 5, 6}
