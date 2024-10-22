# Write a function that takes a list of words as input and returns a list of
# integers. Each integer represents the count of letters in the word that occupy
# their positions in the alphabet.

# Examples:
# solve(["abode","ABc","xyzD"]) # should return [4, 3, 1]
# solve(["abide","ABc","xyz"]) # should return [4, 3, 0]

'''
PEDAC

Problem
Write a function that takes a list of words and returns a list of integers.
Integers represent how many letters in the words are in the same positions as in alphabet
(ex a should have position 1 in word to be counted)

Examples/Test Cases
- case insensitive


Data Structures
input: list of words
output: list of integers
intermediate: string of alphabet letters

Algorithm
- initialize alphabet string that contains all letters in alphabetical order
- initialize aplha_positions empty list
- iterate over words in list
    - initialize count to 0
    - iterate over letters (lower case transformed) in words
        - if position of letter in the word and in alphabet are equal, 
          add 1 to count
    - append count to aplha_positions list
- return aplha_positions list

Coding

'''
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def solve(lst):
    alpha_positions = []
    for words in lst:
        words = words.lower()
        count = 0
        for letter in words:
            if words.index(letter) == ALPHABET.index(letter):
                count += 1
        alpha_positions.append(count)

    return alpha_positions



print(solve(["abode","ABc","xyzD"])) # should return [4, 3, 1]
print(solve(["abide","ABc","xyz"])) # should return [4, 3, 0]