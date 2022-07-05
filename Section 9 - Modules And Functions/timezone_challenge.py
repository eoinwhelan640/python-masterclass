# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime as dt
import pytz

timezone_dict = {str(i+1):v for i,v in enumerate(pytz.all_timezones[:9])}
# while True:
#     {print(f"[{k}]: v") for k,v in timezone_dict.items()}
#     choice = input('Please choose a timezone from the list :> ')
#     if choice in timezone_dict:
#         chosen_tz = pytz.timezone(timezone_dict[choice])
#         local_time = dt.datetime.now(tz=chosen_tz)
#         utc_time = dt.datetime.utcnow()
#
#         print(f"Aware local time {pytz.utc.localize(local_time)}\nAware UTC {pytz.utc.localize(utc_time)}")
#     elif choice == 0:
#         break
#     else:
#         print('invalid choice - choose from the options: ')

#timezone_dict = {i+1:v for i,v in enumerate(pytz.all_timezones[:9])}
print(timezone_dict)
{print(f"[{k}]: {v}") for k,v in timezone_dict.items()}
while True:
    choice = input('Please choose a timezone from the list :> ')
    if choice =='0':
        break

    if choice in timezone_dict:
        tz_to_display = pytz.timezone(timezone_dict[choice])
        world_time = dt.datetime.now(tz=tz_to_display)
        print(f"The time in {timezone_dict[choice]} is {world_time.strftime('%A %x %X %z')} {world_time.tzname()}")
        print(f"Local time is {dt.datetime.now().strftime('%A %x %X')}")
        print(f"UTC time is {dt.datetime.utcnow().strftime('%A %x %X')}")
        print()



