"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

# Comments show expected return values
# change_me("We will meet at noon")       # "We will meet at NOON"
# change_me("No palindromes here")        # "No palindromes here"
# change_me("")                           # ""
# change_me("I LOVE mom and dad equally") # "I LOVE MOM and DAD equally"

'''
Problem
Write a function that turns palindromes uppercase in the given string

input: string
output: a new string

rules:
    explicit:
    - palindromes should be uppercase in return string
    - given an empty string output is an empty string
    - if there're already words that are uppercase but palindromes,
      keep them uppercase

      Question for interviwer: are palindromes case sensitive? 
      Is Mom a palindrom?

    implicit:
    - assume stings contain only letters from english alphabet and spaces
    - assume all inputs are strings
    - words are separated by spaces

Data Structures
- input and output are both strings
- output is a new string
- intermediate data structures: list of words

Algorithm
- initialize empty palindrome_lst
- split given string into words_lst
- iterate over word in the list via indexes
    - if word equals word with reversed order of characters
        - add word with all letters changes to uppercase to palindrome_lst
    - for non-palindromes:
        - add word to palindrome_lst
- return palindrome_lst that was converted to a string

Coding

'''

def change_me(string):
    palindrome_lst = []
    words_lst = string.split()
    for idx in range(len(words_lst)):
        if words_lst[idx] == words_lst[idx][::-1]:
            palindrome_lst.append(words_lst[idx].upper())
        else:
            palindrome_lst.append(words_lst[idx])
    return ' '.join(palindrome_lst)


print(change_me("We will meet at noon"))       # "We will meet at NOON"
print(change_me("No palindromes here"))        # "No palindromes here"
print(change_me(""))                     # ""
print(change_me("I LOVE mom and dad equally")) # "I LOVE MOM and DAD equally"