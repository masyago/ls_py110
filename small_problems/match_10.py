# Write a function that takes a string as an argument and returns True 
# if all parentheses in the string are properly balanced, False otherwise.
#  To be properly balanced, parentheses must occur in matching '(' and ')' pairs.
# Note that balanced pairs must start with a (, not a ).

# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True


def is_balanced(string):
    parenth = 0
    for char in string:
        if char == '(':
            parenth += 1
        elif char == ')':
            parenth -= 1
        
        if parenth < 0:
            return False
        
    return parenth == 0


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True