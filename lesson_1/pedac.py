"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

"""
input: string
output: list of substrings
rules:
    explicit requirements:
        - output list contains palindrom substrings that are 2+ characters from orginal strings
        - palindrome detection is case sensitive

    implicit requireements:
        - if string is empty, retrun an empty list
        - if the string doesn't have palindromes in it, return an empty list
        - if there are overlapping palindroms, add them all to the list
        - order of elements on the list for overlapping palindroms: based on first character
