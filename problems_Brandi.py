def every_third(lst, start):
    # Your implementation here

my_list = [1, 2, [], 4, 2, 'f', 'g', 'h']
print(every_third(my_list, 1))  # [2, 2, 'h']
print(every_third(my_list, 2))  # [[], 'f']


###

target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

# ???

# {
#     'a': { 'present': True, 'count': 1 },
#     'b': { 'present': True, 'count': 2 },
#     'c': { 'present': False, 'count': 0 },
#     'd': { 'present': True, 'count': 1 },
#     'e': { 'present': False, 'count': 0 },
# }


###


# Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order.
# Whitespace and punctuation shall simply be removed!
# The input is restricted to contain no numerals and only words containing the english alphabet letters.

def alphabetized(string):


# Tests
print(alphabetized("The Holy Bible") == "BbeehHilloTy")
print(alphabetized("!@$%^&*()_+=-`,") == "")
print(alphabetized("CodeWars can't Load Today") == "aaaaCcdddeLnooorstTWy")