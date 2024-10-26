# Write a function that takes a string argument and returns a list of
# substrings of that string. Each substring should begin with the first
# letter of the word, and the list should be ordered from shortest to
# longest.

# All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

'''
Problem
High-level description: Write a function that returns a list of substrings
that start with the first letter in input string.

input: string
output: list of substrings

rules:
 - explicit:
    - return a list of sustrings 
    - substrings start with the first characters in input string
    - order of substrungs in result should be from shortest to longest

 - implicit:
   - assume all characters in strings are letters
   - assume no empty strings

Data Structures:
 - return list

 Algorithm:
 - `string` given
 - initialize an empty list `result`
 - extract all substrings that start with first character
    - general formula for substring is `string[:idx + 1]`
    - iterate over idx in range from 0 to length of `string`
        - substring =  sliced `string` from first character to idx+1
        - add each substring to `result` list
- return result

'''

# def leading_substrings(string):
#     result = []
#     for idx in range(len(string)):
#         substring = string[:idx+1]
#         result.append(substring)
    
#     return result

def leading_substrings(string): #substrings that all start with the first character
    return [string[:idx+1] for idx in range(len(string))]

print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])