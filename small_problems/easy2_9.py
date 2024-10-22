# Write a function that counts the number of occurrences of each element
# in a given list. Once counted, print each element alongside the number
# of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

'''
Problem
White a function that counts unique words (case sensitive) in given list.

Examples/Test Cases
- "suv" != "SUV"

Data Structures
input: list
output: dictionary printed nicely

Algorithm
- use dictionary comprehension 
    - expression word, list.count(word)
    - for word in given list
- print key and value in dict(key, value)

Coding

'''

def count_occurrences(vehicles):
    count_dict = {word: vehicles.count(word) for word in vehicles}
    for key, value in count_dict.items():
        print(f'{key} => {value}')

    return count_dict

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

(count_occurrences(vehicles))