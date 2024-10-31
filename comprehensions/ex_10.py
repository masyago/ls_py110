# Refactor the code so it doesn't require two different invocations of randrange.

import random

# def randon_number(number):
#     number = random.randrange(highest + 1)
#     return(number)

highest = 10
# number = random.randrange(highest + 1)
# print(number)
#
# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)



# Using for loop
# for number in range(0, highest + 1):
#     if number != random.randrange(highest + 1):
#         print(number)
#     else:
#         break

# Using while loop
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break
