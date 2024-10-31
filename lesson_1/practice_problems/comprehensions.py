# Compute and display the total age of the family's male members. 
# Try working out the answer two ways: first with an ordinary loop,
#  then with a comprehension.

# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }

# ages = [info['age'] 
#         for info in munsters.values()
#         if info['gender'] == 'male'
# ]

# print(sum(ages))

# Given the following data structure, return a new list with the 
# same structure, but with the values in each sublist ordered in 
# ascending order. Use a comprehension if you can. (Try using a
# for loop first.)

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# ordered_nested_lists = [sorted(nested_list) for nested_list in lst]

# print(ordered_nested_lists)

# Given the following data structure, return a new list with the same 
# structure, but with the values in each sublist ordered in ascending
#  order as strings (that is, the numbers should be treated as strings). 
#  Use a comprehension if you can. 

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# sorted_sublists = [sorted(sublist, key=str)
#                    for sublist in lst]

# print(sorted_sublists)

# Given the following data structure, write some code that defines a dictionary
# where the key is the first item in each sublist, and the value is the second.

# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# dict1 = {sublist[0]: sublist[1] for sublist in lst}

# print(dict1)

# Given the following data structure, sort the list so that the sub-lists are
# ordered based on the sum of the odd numbers that they contain. You shouldn't
# mutate the original list.

# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]


# def odd_sum(sublist):
#     odd_num = [num for num in sublist if num % 2 == 1]
#     return sum(odd_num)

# sorted_lst = sorted(lst, key=odd_sum)

# print(sorted_lst)

# Given the following data structure, return a new list identical in structure
# to the original but, with each number incremented by 1. Do not modify the 
# original data structure. Use a comprehension.

# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]


# # def num_plus1(dict1):
# #     return {key: value + 1 for key, value in dict1.items()}
 

# # lst_plus1 = [num_plus1(dict1) for dict1 in lst]

# lst_plus1 = [{key: value + 1 for key, value in dict1.items()}
#                              for dict1 in lst]
# print(lst_plus1)

# Given the following data structure return a new list identical 
# in structure to the original, but containing only the numbers
# that are multiples of 3.

# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]


# mupliples_of_3 = [[num for num in sublist if num % 3 == 0]
#                   for sublist in lst]

# print(mupliples_of_3)

# Given the following data structure, write some code to return a
# list that contains the colors of the fruits and the sizes of
# the vegetables. The sizes should be uppercase, and the colors
# should be capitalized.

# fruits_vegs_info = ['Red', 'Green', 'MEDIUM]

# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# def extract_info(plant_info):
#     if plant_info['type'] == 'fruit':
#         return [color.capitalize() for color in plant_info['colors']]
#     elif plant_info['type'] == 'vegetable':
#         return plant_info['size'].upper()

# fruits_vegs_info = [extract_info(plant_info) for plant_info in dict1.values()]

# print(fruits_vegs_info)

# Given the following data structure, write some code to return a list that contains
# only the dictionaries where all the numbers are even.

# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]

# def are_nums_even(dict1):
#     for value in dict1.values():
#         if not all([num % 2 == 0 for num in value]):
#             return False
        
#     return True

# even_num = [dict1 for dict1 in lst if are_nums_even(dict1)]

# print(even_num)

import random

# def create_uuid():
#     chars = 'abcdef0123456789'
#     lengths = [8, 4, 4, 4, 12]
#     uuid_sections = []

#     for length in lengths:
#         section = ''
#         for idx in range(length):
#             section += random.choice(chars)
#         uuid_sections.append(section)

#     return '-'.join(uuid_sections)

# def create_uuid():
#     chars = 'abcdef0123456789'
#     lengths = [8, 4, 4, 4, 12]
#     uuid_sections = []

#     for length in lengths:
#         section = [random.choice(chars) for _ in range(length)]
#         uuid_sections.append(''.join(section))
        
#     return '-'.join(uuid_sections)

# print(create_uuid())

# The following dictionary has list values that contains strings.
# Write some code to create a list of every vowel (a, e, i, o, u) 
# that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here


# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

VOWELS = 'aeiou'

# list_of_vowels = []

# for lst_of_words in dict1.values():
#     for word in lst_of_words:
#         for char in word:
#             if char in VOWELS:
#                 list_of_vowels.append(char)

list_of_vowels = [char for lst_of_words in dict1.values()
                       for word in lst_of_words
                       for char in word
                       if char in VOWELS
]
        
print(list_of_vowels)