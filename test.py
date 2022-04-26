import datetime


hour = 10
minute = 13
second = 50
microsecond = 0

time_now = datetime.datetime.now()
time_start = datetime.datetime(
    time_now.year,
    time_now.month,
    time_now.day,
    hour,
    minute,
    second,
    microsecond)

time_difference = time_start - time_now
print(time_difference.total_seconds())
print(time_now)