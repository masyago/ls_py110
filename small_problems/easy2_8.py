# Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

'''
Problem
Write a function that returns a list of digits of given integer

Examples/Test Cases
- should we handle negative numbers?

Data Structures
input: integer
output: list of integers
supporting N/A

Algorithm
- convert given integer to str

Use list comprehension
- expression int(char) 
- for char in given string
- do we need to convert chars to int?

'''

def digit_list(integer):
    return [int(char) for char in str(integer)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True