# Write a function that takes one argument, a positive integer, and
# returns the sum of its digits.

'''
Algorithm
- initialze variable `result` to value 0
- convert integer to string
- split string to a list
- sum elements of the list
- assign calculated sum to `result`
- return `result`

'''

# def sum_digits(num):
#     result = 0

#     for num in list(str(num)):
#         result += int(num)

#     return result

def sum_digits(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digits)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

