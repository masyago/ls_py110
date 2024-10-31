# Write a function that takes a string of digits and returns the appropriate
# number as an integer. You may not use any of the standard conversion 
# functions available in Python, such as int. Your function should calculate
# the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry
# about invalid characters; assume all characters are numeric.


# def string_to_integer(string):
#     DIGITS = {
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#     }

#     value = 0
#     value = 0
#     for char in string:
#         value = (10 * value) + DIGITS[char]

#     return value

# def string_to_signed_integer(string):
#     if string[0] == '+':
#         return string_to_integer(string[1:])
#     elif string[0] == '-':
#         return -string_to_integer(string[1:])
#     else:
#         return string_to_integer(string)

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True


# def integer_to_string(num):
#     DIGITS = {
#         0: '0',
#         1: '1',
#         2: '2',
#         3: '3',
#         4: '4',
#         5: '5',
#         6: '6',
#         7: '7',
#         8: '8',
#         9: '9',
#     }

#     str_num = ''
#     if num == 0:
#         return '0'
    
#     while num > 0:
#         digit = num % 10
#         num = num // 10
#         str_num += DIGITS[digit]
    
#     return str_num[::-1]



# print(integer_to_string(4321)  == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True


# Write a function that takes a string consisting of zero or more
# space-separated words and returns a dictionary that shows the
# number of words of different sizes.

# Words consist of any sequence of non-space characters.

# All of these examples should print True

'''
input: string
output: dictionary

A
- initialize an empty dict `word_len_count`
- split string into words, assign result to `word_list`
- iterate over words in `word_list`
    - add key/value to dict where key is word len and 
     value is incremented by 1
- return `word_len_count`

'''

# # Modify the word_sizes function from the previous exercise
# # to exclude non-letters when determining word size. 
# # For instance, the word size of "it's" is 3, not 4.


# def word_sizes(string):
#     word_len_count = {}
#     word_list = string.split()
#     letters_only_list = []

#     for word in word_list:
#         letters = [char for char in word if char.isalpha()]
#         letters_only_list.append(letters)

#     for new_words in letters_only_list:
#         word_len_count[len(new_words)] = word_len_count.get(len(new_words), 0) + 1
    
#     return word_len_count

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# Given a string of words separated by spaces, write a function that
# swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and
# that the string will always contain at least one word. You may also
# assume that each string contains nothing but words and spaces, and
# that there are no leading, trailing, or repeated spaces.


'''
input: string of words
output: string where words have swapped letters

rules:
- strings contain only letters and spaces
- string is not emprty and has at least one word

ALG
- initiliaze `swapped_words` to empty list
- split input string to words, assign result to
  `word_list`
- iterate over words in word_list
    - if length of word  > 2:
        - swap first and last letters
        - add result to `swapped_words'
    - otherwise add word to `swapped_words'
- convert `swapped_words' to a string with space separator
- return the string

'''

# def swap(string):
#     swapped_words = []
#     word_list = string.split()

#     for word in word_list:
#         if len(word) > 1:
#             updated_word = word[-1] + word[1:-1] + word[0]
#             swapped_words.append(updated_word)
#         else:
#             swapped_words.append(word)

#     return(' '.join(swapped_words))


# print(swap('Oh what a wonderful day it is')
#      == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True


# ```python
# def is_palindrome(string):
#     return string == string[::-1]

# def is_real_palindrome(string):
#     letters_only = ''
#     for char in string:
#         if char.isalnum():
#             letters_only += char.casefold()

#     return is_palindrome(letters_only)

# ```



# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True


'''
input: list of numbers
output: list of numbers


# '''
# ```python
# def running_total(lst):
#     result = []

#     for idx in range(len(lst)):
#         if not result:
#             result.append(lst[idx])
#         else:
#             result.append(lst[idx] + result[-1])

#     return result

# ```

# print(running_total([2, 5, 13]) == [2, 7, 20])  # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True