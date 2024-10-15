def word_sizes(s):
    word_size_freq = {}
    words = alpha_words(s).split()

    for word in words:
        if len(word) in word_size_freq:
            word_size_freq[len(word)] += 1
        else:
            word_size_freq[len(word)] = 1
    
    return word_size_freq

def alpha_words(text):
    clean_s = ''
    for char in text:
        if char.isalpha() or char.isspace():
            clean_s += char
    return clean_s

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
