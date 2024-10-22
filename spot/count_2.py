# Write a function that takes a list of integers as input and counts the number of
# pairs in the list. A pair is defined as two equal integers separated by some
# other integer(s).

# Examples:
# pairs([1, 2, 5, 6, 5, 2]) # --> 2
# pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) # --> 4


'''
Problem
Write a function that takes a list of integers and returns number of duplicate integers in the list

Examples/Test Cases
- all elements of the list are integers
- assume given lists are not empty

Data Structure
input: list of integers
output: integer

intemediate: dictionary to count occurrences

Algorithm
- initialiaze an empty dict
- iterate over integers in list
    - if integer not in the the dict yet, add to the dict. add 1 as value
    - if intgeer is already in the dict, increase value by 1
- count values in 2 increments
- return the count

Coding

'''

def pairs(lst):
    dict = count_int(lst)
    count = 0
    for value in dict.values():
        if value >= 2 and value % 2 == 0:
            count += (value // 2) 

    print(count)

def count_int(lst):
    dict = {}

    for number in lst:
        if number not in dict.keys():
            dict[number] = 1
        elif number in dict.keys():
            dict[number] += 1
        

    return dict


# print(pairs([1, 2, 5, 6, 5, 2])) # --> 2
# print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2])) # --> 4

# count_int([1, 2, 2, 20, 6, 20, 2, 6, 2])
# pairs([1, 2, 2, 20, 6, 20, 2, 6, 2])
