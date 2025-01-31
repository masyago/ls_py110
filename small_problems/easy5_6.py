# Write a function that takes a list of numbers and returns the sum of the sums
# of each leading subsequence in that list. Examine the examples to see what we
# mean. You may assume that the list always contains at least one number.

'''
Algorithm
- initialize variable `result` and assign to value `0`
- iterate over indexes in range up to length of the input_list
    - slice `input_list` from beginning up to index + 1 (so it includes the index)
    - sum elements of the slice
    - add calculated sum to `result`
- return result
'''

# def sum_of_sums(lst):
#     result = 0

#     for idx in range(len(lst)):
#         result += sum(lst[:idx + 1])
    
#     return result


print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True


