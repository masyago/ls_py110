# Write a function that returns a string that contains a UUID

import random

def generate_uuid():
    uuid = []
    char_amount = [8, 4, 4, 4, 12]
    hex_char = '0123456789abcdf'

    for num in char_amount:
        chars = [random.choice(hex_char) for _ in range(num)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

print(generate_uuid())





# OUTPUT: string that contains hexadecimal characters and "-". 
        # pattern: 8-4-4-4-12
