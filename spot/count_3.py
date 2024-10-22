# Write a function that takes two strings as input, `full_text` and `search_text`,
# and returns the number of times `search_text` appears in `full_text`.

# Examples:
# solution('abcdeb','b') # should return 2 since 'b' shows up twice
# solution('aaabbbcccc', 'bbb') # should return 1

'''
Problem
Write a function that counts number of appearance on substring in a strting.

Examples/Test Cases
- both search_text and full_text are not empty
- search_text in present in full_text. no need to handle case
 when seach text is not present

Data Structures
input: 2 strings
output: integer

Algorithm
- use str method count to get the needed count

Coding

'''

def solution(full_text, search_text):
    return full_text.count(search_text)

print(solution('abcdeb','b')) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb')) # should return 1
print(solution('soiulfcneruighrh', '1'))