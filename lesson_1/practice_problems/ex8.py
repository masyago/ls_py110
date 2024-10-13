# Given the following string, create a dictionary that represents the frequency with which each letter occurs. 
#The frequency count should be case-sensitive

statement = "The Flintstones Rock"

# letter_count = {}

# for letter in statement.replace(" ",''):
#     letter_count[letter] = statement.count(letter)

# print(letter_count)

# LS solution:
char_freq = {}
statement = statement.replace(' ', '')
for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)