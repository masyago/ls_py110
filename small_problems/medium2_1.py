# Write a function that takes a string and returns a dictionary containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

# You may assume that the string will always contain at least one character.

'''
input: string
output: dictionary where
                        keys are lowercase/uppercase/neither
                        values are % of chars that fall under the key groups

rules:
- dict values format: '0.00' to '100.00'
- string has at least 1 character

ALG:
- initialize dict `case_ratio` that contians 3 keys and '0' as values


- use 2 list comprehensions to create a list with only lower case chars, another list with upper casechar only

    
lower_percent = len(lower_chars) / len(string) * 100
upper_percent = len(upper_chars) / len(string) * 100

- reassign dict values:
- `case_ratio` with key lower reassign to value lower_percent as an f-string with needed formatting
- same for upper_count
- for key 'neither' value reassigned value is 100 minus (lower_percent + upper_percent). Formated as f-string with needed format.



'''

def letter_percentages(string):
    case_ratio = {'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "0.00",
    }

    lower_chars = [char for char in string if char.islower()]
    upper_chars = [char for char in string if char.isupper()]

    lower_percent = len(lower_chars) / len(string) * 100
    upper_percent = len(upper_chars) / len(string) * 100
    neither_percent = 100 - lower_percent - upper_percent

    case_ratio['lowercase'] = f'{lower_percent:.2f}'
    case_ratio['uppercase'] = f'{upper_percent:.2f}'
    case_ratio['neither'] = f'{neither_percent:.2f}'

    return case_ratio


    

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)