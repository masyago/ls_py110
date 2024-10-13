# Given the object shown below, print the name, age, and gender of each family member:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# for key in munsters.keys():
#     name = key
#     age = munsters[key]['age']
#     gender = munsters[key]['gender']
#     print(f'{name} is a {age}-year-old {gender}.')

# More consice version
for name, info in munsters.items():
    print(f"{name} is a {info['age']}-year-old {info['gender']}.")