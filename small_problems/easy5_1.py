# Given a dictionary where both keys and values are unique, 
# invert this dictionary so that its keys become values and 
# its values become keys.



# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

'''
- create an empty dict `result`
   - iterate over each key/value pair in 
   the input_dict
   - add key/value pair with key and value
     swaped to `result`
- return `result`


'''

# Dict comprehension solution
# def invert_dict(input_dict):
#     return {value:key for key, value in input_dict.items()}


# for loop solution
def invert_dict(input_dict):
    result = {}

    for key, value in input_dict.items():
        result[value] = key
    return result


print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }))