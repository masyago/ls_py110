# Write a function that takes one argument, a list of integers,
# and returns the average of all the integers in the list, 
# rounded down to the integer component of the average. 
# The list will never be empty, and the numbers will always 
# be positive integers.

# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True


'''
Problem
Write a funciton that calculates average of integers in the list.
Rounds down average to output integer.


Examples/Test Cases
- no empty lists
- all integers are positive numbers

Data Structures
input: list of integers
output: integer (round down)

Algorithm
- average = (sum of integers in the list) // (number of integers in the list). 
- return average

Coding
'''

def average(lst):
    average = sum(lst) // len(lst) # // is a floor division operator
    return average

print(average([1, 5, 87, 45, 8, 8]) == 25)       # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True