# Write a function that takes a list of strings and returns a list of the same
# string values, but with all vowels (a, e, i, o, u) removed.

# All of these examples should print True

'''
Algorithm
- initialize variable that contains all vowels: vowel = 'aeiou`
- initialize an empty string `result` 
- iterate over characters in `original` string 
    - if character not in`vowel`
        - add character to `result`
- return `result`

'''

# def remove_vowels(original_lst):
#     result = []
#     vowels = 'aeiouAEIOU'

#     for string in original_lst:
#         new_string = ''
#         for char in string:
#             if char not in vowels:
#                 new_string += char
#         result.append(new_string)
#     return result

VOWELS = 'aeiouAEIOU'

def strip_vowels(string):
    no_vowels = [char for char in string
                 if char not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(original_lst):
    return [strip_vowels(string)
            for string in original_lst]


original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']

print(remove_vowels(original) == expected)        # True
