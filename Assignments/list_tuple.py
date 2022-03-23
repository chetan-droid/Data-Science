def list_in_tuple(list1):
    return list1[1]

list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(list1, key=list_in_tuple))
