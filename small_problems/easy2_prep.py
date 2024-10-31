# '''
# input: 2 lists
# output: set

# '''

# def union(lst1, lst2):
#     set1 = set(lst1)
#     set2 = set(lst2)
#     return set1 | set2
    
# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

'''
inout: list
output: list with 2 sublist


'''

# def halvsies(lst):
#     result = [[], []]

#     if not lst:
#         return result
#     elif len(lst) == 1:
#         result[0] = lst
#     else:
#         if len(lst) % 2 == 0:
#             half = len(lst) // 2

#         elif len(lst) % 2 == 1:
#             half = len(lst) // 2 + 1

#         result[0] = lst[:half]
#         result[1] = lst[half:]

#     return result

# def halvsies(lst):
#     half = (len(lst) + 1) // 2
#     first_half = lst[:half]
#     second_half = lst[half:]
#     return [first_half, second_half]


# # All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

'''
input: list
output: integer that appers twice in the list


ALG:
- initiliaze new_lst
- iterate over num in lst:
    - check if num in new_lst
    - if not, 
        - add num to new_lst
    - otherwise, return num


'''

# def find_dup(lst):
#     result = []
#     for num in lst:
#         if num not in result:
#             result.append(num)
#         elif num in result:
#             return num


# def find_dup(lst):
#     for num in lst:
#         if lst.count(num) == 2:
#             return num

# def find_dup(lst):
#     dups = [num for num in lst if lst.count(num) == 2]
#     return dups[0]


# print(find_dup([1, 5, 3, 1])) # == 1) # True
# print(find_dup([
            #       18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
            #       38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
            #       14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
            #       78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
            #       89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
            #       41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
            #       55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
            #       85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
            #       40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
            #        7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
            #   ]) == 73)       # True


'''
input: 2 lists
output: new list


ALG
- use list comprehension to create a list 
'''
# def interleave(lst1, lst2):
#     list_of_tuples =  [(element1, element2) for element1, element2 in zip(list1, list2)]
#     return [element for tuple in list_of_tuples for element in tuple]

# def interleave(lst1, lst2):
#     result = []
#     for idx in range(len(lst1)):
#         result.extend([lst1[idx], lst2[idx]])
    
#     return result


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2)) # == expected)      # True


'''
input: list of integers
output: string 

ALG:
- initialize `product` to 1
- iterate over elements in the list
    - mupliply product by eleement
- multipl_average = product / len(lst)
- use f-string to get formatting needed

'''
# def multiplicative_average(lst):
#     product = 1

#     for num in lst:
#         product *= num
    
#     multipl_average = product / len(lst)
#     return f'{multipl_average:.3f}'


# # All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

'''
input: 2 lists
output: new list


ALG
- 
'''
# def multiply_list(lst1, lst2):
#     return [el1 * el2 for el1, el2 in zip(lst1, lst2)]

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

'''
# input: int
# output: list of digits

# ALG:


# '''
# def digit_list(number):
#     return [int(digit) for digit in str(number)]


# print(digit_list(12345) == [1, 2, 3, 4, 5])#       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True


'''
input: list
output: string of eleemnts and # of occurances

ALG:

'''

# def count_occurrences(lst):
#     # count = {word: lst.count(word) for word in lst}
#     count = {}

#     for vehicle in lst:
#         count[vehicle] = count.get(vehicle, 0) + 1

#     for item, count in count.items():
#         print(f"{item} => {count}")

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)


def average(lst):
    return sum(lst) // len(lst)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True


