import datetime as dt
import pytz

# local_time = dt.datetime.now()
# utc_time = dt.datetime.utcnow()
#
# print(f'Naive local time {local_time}\nNaive UTC {utc_time}')
#
# aware_local_time = pytz.utc.localize(local_time)
# aware_utc_time = pytz.utc.localize(utc_time)
#
# print(f"Aware local time {aware_local_time}\nAware UTC {aware_utc_time}")
#
#
# # Convert it to timezone we actually want, ie NOT utc
# aware_utc_time = pytz.utc.localize(utc_time).astimezone()
# #aware_utc_time = pytz.utc.localize(utc_time).astimezone(tz=)
# print(f"Aware local time {aware_local_time}\nAware UTC {aware_utc_time}")
#

# localise two utc times
gap_time = dt.datetime(2015,10,25,1,30,0,0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (60*60)

gb = pytz.timezone("GB")

dt1 = pytz.utc.localize(dt.datetime.utcfromtimestamp(s)).astimezone(gb)
print(dt1)
dt2 = pytz.utc.localize(dt.datetime.utcfromtimestamp(t)).astimezone(gb)
print(dt2)

print(f"{s} seconds since the epoch is {dt1}")
print(f"{t} seconds since the epoch is {dt2}")