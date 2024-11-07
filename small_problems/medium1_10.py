'''
input: integer that represents number of digits in Fib num
output: integer that represents index in first Fib num with input number of digits

rules:
- input integer is always greater than or equal to 2


ALG:
- compute Fib numbs until lenth of Fib num is `target_lenth`
- return n of Fib num
'''

def find_fibonacci_index_by_length(length):
    first = 1
    second = 1
    count = 2

    while len(str(second)) < length:
        first, second = second, second + first
        count += 1

    return count

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)