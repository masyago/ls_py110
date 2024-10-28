# Given two lists of integers of the same length, return a new list where 
# each element is the product of the corresponding elements from the two lists.


'''
Algorithm:
- initialize an empty list `result`
- iterate over indexes up to the length of the lists:
    - multiply elements from both lists at the inde position
    - append product to `result`
- return `result` 

'''

# def multiply_items(lst1, lst2):
#     result = []

#     for idx in range(len(lst1)):
#         product = lst1[idx] * lst2[idx]
#         result.append(product)
#     return result


def multiply_items(lst1, lst2):
    return [num1 * num2 for num1, num2 in zip(lst1, lst2)]


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True