# For loop solution (mutates original list)
# def multiply_list(lst):
#     for idx in range(len(lst)):
#         lst[idx] *= 2

#     return lst

# List comprehension solution (creates a new list)
def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])