import pytz
import datetime as dt

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)

local_time = dt.datetime.now(tz=tz_to_display)

print(f"The time in {country} is {local_time}")
print(f"UTC is {dt.datetime.utcnow()}")


# for x in pytz.all_timezones:
#     print(x)

for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}")


# BV causes an error here, has no timezone or something weird, not available as a key
# for x in sorted(pytz.country_names):
#     print(f"{x}: {pytz.country_names[x]} {pytz.country_timezones.get(x)}")


for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}:",end=':')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones):
            tz_to_display = pytz.timezone(zone)
            local_time = dt.datetime.now(tz=tz_to_display)
            print(f"\t\t{zone}: {local_time}")
    else:
        print('\t\tNo timezone specified')