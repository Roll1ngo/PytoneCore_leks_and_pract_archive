from datetime import datetime, timedelta
from decimal import Decimal,getcontext
# current_datetime = datetime.now()
# print(current_datetime.now())
# print(current_datetime.date())
# print(current_datetime.time())

# d1= datetime(year =2012, month =1, day = 7, hour = 14)
# print(d1)

# print(datetime.weekday(datetime.now()))

# current_datetime =  datetime.now()

# future_month = (current_datetime.month % 12)+1
# future_year = current_datetime.year + int(current_datetime.month / 12)
# future_datetime = datetime(future_year, future_month,1)
# print(type(future_datetime - current_datetime))

sevent_day_2020 = datetime.now()
# four_week_interval = timedelta(weeks=4)
# diff = datetime.now()+ four_week_interval
# print(diff)

# now = datetime.now()
# print(datetime.fromtimestamp(100_000))
strf = sevent_day_2020.strftime(" %A %d %B %y")
print(strf)

getcontext().prec = 9

a = Decimal(1) / Decimal(7)
print(a)















