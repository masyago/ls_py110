# Remove all duplicate letters from a string, keeping only the first occurrence.
# The input is restricted to contain no numerals and only words containing the English alphabet letters.

# You may not use a set.


# def remove_duplicates(string):
#     # Implementation


# '''
# input: string 
# output: string with duplicare letters removed

# rules:
# - can't  use sets
# - case insensitive
# - string contains only english letters (no numbers)

# ALG:
# - initialize `result` = ''

# - iterate over chars in string:
#     - if not `result`:
#          - result += char
#     - if char.lower() not in result.lower():
#           - result += char
#  - return result
# 

# def remove_duplicates(string):
#     result = ''
#     for char in string:
#         if not result:
#             result += char
#         elif char.lower() not in result.lower():
#             result += char
#     return result

# # Tests
# print(remove_duplicates("Launch School") == "Launch So")
# print(remove_duplicates("CodeWars can't Load Today") == "CodeWars n'tLy")
# print(remove_duplicates("success") == "suce")

# ----

# Solve it using comprehension

target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

# ???

# {
#     'a': { 'present': True, 'count': 1 },
#     'b': { 'present': True, 'count': 2 },
#     'c': { 'present': False, 'count': 0 },
#     'd': { 'present': True, 'count': 1 },
#     'e': { 'present': False, 'count': 0 },
# }

'''
DS:
outer_dict: key is letter from target letters
            value is inner_dict

inner_dict: 2 key/values
          1
          key: 'present'
          value: True/False  whther letter exists in characters

          2
          key: 'count'
          value: count of letter in characters


'''

def letter_count(lst1, lst2):
    outer_dict = {letter: {'present' : letter in lst2, 
                           'count': lst2.count(letter)}
                           for letter in lst1}
    return outer_dict


print(letter_count(target_letters, characters))