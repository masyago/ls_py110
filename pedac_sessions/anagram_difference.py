'''
Problem: Anagram Difference
high-level problem statement

E
rules:
- if both inputs 
- we can remove letters for either word
- the order of strings in arguments don't matter
- inputs are lowercase only, no need to worry about cases

D
inout: two strings
outpout: integer
intemediate:
- array/list to iterate over stringsdict to store accurence of eahc letter

Algorithm
- iterate through each key and work out how many letters we need to remove
  don't miss letters with zero frequency

- Other generate all possible substring. Select substring that have a match
 in the array of substring. Get the largest substring. Substack size of anagram 
+
-
Natasha
- - initialize a dict of all letters in alphabet. associated value for each letter
  is a list with two elements. {'a' :[0, 0], } )good to show in the algorithm how 
  it'd look like, esp to intermediate data structures
  first element will correspond to letter count in first string, 
  second element will correspond to letter count in second string
- iterate over letters in first string, add counts for each letter to first element in the list
- repeat to second string. this can be a helper function
- if all elements in the lists are zero, return 0
- iterate over dictionary
    - substract elements in the lists. find absolute difference
    - sum result
- return result


['a', 'b']
[1, 0]
[2, 3]


'''

'''
Problem itself
Given two words, how many letters do you have to remove from them to make them anagrams?
'''

# Coding
# communicate in plain english what you'r doing'
# test frequently

def create_alphabet_count():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = {}
    for char in alphabet:
        count[char] = [0,0]
    return count

def anagram_difference(str1, str2):
    count = create_alphabet_count()
    for letter in str1: 
        count[letter][0] += 1

    for letter in str2:
        count[letter][1] += 1
    
    anagram_letters = {}
    for key, value in count.items():
        if value != [0,0]:
            anagram_letters[key] = value

    for key, value in anagram_letters.items():
        anagram_letters[key] = abs(anagram_letters[key][0] - anagram_letters[key][1])

    result = 0
    for value in anagram_letters.values():
        result += value

    return result


# // # Python test cases
print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('a', 'aab') == 2)
print(anagram_difference('codewars', 'hackerrank') == 10)
print(anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42)
print(anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50)