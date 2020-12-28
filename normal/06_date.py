import datetime as dt

date1 = dt.datetime.now()
print(date1)

date2 = dt.datetime(year=2020,month=2,day=14)
print(date2)

days = dt.timedelta(days=25)
print(date2+days)

print(date1-date2)

print(date1.strftime('%A %d, %B %Y'))
