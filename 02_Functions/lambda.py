
data = [(1, 5), (3, 2), (4, 8), (2, 1),(2,2)]

sorted_data = sorted(data, key = lambda x: (x[1],x[0]))
print(sorted_data)

# # desending
# data = [(1, 5), (3, 2), (4, 8), (2, 1)]
# sorted_data = sorted(data, key=lambda x: -x[1])
# print(sorted_data)

# names = ["Alice", "bob", "Charlie", "david"]
# sorted_names = sorted(names, key=lambda x: x.lower())
# print(sorted_names) 

 # Output: ['Alice', 'bob', 'Charlie', 'david']