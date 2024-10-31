# # For each object shown below, demonstrate how you would access the letter g.

# lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

# lst2 = [
#     {
#         'first': ['a', 'b', 'c'],
#         'second': ['d', 'e', 'f']
#     },
#     {
#         'third': ['g', 'h', 'i']
#     }
# ]

# lst3 = [['abc'], ['def'], {'third': ['ghi']}]

# dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# # This one is much more challenging than it looks! Try it, but don't
# # stress about it. If you don't solve it in 10 minutes, you can look
# # at the answer.
# dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}


# print(lst1[2][1][-1])

# print(lst2[1]['third'][0])

# print(lst3[2]['third'][0][0])

# print(dict1['b'][1])

# print(list(dict2['3rd'].keys())[0])

# For each of these collection objects, demonstrate how you would change the value 3 to 4.

# lst1 = [1, [2, 3], 4]

# lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

# dict1 = {'first': [1, 2, [3]]}

# dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

# lst1[1][1] = 4
# print(lst1)

# lst2[2] = 4
# print(lst2)

# dict1['first'][2][0] = 4
# print(dict1)

# dict2['a']['a'][2] = 4
# print(dict2)

# Given the following code, what will the final values of a and b be? Try to answer without running the code.

# a = 2
# b = [5, 8]
# lst = [a, b] #[2, [5, 8]]

# lst[0] += 2 # a = 2, b  = [5, 8]
# lst[1][0] -= a # a = 2, b = [3, 8]

# print(a)
# print(b)

# One of the most frequently used real-world string operations is that 
# of "string substitution," where we take a hard-coded string and modify 
# it with various parameters from our program.

# Given the object shown below, print the name, age, and gender of each family member:
# (name) is a (age)-year-old (male or female).

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# for key, value in munsters.items():
# for idx in range(len(munsters.items())):
#     name = list(munsters.keys())[idx]
#     age_number = munsters[name]['age']
#     gender = munsters[name]['gender']
#     print(f'{name} is {age_number}-year-old {gender}.')

for name, info in munsters.items():
    print(f'{name} is {info['age']}-yearl-old {info['gender']}.')