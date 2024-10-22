'''
P: Understanging Problem
White a function that converts given list ot a list that contain only two elements.
First element is a list of first half of elements from original list.
Second element is a list that contain the rest elements from original list. 
For even number of elements in OG list add extra element to the first sublist

E: Examples + Test Cases 
- order of elements preserved
- if original list contains 1 element, first sublist will contain that eleemnt.
Second element will be empty list
- if original list is empty, return list of 2 empty sublists

Data Structure:
input: list
output: nested list
no intermediate data structures

Algorithm:
- lst given
- create a new list: lst_of_halves [[], []]
- check number of elements in lst. 
    - if 0, return [[],[]]
    - if 1, add element to the first sublist, second sublist will be empty
    - if number of elements is even, add first half to first sublist
      add the rest of the elements to second sublist
    - if number of elements is odd, add half+1 element to first sublist,
      add the rest to the second sublist


C: Coding
'''

# def halvsies(lst):
#     lst_of_halves = []
#     if len(lst) == 0:
#         lst_of_halves = [[], []]
#     if len(lst) == 1:
#         lst_of_halves.append(lst[:])
#         lst_of_halves.append([])
#     elif len(lst) >= 2:
#         lst_half_len = int(len(lst) / 2)

#         if len(lst) % 2 == 0:
#             first_half_even = lst[: lst_half_len]
#             second_half_even = lst[lst_half_len:]       
#             lst_of_halves.append(first_half_even)
#             lst_of_halves.append(second_half_even)
#         elif len(lst) % 2 == 1:
#             first_half_odd = lst[: (lst_half_len + 1)]
#             second_half_odd = lst[(lst_half_len + 1):]  
#             lst_of_halves.append(first_half_odd)
#             lst_of_halves.append(second_half_odd)
    

#     return lst_of_halves

def halvsies(lst):
    half_len = (len(lst) + 1) // 2
    first_lst = lst[:half_len]
    second_lst = lst[half_len:]
    return [first_lst, second_lst]

# All of these examples should print True
print(halvsies([1, 2, 3, 4])) #== [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3])) #== [[1, 5, 2], [4, 3]])
print(halvsies([5])) # == [[5], []])
print(halvsies([])) # == [[], []])

# print(halvsies([1, 2, 3, 4, 5]))