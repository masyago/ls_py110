# Write a function that takes two list arguments, each containing a list 
# of numbers, and returns a new list that contains the product of each
# pair of numbers from the arguments that have the same index. You may
# assume that the arguments contain the same number of elements.

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

'''
Problem
Write a function that mupltiplies numbers from two lists with same indexes

Examples/Test Cases
- given lists contain only numbers
- given pair of list have the same number of elements

Data Structure
input: two lists
output: a new list
supporting: maybe list comprehension

Algorithm
- not list comprehension:
    - initiliaze multiplied empty list
    - iterate over indexes 
        - mupltiply elements with the index
        - append result to mulitplied list
    -  return multiplied list
- list comprehension:
    - [expression for element in iterable if condition]
    - expression: element1 * element2
    - iterable: zip(list1, list2)
    - no condition

Coding

'''

# Not comprehension solution
# def multiply_list(list1, list2):
#     multiplied = []
#     for idx in range(len(list1)):
#         product = list1[idx] * list2[idx]
#         multiplied.append(product)
#     return multiplied

# Comprehension solution
def multiply_list(list1, list2):
    multiplied = [element1 * element2 for element1, element2 in zip(list1, list2)]
    return multiplied

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True