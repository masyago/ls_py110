DIGITS =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(integer):
    string = ''
    integer = abs(integer)

    while integer > 0:
        integer, remainder = divmod(integer, 10)
        string = DIGITS[remainder] + string

    return string or '0'

def signed_integer_to_string(integer):
    if integer > 0:
        return '+' + integer_to_string(integer)
    elif integer < 0:
        return '-' + integer_to_string(integer)
    else:
        return '0'
    
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

