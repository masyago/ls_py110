# Modify the function from the previous exercise so it ignores non-alphabetic
# characters when determining whether it should uppercase or lowercase each 
# letter. The non-alphabetic characters should still be included in the return
# value; they just don't count when toggling the desired case.


'''
A
- initialize empty string `result`
- initialize variable `upper` to boolean True
 - iterate over chars in string
    - if char isalpha:
        - if `upper` is True:
            - add char.upper() to `result`
        - if `upper` is not True:
            - add char.lower() to `result`
    - if char in not alpha:
       - add char to `result`
- return result


# '''
def staggered_case(string):
    result = ''
    upper = True

    for char in string:
        if char.isaplha():
            result += char.upper if upper else char.lower()
            upper = not upper
        else: 
            result += char

    return result


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True