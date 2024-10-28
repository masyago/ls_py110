# Given a dictionary and a list of keys, produce a new dictionary
# that only contains the key/value pairs for the specified keys.

# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }

# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True

'''
Algorithm
- initialize am empty dictionary `result`
- iterate over items in input_dict:
    - if key is in list `keys`:
        - add key/value pair to `result`

- return `result`

'''

# def keep_keys(input_dict, keys_lst):
#     result = {}

#     for key, value in input_dict.items():
#         if key in keys:
#             result[key] = value
#     return result

def keep_keys(input_dict, keys_lst):
    return {key: value
            for key, value in input_dict.items()
            if key in keys_lst}


input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True