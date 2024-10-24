# Write a function that takes a string, doubles every character
# in the string, then returns the result as a new string.

# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

'''
Problem
Write a function that returns a new string containing all elements
from given string doubled.

Examples/Test Cases
- empty string should return empty string
- all characters (not just letters) are doubled.
 It includes spaces, explamantion marks

 Data Structures
 input: string
 output: string
 supporting? 

 Algorithm
- initialize empty string double_char
- iterate over every char in the given string
    - add double char to double_char string
- return double_char string
OR

- use list comprehension to create a list of double char
    - expression: char * 2
    - iterable: for char in string

- then join elements of the list to a string

Coding
'''
# Non list comprehension solution
# def repeater(string):
#     double_char = ''
#     for char in string:
#         double_char += char * 2

#     return double_char

# List comprehension solution
def repeater(string):
    double_lst = [char * 2 for char in string]
    double_char = ''.join(double_lst)
    return double_char

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
