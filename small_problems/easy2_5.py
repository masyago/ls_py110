'''
Problem
2 non-empty lists are given. Return a new list that contains all elements from 
given lists. Pattern of new list: 1st element from lst1, 1st el from lst2, 
2nd element from lst1 etc

Examples/Test Cases:
- given list have the same number of elements

Data Structures:
input - 2 lists
output - 1 new list

Algorithm:
- iterate over both lists
- add elements to new list one by one

Coding
'''

# def interleave(lst1, lst2):
#     new_lst = []
#     for idx in range(len(lst1)):
#         new_lst.extend([lst1[idx],lst2[idx]])

#     return new_lst

# Solution using zip
def interleave(lst1, lst2):
    new_lst = []
    dict = zip(lst1, lst2)
    for pair in list(dict):
        for element in pair:
            new_lst.append(element)

    return new_lst


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

# print(interleave(list1, list2))