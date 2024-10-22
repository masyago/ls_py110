
def union(lst1, lst2):
    union_set = set(lst1) | set(lst2)
    return union_set


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True