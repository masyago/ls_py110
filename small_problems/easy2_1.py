''' PEDAC  
P: Understand the Problem
E: Examples / Test cases
D: Data Structures
A: Algorithm
C: Code


P: Understand the Problem. Write high-level description in you own words
Write a function that takes angles expressed in floating numbers and 
converts them to degrees, minutes, and seconds

E: Examples and Test Cases
- numbers without decimals (whole numbers) should output 00 minutes and 00 seconds
- format of the output is 76°43'48"
- zero outputs 0°00'00"
- 360 outputs 360°00'00"
- no need to trasform whole number for the angles (ex 270 outputs 270 and not (270 - 90))


D: Data Structures
Strings

A: Algorithm
- initialize an empty string s to store result
- degrees value: extract value before decimal and concatenate it to the string s. 
 concant degree sign to the end
- subtract that value from input number num
- multiply num by 100
- calculate minutes: (60 * (num / 100)). round to whole number. maybe need to use integer division?
  concat to string s, concat ' sign at the end
- subtract the minutes value from result of (60 * (num / 100))
- repeat steps:
    - - multiply num by 100
    - - calculate minutes: (60 * (num / 100)). round to whole number.
- concat seconds value and seconds sign to the string
- return the string

'''
DEGREE = "\u00B0"

def modify_angle_num(angle_num):
    while int(angle_num) < 0 or int(angle_num) > 360:
        if int(angle_num) < 0:
            angle_num = 360 + int(angle_num)
        elif int(angle_num) > 360:
            angle_num = int(angle_num) - 360

    return angle_num


def format_zeros(number):
    num_str = str(number)
    if len(str(number)) < 2:
        return '0' + num_str
    else:
        return num_str

def dms(angle_num): # 76.73
    angle_num = modify_angle_num(angle_num)
    degrees = int(angle_num)
    minutes = int((angle_num - degrees) * 60) # 43
    seconds = int((angle_num - degrees - (minutes / 60)) * 60 * 60) # 48
    return (f"{degrees}{DEGREE}"
          f"{format_zeros(minutes)}'"
          f'{format_zeros(seconds)}"')


# All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"