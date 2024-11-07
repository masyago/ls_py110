# # A featured number (something unique to this exercise) is an odd number that is a multiple of 7, 
# # with all of its digits occurring exactly once each. For example, 49 is a featured number, 
# # but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

# # Write a function that takes an integer as an argument and returns the next 
# # featured number greater than the integer. Issue an error message if
# #  there is no next featured number.

# # NOTE: The largest possible featured number is 9876543201.


# '''
# input: integer
# output: integer that is the next featured number less than 9876543201
#         - if such number doesn't exist, return Error Message
 

# rules:
# - featured number rules below (ALL have to be true):
#    - odd number
#    - divisible by 7
#    - no digits in the nubmer repeat. each occurs only once

# - max featured num is 9876543201


# DS:

# ALG:
# - MAX_FEATURED_NUMBER = 9876543201

# - starting_factor = given_number // 7

# - while number <= 9876543201:
#     - next number to try is (starting_factor + 1) * 7
#         - check if that num is odd. if yes, keep going
#         - iterate over digits in str representation of number:
#         - if count if larger not equals 1, need another iteration.
#                 - meaning starting_factor + 1
#             - if all conditions satisfied, return that number

#             - if no number, return Error message




# '''
# def is_featured_number(number):
#     featured_number_attributes = []

#     if number % 2 == 1:
#         featured_number_attributes.append(True)
#     else: 
#         featured_number_attributes.append(False)
    
#     digits = list(str(number))

#     if len(digits) == len(set(digits)):
#         featured_number_attributes.append(True)
#     else: 
#         featured_number_attributes.append(False)

#     return all(featured_number_attributes)



# def next_featured(starting_number):
#     MAX_FEATURED_NUMBER = 9876543201
#     MAX_MULTIPL_FACTOR = MAX_FEATURED_NUMBER // 7

#     multipl_factor = starting_number // 7

#     for factor in range(multipl_factor, MAX_MULTIPL_FACTOR):
#         factor += 1
#         number = factor * 7

#         if is_featured_number(number):
#             return number

#     return 'Error'


# LS solution

def to_od_multiple_of_7(number):
    number += 1
    while number % 2 == 0 or number % 7 != 0:
        number += 1

    return number

def all_unique(number):
    digits = list(str(number))
    return len(digits) == len(set(digits))

def next_featured(number):
    MAX_FEATURED_NUMBER = 9876543201

    featured_number = to_od_multiple_of_7(number)

    while featured_number <= MAX_FEATURED_NUMBER:
        if all_unique(featured_number):
            return featured_number
        
    return 'Error'
        

# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

