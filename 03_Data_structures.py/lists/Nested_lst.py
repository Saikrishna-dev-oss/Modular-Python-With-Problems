# Max,Min Elemnet in list

lst = [[1,2,88],[3,9,69],[4,12,2]]
maximum = max(max(row) for row in lst)
minimum = min(min(row) for row in lst)
print(maximum,minimum)


# read Elements from user to nested list
lst = []
rows,cols = 3,3
for i in range(rows):
    sub_list = []

    for j in range(cols):
        n = input(f"Enter Element for row {i+1} , column {j+1} : ")
        sub_list.append(n)
    lst.append(sub_list)
print(lst)
    




