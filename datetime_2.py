# Part 3
import datetime


d1 = datetime.datetime.combine(datetime.date.today(), datetime.time(8,0,0))
d2 = datetime.datetime.combine(datetime.date.today(), datetime.time(12,0,0))

print('Start time......', d1.time())
print('End time .......',d2.time())
print('Time difference:', (d2-d1).seconds//3600, ':', ((d2-d1).seconds//60)%60, ':', (d2-d1).seconds%60)