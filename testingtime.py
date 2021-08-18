import time
import calendar

# current local time at the time of running script
localtime = time.asctime(time.localtime(time.time()))

# provides a calendar for the year, month provided
cal = calendar.month(2018, 11)

print(localtime)
print(cal)

# checks to see if year is leap year

print(calendar.isleap(2020))
