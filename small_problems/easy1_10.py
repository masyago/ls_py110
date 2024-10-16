DIGITS =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(integer):
    string = ''

    while integer > 0:
        integer, remainder = divmod(integer, 10)
        string = DIGITS[remainder] + string

    return string or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True