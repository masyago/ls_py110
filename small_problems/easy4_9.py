# Write a function that takes two arguments, an inventory item ID and
# a list of transactions, and returns a list containing only the 
# transactions for the specified inventory item.

# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
#       ]) # True

'''
Problem
Write a function that returns transactions for select item
# The problem is around filtering data from a list of 
# dictionaries based on provided criterion

inputs:
- integer: item ID
- list of transactions (list of dictionaries)

output:
- list of transactions (list of dictionaries)

rules:
    - explicit 
        - return only transactions for specified ID

    - implicit
        - assume transactions have the same format 
        (dicts with the same number of key/value pairs)
        and same data types of keys and values

Data Structures:
- list of dictionaries
- possibly list comprehension

Algorithm:
- initialize empty list `result`
- iterate over dicts in input_transactions list:
    - Extract nested dict where id is specified number
    - add extracted dicts to `result`
- return `result`

Coding
'''

# def transactions_for(id_number, input_transactions):
#     result = []
#     for line in input_transactions:
#         if line['id'] == id_number:
#             result.append(line)

#     return result

def transactions_for(id_number, input_transactions):
    return [line 
            for line in input_transactions
            if line['id'] == id_number]


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True