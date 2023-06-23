from datetime import datetime, timedelta
import time
import random


current_dt = datetime.now()
# print(current_dt,
#       type(current_dt),
#       current_dt.year,
#       current_dt.month,
#       current_dt.hour,
#       type(current_dt.microsecond),
#       current_dt.date(),
#       current_dt.time())

my_dt =  datetime(year = 1970, month = 2,day = 7)
my_dt_2 =  datetime(year = 1970, month = 2,day = 8)
time_delta =my_dt_2 - my_dt
custom_time_delta = timedelta(weeks=3)
future_dt = datetime.now() + custom_time_delta


now = datetime.now()
format_now = now.strftime("%A %d.%m.%Y___ %H:%M")
strptime_for = datetime.strptime(format_now,  "%A %d.%m.%Y___ %H:%M")
datetime.fromtimestamp(1687519740.0)

print(now.timestamp())


















