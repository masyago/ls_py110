# Write a function that rotates the last count digits of a number.
# To perform the rotation, move the first of the digits that you 
# want to rotate to the end and shift the remaining digits to the left.


'''
Problem: Write a function that returns integer with one of the digits
moved to the end of the integer (position on the integer ID'd by second
 argument), all other digits simply moved ot the left.

input: 2 integers
  1. given integer
  2. position of digit we need to move, counting from the right side of 
    given integer 1

output: another integer
intermidiate DS: string

rules:
- 2 integers are always provided
- no zero positions


ALG:
- initialize variable `result`
- extract digit that will be moved
- using slicing, assign the rest of integer turned to str to 
`result`
- concatenate moved digit to the end of `result`
- return `result` converted to an integer

'''

# def rotate_rightmost_digits(original_int, position):
#     result = ''
#     str_int = str(original_int)
    
#     if position == 1:
#         return original_int
#     else:
#         digit_to_move = str_int[-position]
#         result = str_int[:-position] + str_int[-position + 1:] + digit_to_move
#         return int(result)


def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def rotate_string(string):
    return string[1:] + string[0]


print(rotate_rightmost_digits(735291, 2)  == 735219)  # True   
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3)  == 1002)      # True