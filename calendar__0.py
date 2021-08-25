import calendar
year = 2018
month = 9
c = calendar.TextCalendar(calendar.MONDAY)
cal = c.formatmonth(year,month)
print(cal)
