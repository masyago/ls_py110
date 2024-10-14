# Given the following data structure, sort the list so that the sub-lists are ordered based on the sum
# of the odd numbers that they contain. You shouldn't mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]


def sum_of_odd_num(sublist):
    odd_numbers = [num for num in sublist if num % 2 != 0]
    return sum(odd_numbers)

sorted_list = sorted(lst, key=sum_of_odd_num)
print(sorted_list)
