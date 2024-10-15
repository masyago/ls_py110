# Given the following data structure return a new list identical in 
# structure to the original, but containing only the numbers that are 
# multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# def mupliples_of_3(sublist):
#     mult3_num = [num for num in sublist if num % 3 == 0]
#     return mult3_num

# new_list = [mupliples_of_3(sublist) for sublist in lst]

# One-liner
new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
print(new_list)