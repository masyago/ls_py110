# Write a function that returns a list of all palindromic substrings of a string. 
# That is, each substring must consist of a sequence of characters that reads
# the same forward and backward. The substrings in the returned list should be 
# sorted by their order of appearance in the input string. Duplicate substrings
# should be included multiple times.

# You may (and should) use the substrings function you wrote in the previous
# exercise.

# For the purpose of this exercise, you should consider all characters and 
# pay attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 
# 'Abc-bA' are not. In addition, assume that single characters are not palindromes.

# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

'''
Problem
High-level description: Write a function that takes a string and returns
a list of only palindrome sustrings from that string.

input: string
output: list of substrings that are palindromes

rules:
- explicit:
  - return list of substrings that are palindromes
  - length of palindromes is >= 2
  - use case sensitive comparisons
  - order of substrings in result list is the same as order of occurence 
   original string
 - duplicate substrings included multiple times

- implicit:
  - if there are no palindorms in the `string`, return empty list
  - special characters can be part of the string and 
   can be part of palindromes

Data Structure:
list

Algorithm:
- initialize an empty list 'result`
- extract all substrings from the `string`
- iterate over substrings
    - check if substring is palindrome:
        - if yes, add substring to `result`
- return result


'''

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    return [
        substring
        for idx in range(len(string))
        for substring in leading_substrings(string[idx:])
    ]

def is_palindrome(substring):
    return len(substring) > 1 and substring == substring[::-1]

# def palindromes(string):
#     result = []
#     for substring in substrings(string):
#         if is_palindrome(substring):
#             result.append(substring)
    
#     return result

def palindromes(string):
    return [substring 
            for substring in substrings(string)
            if is_palindrome(substring)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True
print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True