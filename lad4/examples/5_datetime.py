import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating date objects

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# strftime()

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))