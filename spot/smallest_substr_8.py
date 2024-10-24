# Write a function that takes a non-empty string `s` as input and finds the
# minimum substring `t` and the maximum number `k`, such that the entire string
# `s` is equal to `t` repeated `k` times.

# Examples:
# f("ababab") # should return ["ab", 3]

def min_max_substring(s):
    min_str_max_repeats = []

    for idx1 in range(len(s)):
        half_length = int(len(s) / 2) + 1
        for idx2 in range(half_length - idx1):
            substring = s[idx1:idx2]
            if not substring:
                continue

            if len(s) % len(substring) == 0:
                k = len(s) // len(substring)
                if substring * k == s:
                    min_str_max_repeats.append(substring)
                    min_str_max_repeats.append(k)

    return min_str_max_repeats




print(min_max_substring('aaaaa'))