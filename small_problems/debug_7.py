def sum_numbers(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_numbers(numbers, 2) == 20)