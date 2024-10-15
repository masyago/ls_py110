# Write some code to create a list of every vowel (a, e, i, o, u)
#  that appears in the contained strings, then print it.
# Exprected output: ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']


dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# for loops solution
# vowels = 'aeiou'
# list_of_vowels = []
# for list_of_words in dict1.values():
#     for word in list_of_words:
#         for char in word:
#             if char in vowels:
#                 list_of_vowels.append(char)

# print(list_of_vowels)

# List comprehension solution
vowels = 'aeiou'
list_of_vowels =[char for list_of_words in dict1.values()
                      for word in list_of_words
                      for char in word if char in vowels]

print(list_of_vowels)


