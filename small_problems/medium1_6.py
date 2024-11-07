# A prime number is a positive number that is evenly divisible only by itself and 1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

# Write a function that takes a positive integer as an argument and returns true if the number is prime, false if it is not prime.

# You may not use any of Python's add-on packages to solve this problem. Your task is to programmatically determine whether a number is prime without relying on functions that already do that for you.
'''
input: positive integer
output: boolean True or False (repsents whether integer is prime or not)

rules:
- input integers are positive
- integer can be visually split by using `_`
- 1 is not prime number

DS: maybe list

ALG:
- if `input_number` is 1, return False
- iterate over the `num`  in range from 2 to (`input_number` / 2) + 1
    - if input_number % num == 0:
        - return False
- return True

'''

def is_prime(input_number):
    if input_number == 1:
        return False
    for num in range(2, input_number):
        if input_number % num == 0:
            return False
    
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True