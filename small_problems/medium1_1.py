# Write a function that rotates a list by moving the first element to the end of
# the list. Do not modify the original list; return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.

# All of these examples should print True

'''
P
Write a function that returns a new list with first element of given list
being moved to the end of the list.

Input: list (can be empty or even not a list)
Output: a new list

rules:
- don't modify given list, return a new list
- If the input is an empty list, return an empty list.
- If the input is not a list, return None.
- elements of the given list can bevariou sdata types,
 eg numbers, strings, dicts

ALG:
- initialize empty list `result`
- check data type of argument passed in the func
    - if not list,
        - return None
    - elif not list (empty list):
        - return empty list
    - elif list:
         - slice given list [1:]
         - assign the slice to `result`
         - append given list [0] to `result`
- return `result`

'''

def rotate_list(lst):
    result = []

    if isinstance(lst, list) == False:
        return None
    elif not lst:
        return lst
    elif lst:
        result = lst[1:]
        result.append(lst[0])
        return result




print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
