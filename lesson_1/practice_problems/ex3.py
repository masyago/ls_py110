# How would you obtain a set that contains all the unique values from both sets?
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# c = a.union(b) # you can use union function or | operator
c = a | b

print(c)
