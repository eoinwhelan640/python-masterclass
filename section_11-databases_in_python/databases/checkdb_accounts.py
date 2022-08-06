import sqlite3
import datetime as dt
import pytz

# need to actually declare the types we're using. use detect types
db= sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
                      "history.account, history.amount FROM history ORDER BY history.time"):
    # prints our tuples of each row
    print(row)

    # show we're using strings for times here
    #local_time= row[0]
    #print(f"{local_time}\t{type(local_time)}")

    # utc_time= row[0]
    # local_time= pytz.utc.localize(utc_time).astimezone()
    # print(f"{utc_time}\t{local_time}")