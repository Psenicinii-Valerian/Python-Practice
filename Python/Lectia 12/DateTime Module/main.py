from datetime import datetime
# default datetime format
current_datetime = datetime.now()
print(current_datetime)
# extracting date by format year-month-day
formated_datetime = current_datetime.strftime("%Y-%m-%d")
print(formated_datetime)
# extracting time by format hour:minute
hour = current_datetime.strftime("%H:%M:%S")
print(hour)

# another thing to do with datetime
from datetime import *
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

# extracting date and time separately (1 data per 1 variable)
current = datetime.now()
year = current.year
month = current.month
day = current.day
sec = current.second
print(year, month, day, sec)