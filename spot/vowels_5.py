# Write a function that takes a lowercase string as input and returns the
# length of the longest substring that consists entirely of vowels (a, e, i, o, u).

# Examples:
# solve("roadwarriors") # should return 2
# solve("suoidea") # should return 3

'''
PEDAC

Problem
Write a function that takes a string and returns length of longest substing of vowels.

Examples/Test Cases
- all letters are lower strings. no need to worry about case
- vowels are 'aeiou'


Data Structures
input: string
output: integer
supporting/intermediate: 
- string of vowels
- list of counts?

Algorithm
- initialize vowels string 'aeiou'
- initialize empty string longest_vowels 
- initialze counts list 
- iterate over char in given string
    - if char in vowels and longest_vowels is empty:
        - add char to longest_vowels
    - if char in vowels:
        - if last char of longest_vowels is vowel:
            - add char to longest_vowels
        - else:
            - add length of longest_vowels to counts list 
            - reassign longest_vowels to char
    - if char not in vowels:
        - add length of longest_vowels to counts list (if not 0)
    - determine highest integer in counts
    - return the highest integer


Coding

'''
VOWELS = 'aeiou'

def solve(string):
    longest_vowels = ''
    counts = []

    for char in string:
        if char in VOWELS:
            if not longest_vowels:
                longest_vowels += char
            elif longest_vowels[-1] in VOWELS:
                longest_vowels += char
            else:
                counts.append(len(longest_vowels))
                longest_vowels = char
        else:
            counts.append(len(longest_vowels))
            longest_vowels = char

    longest = max(counts)
    return longest



print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3