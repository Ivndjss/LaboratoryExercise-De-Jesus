import datetime

t1 = datetime.time(4, 20, 1)
t2 = datetime.time(6, 20, 1)

print(t1)
print('hour :', t1.hour)
print('minute:', t1.minute)
print('second:', t1.second)
print('microsecond:', t1.microsecond)
print('tzinfo:', t1.tzinfo)