# Given the following data structure, return a new list identical in 
# structure to the original but, with each number incremented by 1.
# Do not modify the original data structure. Use a comprehension.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# def add1(dictionary):
#     return {key: value + 1 for key, value in dictionary.items()}

# lst_plus1 = [add1(dictionary) for dictionary in lst]
# print(lst_plus1)

# one list comprehension
lst_plus1 = [{key: value + 1 for key, value in dictionary.items()}
                             for dictionary in lst]
print(lst_plus1)