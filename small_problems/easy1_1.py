# def number_ending(integer):
#     if integer == 1:
#         ending = 'st'
#     elif integer == 2:
#         ending = 'nd'
#     elif integer == 3:
#         ending = 'rd'
#     else:
#         ending = 'th'
#     return ending

# def five_numbers(lst):
#     new_lst = []
#     for n in lst:
#         n = str(n)
#         new_lst.append(n)
#     display_numbers = ', '.join(new_lst)
#     return display_numbers

# first_five = []
# for count in range(1,6):
#     num = int(input(f'Enter the {count}{number_ending(count)} number: '))
#     first_five.append(num)


# last_number = int(input('Enter the last number: '))

# if last_number in first_five:
#     print(f"\n{last_number} is in {five_numbers(first_five)}.")
# else:
#     print(f"\n{last_number} isn't in {five_numbers(first_five)}.")


# Expected output examples:
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# LS solution
numbers = []

numbers.append(input("Enter the 1st number: "))
numbers.append(input("Enter the 2nd number: "))
numbers.append(input("Enter the 3rd number: "))
numbers.append(input("Enter the 4th number: "))
numbers.append(input("Enter the 5th number: "))
last_number = input("Enter the last number: ")

numbers_list = ','.join(numbers)

if last_number in numbers:
    print(f"{last_number} is in {numbers_list}.")
else:
    print(f"{last_number} isn't in {numbers_list}.")

