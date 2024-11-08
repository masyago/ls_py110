# Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.


'''
input: positive integers
output: integer

rules:
- output is the result of substracting square of sum of all positive numbers until given number, incldung the given number, and sum of squares of those numbers

DS: ranges, lists

ALG:

- first_count_nums = list of integers in range(1, limit_num + 1)
- sq_first_count_nums -  use list comprehension 

- first_part = sum(first_count_nums)**2
- second_part = sum(sq_first_count_nums)

- return difference between first_part and second_part
'''

# def sum_square_difference(limit_num):
#     first_count_nums = list(range(1, limit_num + 1))
#     sq_first_count_nums = [num**2 for num in first_count_nums]
    
#     first_part = sum(first_count_nums)**2
#     second_part = sum(sq_first_count_nums)

#     return first_part - second_part


def sum_square_difference(count):
    sum_ = sum(range(1, count + 1))

    sum_of_squares = 0
    for i in range(1, count + 1):
        sum_of_squares += i**2
    
    return sum_**2 - sum_of_squares
    

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True