import calendar

month, day, year = input().split()

x = calendar.weekday(int(year), int(month), int(day))

print(calendar.day_name[x].upper())


