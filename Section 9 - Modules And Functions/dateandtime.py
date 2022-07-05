import datetime
import time

print(f"The epoch on this system starts at {time.strftime('%c', time.gmtime(0))}")
print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")

if time.daylight != 0:
    print(f"Daylight savings time is in effect in this location")
    print(f"The DST timezone is {time.tzname[1]}")

print(f"Local time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
print(f"UTC time is {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}")


# daytime is the name of the module but also a class within that
print(35*'*' + " DATETIME " + 35*'*')
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())


