# Write a function that takes a string, doubles every consonant in the string, 
# and returns the result as a new string. The function should not double 
# vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

# You may assume that only ASCII characters will be included in the argument.

# All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

'''
Problem
Write a fucntion that doubles consonants only in the given string

Examples/Test Cases:
- empty string shold return empty string
- preserve character case

Data Structures:
input: string
output: sting
supporting: list comprehension

Algorithm:
- initialize a string consonants that contains all consonants
- iterate over char in string
    - if char (trasformed to lower case) is consonant, add double char to a new string
    - of char is not consonant, add signle char to a new string
- return the new string

Coding
'''
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def double_consonants(string):
    double_str = ''
    for char in string:
        if char.lower() in CONSONANTS:
            double_str += char * 2
        else:
            double_str += char

    return double_str

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")