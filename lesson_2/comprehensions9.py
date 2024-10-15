# Given the following data structure, write some code to return a list 
# that contains only the dictionaries where all the numbers are even.
# Expected output: [{e: [8], f: [6, 10]}]

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def all_even(dictionary):
    for values in dictionary.values():
        if not all([num % 2 == 0 for num in values]):
            return False
        
    return True

result = [element for element in lst if all_even(element)]
print(result)