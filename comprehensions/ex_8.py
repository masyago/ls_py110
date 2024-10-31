# Write a comprehension that creates a dict object whose keys are strings and
# whose values are the length of the corresponding key.
# Only keys with odd lengths should be in the dict. Use the set given by my_set
# as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

def odd_lengths(test_set):
    return {element : len(element)
            for element in test_set
            if len(element) % 2 !=0 }

print(odd_lengths(my_set))
