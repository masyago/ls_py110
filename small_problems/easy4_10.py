# Building on the previous exercise, write a function that returns
# True or False based on whether or not an inventory item (an ID 
# number) is available. As before, the function takes two arguments:
# an item ID and a list of transactions. The function should return
# True only if the sum of the quantity values of the item's 
# transactions is greater than zero. Notice that there is a movement 
# property in each transaction object. A movement value of 'out'
# will decrease the item's quantity.

# You may (and should) use the transactions_for function from the previous exercise.

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

# print(is_item_available(101, transactions) == False)  # True
# print(is_item_available(103, transactions) == False)  # True
# print(is_item_available(105, transactions) == True)   # True


'''
Algorithm:
- extract all transactions with id_number into a new list 
    `id_transactions`
- initialize variable `quantity` to 0
- iterate over transactions in `id_transactions`
        - if 'movement' is 'in':
            - add corresposning value to `quantity`
        - if `movement` is `out`:
            - substract value from `quantity`
        
- if sum > 0:
    - return True
- return False if not

'''

def transactions_for(id_number, input_transactions):
    return [line 
            for line in input_transactions
            if line['id'] == id_number]


def is_item_available(id_number, input_transactions):
    quantity = 0

    for transaction in transactions_for(id_number, input_transactions):
        if transaction["movement"] == 'in':
            quantity += transaction["quantity"]
        else:
            quantity -= transaction["quantity"]

    return quantity > 0



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

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True