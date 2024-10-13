names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names): # [(index1, name1), (index2, name2), ...]
    name_positions[name] = index # add key (name) /value (index) pair to dict name_positions
print(name_positions)

"""
Expected output
{"Fred" : 0,
 "Barney" : 1,
 "Wilma" : 2,
 "Betty" : 3,
 "Pebbles" : 4,
 "Bambam" : 5,
}

"""