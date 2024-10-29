# Given a sequence of integers, filter out instances where the same value occurs
# successively, retaining only the initial occurrence. Return the refined sequence.


'''
A

- initialize `result` to an empty list

- iterate over numbers in `original` list
- if `result` is empty or current num not equals previous element of `result`:
    - add current num to `result`
- return `result`

'''

# def unique_sequence(original):
#     result = []

#     for num in original:
#         if not result or num != result[-1]:
#             result.append(num)

#     return result

def unique_sequence(original):
    return [num 
            for idx, num in enumerate(original)
            if (idx == 0) or (num != original[idx-1])]


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True


# original = []
# print(unique_sequence(original))