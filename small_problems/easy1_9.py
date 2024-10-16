def string_to_integer(string):
    DIGITS = {'1' : 1,
              '2' : 2,
              '3' : 3,
              '4' : 4,
              '5' : 5,
              '6' : 6,
              '7' : 7,
              '8' : 8,
              '9' : 9,
              '0' : 0
              }
    value = 0
    for char in string:
        value = (10 * value) + DIGITS[char]

    return value


def string_to_signed_integer(string):
    if string[0] == '+':
        return string_to_integer(string[1:])
    elif string[0] == '-':
        return -string_to_integer(string[1:])
    else:
        return string_to_integer(string)
    
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True