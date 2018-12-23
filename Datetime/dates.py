"""" two kinds of date and time objects: `naive` and `aware` """
# `naive` - doesn't contain sufficent information to determine timezone, daylight saving times
# `aware` - contains enought information to determine timezone and daylight saving time

import datetime
import pytz

# create date
d = datetime.date(2018, 1, 30)
print(d)


# current date
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

print(today.weekday())  # monday 0 sunday 6
print(today.isoweekday())  # monday 1 sunday 7


# timedelta ==> difference between two dates or times
tdelta = datetime.timedelta(days=7)
print(today + tdelta)  # date after 7 days
print(today - tdelta)  # date before 7 days

# date2 = date1 + tdelta
# tdelta = date1 + date2


bday = datetime.date(2018, 12, 24)
till_bday = bday - today
print(till_bday.days)  # total remaining day before specific date
print(till_bday.total_seconds())  # total remaining seconds before specific date


t = datetime.time(22, 11, 50, 100000)  # time(hr, min, sec, microsec)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)


t = datetime.datetime(2018, 12, 23, 22, 14, 50, 100000)
print(t)
print(t.date())
print(t.time())
print(t.year)

tdelta = datetime.timedelta(days=7)
print(t + tdelta)

tdelta = datetime.timedelta(hours=10)
print(t + tdelta)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)


# timezone `aware` datetime using UTC
dt = datetime.datetime(2018, 12, 23, 22, 24, 50, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)  # *** #
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_ktm = dt_now.astimezone(pytz.timezone('Asia/Kathmandu'))
print(dt_ktm)

# print all timezone contained in pytz library
for tz in pytz.all_timezones:
    print(tz)

local_time = datetime.datetime.now()
dt_mtn = local_time.astimezone(pytz.timezone('US/Mountain'))

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(local_time)
print(dt_mtn)


dt_ktm = datetime.datetime.now(tz=pytz.timezone('Asia/Kathmandu'))
print(dt_ktm)
print(dt_ktm.isoformat())

# to display date in specific format like December 23, 2018
# `strftime` --> converts datetime to string
print(dt_ktm.strftime('%B %d, %Y'))

# convert string to datetime
# `strptime` --> converts string to datetime
dt_str = 'December 23, 2018'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
