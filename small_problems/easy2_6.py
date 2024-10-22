'''
Problem
Write a funciton that calculate multoplicative average of elements in given list.
Return result with 3 decimal points

Examples/Test Cases
- assume all list elements are numbers
- assume given list is not empty

Data Structures
input: list
output: float with three decimal places

Algorithm
- multiply all elements of the list
- divide by length of the list
- round result to three decimal points

Coding

'''

def multiplicative_average(lst):
    product = 1
    for number in lst:
        product *= number
    average = product / len(lst)

    return(f'{average:.3f}')



# print(multiplicative_average([2, 5, 8]))
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")