# Given the following data structure, write some code to return a list 
# that contains the colors of the fruits and the sizes of the vegetables.
# The sizes should be uppercase, and the colors should be capitalized.
# expected return value: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# for loop solution
# info_lst = []

# for key1, value1 in dict1.items():
#     if value1['type'] == 'fruit':
#         capitalized_lst = [colors.capitalize() for colors in value1['colors']]
#         info_lst.append(capitalized_lst)
#     elif value1['type'] == 'vegetable':
#         info_lst.append(value1['size'].upper())

# print(info_lst)

# helper func + comprehension solution

def transformed_info(plants):
    if plants['type'] == 'fruit':
        capitalized_lst = [colors.capitalize() for colors in plants['colors']]
        return capitalized_lst
    elif plants['type'] == 'vegetable':
        return plants['size'].upper()


info_lst = [transformed_info(plants) for plants in dict1.values()]
print(info_lst)