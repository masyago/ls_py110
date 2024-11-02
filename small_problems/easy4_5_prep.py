# Write a function that returns a list of all subsrtings
# of a given list.

#1. fucnt that extract all substr that start with specific 
    # element (ex first one)
#2. fuct that changes that element and goes over all of them


# def get_substr_same_start(string):
#     return [string[:idx + 1] for idx in range(len(string))]

# def get_all_substr(string):
#     all_substr =  [get_substr_same_start(string[idx:])
#             for idx in range(len(string))]

#     return [substring for substring_lst in all_substr
#                     for substring in substring_lst]
    

# print(get_all_substr('Rjhd123'))

'''
input: string
output: string with stagged caps

relues: 
- start with uppercase
- don't change case on non-alpha but consider to 
  determin upper/lower case

ALG
- initialize result = ''
- iterate over idx in len(string)
    - if idx % 2 == 0 and char.isalpha():
       - result += char.upper()
    - elif idx % 2 != 0 and char.isalpha():
        - result += char.lower()
    - else:
        - result += char
- return result

'''
def staggered_case(string):
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char

    return result



string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True