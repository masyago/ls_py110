# Write a function that takes a string argument consisting 
# of a first name, a space, and a last name. The function
# should return a new string consisting of the last name,
# a comma, a space, and the first name.


def swap_name(string):
    name_list = string.split(' ')
    last_name = name_list.pop()
    first_middle = ' '.join(name_list)
    return (f"{last_name}, {first_middle}")


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True