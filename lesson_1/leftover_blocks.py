"""
P: Understand the Problem
input: integer (number of blocks)
output: integer (number of blocks left over)
rules:
    explicit:
    - build tallest possible valid structure
    - Ok not to use all blocks
    - building blocks are cubes
    - structure is built in layers without any gaps between blocks
    - top layer is a single block
    - A block in an upper layer must be supported by four blocks in a lower layer.
    - A block in a lower layer can support more than one block in an upper layer.

    implicit:
    - all numbers are integers
    - second to the most upper layer has at least 4 blocks
    - layer configuration:
        - layer 1 (top row): 1 block (1x1)
        - layer 2 (middle row): 4 blocks (2x2)
        - layer 3 (bottom row): 9 blocks (3x3)
    - progressive layer sizes are square numbers. Number of the row squared.


questions to clarify:

E: Examples and Test Cases

Test cases provided:
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

Analysis of the test cases:
- handling zero as input. If zero blocks provided, output should be zero
- There can be just one layer that consists of one block
- second layer consists of 4 blocks
- our assumed numbers for blocks for the first 3 layers are correct
- we don't have to have any leftover blocks. Number of leftover blocks can be zero

D: Data Structures
1
22
333
4444

- List of integers: [1*1, 2*2, 3*3, 4*4,..]

A: Algorithm
- number of block is given
- initialize layers list. start with [1]. at each iteration add (n+1) squared number
- subtract number of blocks needed for layers starting from the top layer until number 
  of blocks if not enough to cover the last layer we tried (meaning results of subtraction < 0)
- return result of subtraction for the last layer that block can fully fill out

"""

# def calculate_leftover_blocks(number_of_blocks):
#   layers = []
#   for num in range(number_of_blocks + 1):
#     layer = num
#     layers.append(layer * layer)
#     leftover_blocks = (number_of_blocks - sum(layers))
#     if leftover_blocks < 0:
#       layers.pop()
#       # print(layers)
#       leftover_blocks = (number_of_blocks - sum(layers))

#   return leftover_blocks


# LS solution
def calculate_leftover_blocks(n):
    current_layer = 0
    remaining_blocks = n

    required_blocks = (current_layer + 1) ** 2

    while remaining_blocks >= required_blocks:
        remaining_blocks -= required_blocks
        current_layer += 1
        required_blocks = (current_layer + 1) ** 2

    return remaining_blocks


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
