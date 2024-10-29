# Write a function that takes a string as an argument and returns that 
# string with a staggered capitalization scheme. Every other character, 
# starting from the first, should be capitalized and should be followed
# by a lowercase or non-alphabetic character. Non-alphabetic characters
# should not be changed, but should be counted as characters for 
# determining when to switch between upper and lower case.

'''
P
Write a function that returns a string with staggerred captitalization
scheme.

E
rules:
- empty string returns empty string
- string consistes of mix of letters, upper and lower case, 
  digits, spaces, special characters
- only letters will be changed
- however, non-letters are counted as well to determine
  case of the next letter
- result string starts with capital letter

  D
  input: string
  output: string with staggered cases
  intermediate: potentially list(s)

  A
  - initialize empty string `result`
  - iterate over indexes in range len(string)
      - if index % 2 == 0:
         - apply upper() method to char at index position
           and add the char to `result
      - if index % 2 != 1:
          - add char.lower() at index position to `result`
- return `result`


 C
'''


def staggered_case(string):
    result = ''
    for idx in range(len(string)):
        if idx % 2 == 0:
            result += string[idx].upper()
        elif idx % 2 == 1:
            result += string[idx].lower()

    return result

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string)  == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True