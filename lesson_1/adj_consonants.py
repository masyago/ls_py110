"""

P: Understand the Problem

input: list of strings
output: a new list of sorted strings. The strings should be sorted based on the highest number of adjacent consonants a string contains.
rules:
    explicit:
    - strings should be sorted by the highest number of adjacent consonants
    - consonants are adjacent if they're next to each other in the same word or if there is a space between two consonants in adjacent words.
    - If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. 


    implicit:
    - strings may contain more than one word. can contain spaces

clarifying questions:
- handling empty strings/list of strings. No examples provided with empty strings
- consonant definition. Any letters other than a, o, u, e, i
- direction of sort order(ascending or descending). Descending
- upper and lower case handling, are they similar or different? No examples provided

E: Examples and Test Cases

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa'] 

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

D: Data Structures
- output is list of strings
- for keeping track of number of adj consonants: dictionary with elements 'string' : number of adj consotants

A: Algorithm
- initialize an empty dictionary
- Given a string, return a count of the highest number of adj consonant in the string
- add numbers to the dictionary
- sort strings based on how many adj consonants appeared
- extract dict values to a new string
- return that string

Sub-Algorithm for the step "Given a string, return a count of the highest number of adj consonant in the string":
Input: string
Output: number of adj consonants

Test cases:
print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjecc')) # 4
# """

# LS version. Using list sorting with a key instead of a dictionary
# def sort_by_consonant_count(strings):
#     strings.sort(key=count_max_adjacent_consonants, reverse=True)
#     return strings


def sort_by_consonant_count(given_list):
    number_tracker = {}
    for string in given_list:
        max_consonant_number = count_max_adjacent_consonants(string)
        number_tracker[string] = max_consonant_number
    sorted_number_tracker = dict(sorted(number_tracker.items(), key=lambda item: item[1], reverse=True))
    sorted_list = list(sorted_number_tracker.keys())

    return sorted_list

def count_max_adjacent_consonants(string):
    string_without_spaces = string.replace(" ","")
    max_consonants_count = 0
    adj_consonants_str = ''
    for letter in string_without_spaces:
        if letter in 'bcdfghjklmnpqrstvwxyz':
            adj_consonants_str += letter
            if len(adj_consonants_str) > max_consonants_count:
                if len(adj_consonants_str) > 1:
                    max_consonants_count = len(adj_consonants_str)
        else:
            if len(adj_consonants_str) > max_consonants_count:
                if len(adj_consonants_str) > 1:
                    max_consonants_count = len(adj_consonants_str)

            adj_consonants_str = ''
    return max_consonants_count




# print(count_max_adjacent_consonants('ddd    aa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4
# print(count_max_adjacent_consonants('xxxb')) # 4

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa'] 

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']