# The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

# Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:


'''
input: positive integer
output: positive integer that is the n-th Fibonacci number

rules:
- F(n) = F(n - 1) + F(n - 2)    (where n > 2)

DS: maybe list

ALG:
- fibonacci_list = [1, 1]
- if given `number` is 1 or 2, 
    - return 1

- iterate over n in range(3, number+1):
    - compute fib n-th number
    - append to the fib list 
    (fib_number = fibonacci_nums[n-2] + fibonacci_nums[n-3])
    - (fibonacci_nums.append(fib_num))


- return fibonacci_nums[n - 1]

'''
# def fibonacci(number):
#     fibonacci_list = [1, 1]

#     if number in [1, 2]:
#         return 1

#     for n in range(3, number + 1):
#         fib_number = fibonacci_list[n-2] + fibonacci_list[n-3]
#         fibonacci_list.append(fib_number)

#     return fibonacci_list[number - 1]

def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current

    return current
    
# nth = 3
# previous, current = 1, 2
# nth = 4
# prevoius, current = 2, 3

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True