
# def double_consonants(string):
#     VOWELS = 'aeiouAEIOU'
#     result = ''

#     for char in string:
#         if char.isalpha() and char not in VOWELS:
#             result += char * 2
#         else:
#             result += char
    
#     return result

# # All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

# def reverse_number(num):
#     return int(str(num)[::-1])

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True


# Write a function that takes an integer argument and
# returns a list containing all integers between 1 and 
# the argument (inclusive), in ascending order.

# You may assume that the argument will always be a 
# positive integer.


# def sequence(input_number):
#     return list(range(1, input_number + 1))

# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

# def swap_name(string):
#     names = string.split()
#     return f'{names[1]}, {names[0]}'


# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True


# def sequence(count, starting_num):
#     # result = []
#     # for idx in range(1, count + 1):
#     #     result.append(starting_num * idx)

#     # return result
#     return [starting_num * idx for idx in range(1, count + 1)]

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True



# def reverse_list(lst):
#     first = 0
#     last = -1

#     while first < (len(lst) // 2):
#         lst[first], lst[last] = lst[last], lst[first]
#         first += 1
#         last -= 1
    
#     return lst

# def reverse_list(lst):
#     for idx in range(len(lst) // 2):
#         lst[idx], lst[-idx - 1] = lst[-idx - 1], lst[idx]
    
#     return lst


# list1 = [1, 2, 3, 4]
# reverse_list(list1)
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

# def is_balanced(string):
#     balanced = 0
#     parentheses = ''

#     for char in string:
#         if char == '(' or char == ')':
#             parentheses += char

#     if parentheses:
#         if parentheses[0] != '(' or parentheses[-1] != ')':
#             return False

#     for char in string:
#         if char == '(':
#             balanced += 1
#         elif char == ')':
#             balanced -=1
        
#     return balanced == 0

def is_balanced(s):
    parens = 0
    for char in s:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False
    return parens == 0



print(is_balanced("What (is) this?")) # == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True