"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
# palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
# palindrome_substrings("palindrome") # []
# palindrome_substrings("")           # []
# palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
# palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]


'''
Problem
Write a fuction that returns all palindrome substings of a given string.

input: string
output: list of strings

rules:
    - explicit:
        - return a list of substrings that are palindromes
        - substrings should have as least 2 characters
        - palindromes are case sensitive

    - implicit
        - if input string doesn't contain any palindromes, return as empty list
        - empty string retruns an empty list
        - assume all characters in input string are letters

Data Structure:
- a list

Algorithm:
- initialize an empty list palindrome_lst
- create a list substr_lst that contains all substrings
      - iterate over substring in the lst:
            - if substing is a palindrome, add palindrome to palindrome_lst
- return palindrome_lst

1. substrings function
  problem: return list of all substrings of a string

  input: string
  output: list of substrings

  algorithm:
  - initiliaze empty list `result`
  - initialze `start_index` variable to 0 for the first character of substring
  - iterate over `start_index` from 0 through position of string length - 2
    - initialize `num_char` variable to `2` for the initial substing length
    - iterate from `num_char` to length of string - `start_index`
      - extract substring of that length starting at `start_index`
      - append extracted substring to `result`
      - increment `num_char` by 1
    - end of inner loop
    - increment `start_index` by 1
- End of outer loop
-Return `result`


Formal Pseudocode - not expected to use at assessments

START
/* Given a string named `string` */

SET result = []
SET start_index = 0

WHILE start_index <= (length of string - 2)
    SET num_chars = 2
    WHILE num_chars <= (length of string - start_index)
        SET substring = num_chars characters of string starting with start_index
        append substring to result list
        SET num_chars = num_chars + 1

    SET start_index = start_index + 1

RETURN result

END

2. is_palindrome function
- reverse given string and assing it to 'reverse_string'
- if string equals `reverse_string`:
    - return True
- else
    - return False
end if
  
'''


def substrings(string):
    result = []
    start_index = 0

    while start_index <= (len(string) - 2):
        num_chars = 2
        while num_chars <= (len(string) - start_index):
            substring = string[start_index:(start_index + num_chars)]
            result.append(substring)
            num_chars += 1
        start_index += 1
    
    return result

def is_palindrome(substring):
    return substring == substring[::-1]

def palindrome_substrings(string):
    result = []
    substrings_list = substrings(string)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result

print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]