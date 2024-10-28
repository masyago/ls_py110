# Write a function that takes a string as an argument and returns a list that
# contains every word from the string, with each word followed by a space and
# the word's length. If the argument is an empty string or if no argument is
# passed, the function should return an empty list.

# You may assume that every pair of words in the string will be separated by 
# a single space.

# All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

'''
Algorithm
- initialize empty list `result`
- split `words` string into words, assign them to `word_list` list
- iterate over words in `word_list` -  this loop can be a list comprehension
    - initialize variable `word_count` to an empty string
    - use string inteprolation to assign word and length of word
     to `word_count`
     - add `word_count` to `result`
- return `result`

'''

def word_lengths(string=''):
    return [f'{word} {len(word)}' for word in string.split()
            if len(word) > 0]         # instead coult use if not string: return []


# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True