# Write a function that takes a string as an argument 
# and returns that string with every occurrence of a 
# "number word" -- 'zero', 'one', 'two', 'three', 'four',
# 'five', 'six', 'seven', 'eight', 'nine' -- converted to 
# its corresponding digit character.

# You may assume that the string does not contain any punctuation.


'''
Problem
Write a funciton that convert word numbers in the string to 
integers

input: string
output: string with corresponding integers
intermediate DS: dictionary, lists

ALG
- initialize a dict `numbers` with contains number words and integers
- convert input string to a `word_list`
- iterate over words in word_list
    - if word found in dictionary `numbers`:
        - replace word with the number in word_list
- convert word_list into a str with space as separator
- return result



'''

NUMBERS = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

# def word_to_digit(string):
#     word_list = string.split()
    
#     for idx in range(len(word_list)):
#         if word_list[idx] in NUMBERS.keys():
#             word_list[idx] = NUMBERS[word_list[idx]]

#     return ' '.join(word_list)


def word_to_digit(string):
    word_list = string.split()
    processed_words = [NUMBERS.get(word, word) for word in word_list]
    return ' '.join(processed_words)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True