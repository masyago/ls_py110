# Write a function that takes a string as input and counts the occurrences of each
# lowercase letter in the string. Return the counts in a dictionary where the
# letters are keys and their counts are values.

# letter_count('launchschool') #=> { ’a’: 1, ‘c’: 2, ‘h’: 2, ‘l’: 2, ‘o’: 2, ‘u’: 1 }

'''
Problem
Take string as input, count each letter, return a dictionary with counts

Examples/Test Cases
- all letters are lower case
- string is not empty
- string contains only letters

Data Structures
input: list of letters as strings
output: dictionary where  key-value pairs are 'letter'- count 

Algorithm
- create an empty dict
- iterate over letters in string
    - check if key already in the dict.
        - if yes, add 1 to value
    - if key is not in the dict:
        - add key/value pair to dict
        - (key is letter, value is 1)

- return the dict

Coding

'''

def letter_count(string):
    letter_occurence = {}
    for char in string:
        if char.islower():
            if char in letter_occurence.keys():
                letter_occurence[char] += 1
            else:
                letter_occurence[char] = 1

    return letter_occurence

print(letter_count('AAbbCcC'))