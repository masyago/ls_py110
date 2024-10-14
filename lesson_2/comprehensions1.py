# Compute and display the total age of the family's male members.
#  Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}


# using for loop
# total_age = 0
# for value in munsters.values():
#     if value['gender'] == 'male':
#         total_age += value['age']

# print(total_age)

# using comprehension
male_ages = [member['age'] for member in munsters.values()
                           if member['gender'] == 'male']

print(sum(male_ages))