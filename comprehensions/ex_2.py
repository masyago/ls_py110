# Update code wiht for loop to display the future ages.

age = int(input('How old are you? '))
print()
print(f'You are {age} years old.')

delta_years = [10, 20, 30, 40]
for years in delta_years:       # more elegant: in range(10, 50, 10)
    print(f'In {years} years, you will be {age + years} years old.')
#print(f'In 20 years, you will be {age + 20} years old.')
#print(f'In 30 years, you will be {age + 30} years old.')
#print(f'In 40 years, you will be {age + 40} years old.')
