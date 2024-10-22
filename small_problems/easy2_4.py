'''
Problem
given a list with one element repeated twice, find and return the duplicate value

Examples/Test Cases
- all values are int
- only one value is a duplicate

Data Structures:
- input: list
- output: integer

Algorithm:
- iterate over elements to find duplicate

Coding:
'''
# def find_dup(lst):
#     for number in lst:
#         if lst.count(number) == 2:
#             return number

def find_dup(lst):
    dups = [number for number in lst if lst.count(number) == 2]
    return dups[0]

print(find_dup([1, 5, 3, 1])  == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True