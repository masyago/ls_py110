#check if data type is list, set, tuple
# isinstance takes tow arguments: variable we want to check data type of and data type
# a = [1, 2, 3]
# print(isinstance(a, list))
# print(isinstance(a, tuple))


# a = 1
# print(isinstance(a, int))

# a = {'b', 2}
# if isinstance(a, set):
#     print('a is a set')
# else:
#     print('not a dict!')


# def word_to_digit(string):
#     num_words = {'zero' : '0',
#                  'one' : '1',
#                  'two' : '2',
#                  'three' : '3',
#                  'four' : '4', 
#                  'five' : '5',
#                  'six' : '6',
#                 'seven' : '7',
#                 'eight' : '8',
#                 'nine' : '9'}
#     message_list = message.split()
#     new_message = [num_words.get(word, word) for word in message_list]
#     return ' '.join(new_message)

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

# a = 'Hello, Monkey'
# # print every other char
# for idx in range(0, len(a), 2):
#     print(a[idx])

# num1 = 1
# num2 = 2
# num1, num2 = num2, num1 + num2 # num1 = 2, num2 = 3
# print(f'num1 is {num1}')
# print(f'num2 is {num2}')
      
# a = '12345671111'
# print(list(a))
# print(set(a))

# a = '10'
# # sum of all positve  integers less than a
# print(sum(range(1, 10)))

# dict1 = {'a' : 10, 
#          'b' : 22,
#          'c' : 1}

# # sort items in dict based on values
# def sort_value(item):
#     return item[1]

# sorted_dict = sorted(dict1.items(), key=sort_value)

# print(sorted_dict)


# get all substrings of the string

# def get_substrings(s):
#     substrings = [s[:idx + 1] for idx in range(len(s))]
#     return substrings

# def get_all_substrings(a):
#     all_substrings = [substring for i in range(len(a))
#                                  for substring in get_substrings(a[i:])
#                                  if substring == substring[::-1]]


#     # for i in range(len(a)):
#     #     substr = get_substrings(a[i:])
#     #     all_substrings.extend(substr)

#     return all_substrings

# print(get_all_substrings('Natasha is studying Python'))


# def get_leading_substrings(s):
#     return [s[:idx + 1] for idx in range(len(s))]


# def substrings(string):
#     return [sub_s for idx in range(len(string))
#                   for sub_s in get_leading_substrings(string[idx:])]

# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

# print(substrings('abcde') == expected_result)  # True

# def get_leading_subs(s):
#     return [s[:i + 1] for i in range(len(s))]

# def palindromes(string):
#     return [sub_s for idx in range(len(string))
#                   for sub_s in get_leading_subs(string[idx:])
#                   if sub_s == sub_s[::-1] and len(sub_s) > 1]

# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam')) # == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

# dict1 = {1 : 'a',
#          2 : 'b',
#          3 : 'c'}

# # swap keys and values

# # swapped = {value : key}

# swapped = {value: key for key, value in dict1.items()}
# print(swapped)


# original = {key : value}
# inverted = {value : key}

# def invert_dict(fruits):
#     return {value: key for key, value in fruits.items()}

# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }))

# a = "Hello, it's Tuesday"
# staggered = ''

# for idx, char in enumerate(a):
#     result = [char.upper if idx % 2 == 0 else char.lower
#                          for idx, char in enumerate(a)]
#     # if idx % 2 == 0:
#     #     staggered += char.upper()
#     # else:
#     #     staggered += char.lower()

# print(result)


# fruits = ["apple", "banana", "cherry"]

# # Create a new list with index and fruit name
# #indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]

# print(list(enumerate(fruits)))

# a = [1, 0 , 12, 14, 1, 52, 1, 1, 52]
# remove duolicates while preserving order using set

# seen = set() # remmeber, sets are unordered!
# result = []

# for num in a:
#     if num not in seen:
#         seen.add(num)
#         result.append(num)
# print(seen)
# print(result)

# a = [1, 0 , -12, 14, 1, 52, -1, 1, 52]
# # check if any numbers are <= 0
# if any([num <= 0 for num in a]):
#     print('there are some non-positive numbers')

# angles = [0, 55, 70]
# # if any angles are 0 or less, return invalid

# if any([angle <= 0 for angle in angles]):
#     print('invalid')
# else: 
#     print('ok')
# a = [1, 0 , -12, 14, 1, 52, -1, 1, 52]
# # create a dict with numbers occurances
# count = {}
# for num in a:
#     count[num] = count.get(num, 0) + 1

# print(count)


# a = 'Hello little monkey goose'
# count = {}

# for char in a:
#     count[char] = count.get(char, 0) + 1

# print(count)

a = 'Hello Little Monkey Goose'
# list of lower case letters or triple chars for upper cae

b = [char if char.isupper() else char * 3
              for char in a]
print(''.join(b))
