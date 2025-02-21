import datetime

# get current date and time
now = datetime.datetime.now()
print(now)  # example: 2025-02-18 11:03:19.709129

# extract year and weekday
print(now.year)  # year
print(now.strftime("%A"))  # weekday

# manually create a date object
custom_date = datetime.datetime(2020, 5, 17)
print(custom_date)  # 2020-05-17 00:00:00

# strftime(): format date into a string
print(custom_date.strftime("%B"))  # may

# some other date formatting examples
print(now.strftime("%d-%m-%Y %H:%M:%S"))  # 18-02-2025 11:03:19
print(now.strftime("%A, %d %B %Y"))  # tuesday, 18 february 2025
