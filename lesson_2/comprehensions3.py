# return a new list with the same structure, but with the values in each sublist ordered in ascending order as strings 
# (that is, the numbers should be treated as strings). Use a comprehension if you can.

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new_lst = [] 
# for sublst in lst:
#     reverse_sublst = sorted(sublst, key=str)
#     new_lst.append(reverse_sublst)
    
# print(new_lst)


new_lst = [sorted(sublst, key=str) for sublst in lst]
print(new_lst)