# Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

'''
input: positive integer that represents year
output: integer that represent number of Fridays the 13ths in that year

rules:
- assume Gregorian calendar

ALG: 
- things we need to know:
    - whether the year is leep year
    - day of the week the year started

number for Friday is 4

- import datetime module
- count_Fridays = 0
- iterate over month in range(1, 13):
    - get date of the week in number form: 
          day_of_weeek_num = datetime.date(input_year, month, 13).weekday()
    - check if the number is 4 (represents Friday). If yes: 
        - add 1 to count
 - return count

'''

import datetime

def friday_the_13ths(given_year):
    count_Fridays = 0

    for month in range(1, 13):
        day_of_weeek_num = datetime.date(given_year, month, 13).weekday()
        if day_of_weeek_num == 4:
            count_Fridays += 1
    return count_Fridays

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
