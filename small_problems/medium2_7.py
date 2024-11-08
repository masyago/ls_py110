'''
input: list that contains at least 2 items
output: same list but sorted using bubble algorithm

rules:
- use Bubble algorithm
- given list has at least 2 items
- mutate given list

ALG:
- list_before_swap = original_list
- list_after_swap = 0
- while list_before_swap != list_after_swap:
    - list_after_swap = list_before_swap[:] # copy so we don't update list_before swap during sorting
    - do a round f sorting (swap_nums(lst) function)
-return list_after_swap


helper function: swap_nums:
    - iterate over idx in range from 0 to len(original_list)
        - if element with idx is larger than element with idx + 1
            - reassign elements in list_after_swap: idx to idx + 1 and vise versa (tuple unpacking)
    - return lst

- if list_before_swap == list_after_swap
    - return list_after_swap
'''

# def swap_nums(lst):
#     for idx in range(len(lst) - 1):
#         if lst[idx] > lst[idx + 1]:
#             lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]

#     return lst

# def bubble_sort(original_list):
#     list_before_swap = []
#     list_after_swap = original_list

#     while list_before_swap != list_after_swap:
#         list_before_swap = list_after_swap[:]
#         swap_nums(list_after_swap)
    
#     return list_after_swap

def bubble_sort(lst):
    while True:
        swapped = False
        for idx in range(1, len(lst)):
            if lst[idx - 1] <= lst[idx]:
                continue

            lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
            swapped = True

        if not swapped:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True