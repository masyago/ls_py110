def swap(string):
    swapped_letters = []
    words = string.split()
    for word in words:
        if len(word) == 1:
            swapped_letters.append(word)
        else:
            word = word[-1] + word[1: - 1] + word[0]
            swapped_letters.append(word)

    return (' ').join(swapped_letters)

print(swap('Oh what a wonderful day it is'))

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True