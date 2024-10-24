# Write a function that generates text following a pattern where:
# 1) the first and last characters of each word remain in their original place
# 2) characters between the first and last characters are sorted alphabetically
# 3) punctuation should remain at the same place as it started

# Examples:
# scramble_words('professionals') # should return 'paefilnoorsss'
# scramble_words("you've gotta dance like there's nobody watching,
#                 love like you'll never be hurt, sing like there's 
#                 nobody listening, and live like it's heaven on earth.") # should return "you've gotta dacne
# # like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."
# question for examiner: if there is a special character in the word (ex you've), does it count as one word? or as 2

def scramble_words(string):
    scramble_lst = []
    words = string.split(' ')
    for word in words:
        if "," in word:
            join_comma = ''
            join_comma_lst = []
            split_words = word.split(",")
            for w in split_words:  #['you', 've]
                if len(w) > 3:
                    scramble_w = ''
                    rest_of_w = ''.join(sorted(w[1:(len(w) - 1)]))
                    scramble_w = w[0] + rest_of_w + w[-1]
                else:
                    scramble_w = w
                join_comma_lst.append(w)
                
                join_comma = ''.join
        elif "'" in word: 
            split_words = word.split(",")
            for w in split_words:  #['you', 've]
                if len(w) > 3:
                    scramble_w = ''
                    rest_of_w = ''.join(sorted(w[1:(len(w) - 1)]))
                    scramble_w = w[0] + rest_of_w + w[-1]
                else:
                    scramble_w = w
        else:
            scramble_word = ''
            rest_of_word = ''.join(sorted(word[1:(len(word) - 1)]))
            scramble_word = word[0] + rest_of_word + word[-1]
            scramble_lst.append(scramble_word)
        return scramble_lst.append(scramble_w)

    # words = string.split('\'')
    # words = string.split
    # for word in words:
    #     scramble_word = ''
    #     rest_of_word = ''.join(sorted(word[1:(len(word) - 1)]))
    #     scramble_word = word[0] + rest_of_word + word[-1]
    #     scramble_lst.append(scramble_word)
    # return ' '.join(scramble_lst)
        
        
# print(scramble_words('professionals'))
# print(scramble_words('Lucy likes mandarins'))
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."))