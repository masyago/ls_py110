# fruits = ("apple", "banana", "cherry", "date", "banana")

# print(fruits.count('banana'))


# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# # c = a.union(b) # {1, 2, 3, 4, 5, 6}
# # print(c)

# # c = a | b
# # print(c)

# # a.update(b)
# # print(a)
# # print(b)

# a |= b
# print(a)
# print(b)

# names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
# indexed_names = {}

# for index, name in enumerate(names):
#     indexed_names[name] = index

# print(indexed_names)

# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }

# total_age = sum(ages.values())
# print(total_age)

# min_age = min(ages.values())
# print(min_age)

# statement = "The Flintstones Rock"

# # letter_count = {char: statement.count(char)
# #                 for char in statement
# #                 if char.isalpha()}

# # print(letter_count)

# letters_only = statement.replace(' ', '')
# letter_count = {}

# for letter in letters_only:
#     letter_count[letter] = letter_count.get(letter, 0) + 1

# print(letter_count)

