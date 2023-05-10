from datetime import datetime
from datetime import date
# mytime=datetime.time(2,30,1,20)
# print(mytime.minute)
# print(mytime)
# #micro second information
# print(mytime.microsecond)
# #date Object
# today=datetime.date.today()
# print(today)
# print(today.month)
# print(today.year)
mydatetime=datetime(2021,10,3,14,20,1)
print(mydatetime)
#replacement
print(mydatetime.replace(year=2020))
#diffrence
date1=date(2021,11,3)
date2=date(2020,11,3)
print(date1-date2)