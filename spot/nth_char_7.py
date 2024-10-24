# Write a function that takes a list of words and constructs a new word by
# concatenating the nth letter from each word, where n is the position of the
# word in the list.

# Example:
# nth_char(['yoda', 'best', 'has']) # should return 'yes'


def nth_char(words):
    nth_word = ''
    for idx in range(len(words)):
        nth_word += words[idx][idx]

    return nth_word

print(nth_char(['yoda', 'best', 'has']))
