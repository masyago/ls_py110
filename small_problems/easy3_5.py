# Write a function that takes a positive integer as an argument 
# and returns that number with its digits reversed.

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

'''
Problem
Write a fuction that reverses integer digits

Examples/Test Cases
- all numbers are positive
- all numbers are integers

Data Structures:
input: integer
output: integer
supporting:  list

Algorithm:
- convert integer to a list of numbers
- reverse the list
- convert reversed list to an integer
- return integer


Coding
'''

def reverse_number(number):
    num_lst = list(str(number))
    reverse_num_lst = num_lst[::-1]
    reverse_num = int(''.join(reverse_num_lst))
    return reverse_num

# Simplier solution
# def reverse_number(number):
#     return int(str(number)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
