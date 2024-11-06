# Take the number 735291 and rotate it by one digit to the left, getting 352917.
# Next, keep the first digit fixed in place and rotate the remaining digits
# to get 329175. Keep the first two digits fixed in place and rotate again
# to get 321759. Keep the first three digits fixed in place and rotate again 
# to get 321597. Finally, keep the first four digits fixed in place and 
# rotate the final two digits to get 321579. The resulting number is called
# the maximum rotation of the original number.

# Write a function that takes an integer as an argument and returns the 
# maximum rotation of that integer. You can (and probably should) use
# the rotate_rightmost_digits function from the previous exercise.


'''
Problem
Write a function that returns an integer that is called max rotation of
given number.

input: integer
output: integer
intermediate DS: strings

ALG
- initializr `result` to empty string
- convert int to str
- iterate over counts in the str_number from 0 to len(str_num) - 1:
    - rotate string each time



'''

def max_rotation(number):
    number_str = str(number)

    for count in range(len(number_str) - 1):
        number = (rotate_rightmost_digits(number, count))
        print(number)

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def rotate_string(string):
    return string[1:] + string[0]


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True