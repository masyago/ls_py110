# The time of day can be represented as the number of minutes before or after midnight. 
# If the number of minutes is positive, the time is after midnight. If the number of
# minutes is negative, the time is before midnight.

# Write a function that takes a time using this minute-based format and returns the 
# time of day in 24-hour format (hh:mm). Your function should work with any integer input.

# You may not use Python's datetime module.

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True


'''
Problem
Write a function that converts minute-based format (before/after midnight) tpo
24 h time format without using datetiem module

Examples/Test Cases
- integers can be positive, negative, zero
- zero returns 00:00

Data Structures
input: integer
Output: string containing time in hh:mm format

Algorithm
- initialize time (empty string)
- extract number of hours and minutes from input
- add result to 24 hours 0 minutes
- divide hours by 24. remainder is hours
- concatenate hours and minutes to time string in requered format

Coding
'''
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR


def format_time(time_hours, time_minutes):
    return (f"{time_hours:02d}:{time_minutes:02d}") # formatting: minimum 2 digit width. 

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    time_hours = delta_minutes // MINUTES_PER_HOUR
    time_minutes = delta_minutes % MINUTES_PER_HOUR

    return(format_time(time_hours, time_minutes))



print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True