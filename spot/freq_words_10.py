# Write a function that, given a string of text, returns a list of the top-3 most
# occurring words, in descending order of the number of occurrences.

# Assumptions:
# - A word is a string of letters (A to Z) optionally containing one or more apostrophes (').
# - Matches should be case-insensitive.
# - Ties may be broken arbitrarily.
# - If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty list if a text contains no words.

# Examples:
# top_3_words(" , e .. ") # ["e"]
# top_3_words(" ... ") # []
# top_3_words(" ' ") # []
# top_3_words(" ''' ") # []
# top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.""") # should return ["a", "of", "on"]


''''
Problem
Write a function that takes a string and returns top3 most common words in descending order of occurence

Examples/Test Cases:
- word is a string of letters and '
- case-insensetive comparison
- ties broken arbitrarily
- if less than 3 words, return top2/1 or an empty list

Data Structures:
input: string 
output: list 
supporting: dict for counts?

Algorithm:
- split string using whitespaces as delimiters
- generate a dict with all words as keys
- add 1 to corresponding value the word occurs
- generate list of values, sort them indescendign order
- generate a list of keys corresponding to top values

Coding
'''
def count_first(word_count):
    w, c = word_count
    return (c, w)

def top_3_words(string):
    top_3 = []
    words = string.split()
    words = [word.lower() for word in words]
    count_words = {}
    for word in words:
        if word not in count_words.keys():
            count_words[word] = 1
        elif word in count_words.keys():
            count_words[word] += 1
    words_items = list(count_words.items())
    sorted_words = sorted(words_items, key=count_first, reverse=True)

    
    for idx in range(3):
        top_3.append(sorted_words[idx][0])

    return top_3

print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))

