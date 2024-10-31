# Write a function that computes and returns the factorial of a number
# by using a for or while loop. The factorial of a positive integer n,
# signified by n!, is defined as the product of all integers between 1 and n, inclusive.
# You may assume that the argument is always a positive integer.

n = int(input('Type a positive integer '))

# Using while loop
def get_factorial_while_loop(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Using for loop
# def get_factorial_for_loop(n):
#     result = 1
#     for number in range(1, n+1):
#         result = result * number
#     return result


print(get_factorial_while_loop(n))
#print(get_factorial_for_loop(n))
