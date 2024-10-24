# Write a function that takes a string of integers as input and returns the
# number of substrings that result in an odd number when converted to an integer.

# Examples:
# solve("1341") # should return 7
# solve("1357") # should return 10


def solve(string):
    count = 0
    for idx_1 in range(len(string)):
        for idx_2 in range(len(string)):
            substring = string[idx_1:(len(string) - idx_2)]
            if not substring:
                continue
            
            current_num = int(substring)
            # print(current_num)
            if int(current_num) % 2 == 1:
                count += 1
    
    return count

print(solve("1341")) # should return 7
print(solve("1357"))# should return 10

