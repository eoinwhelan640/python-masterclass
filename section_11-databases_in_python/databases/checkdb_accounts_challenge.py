import sqlite3
import datetime as dt
import pytz
import pickle

# need to actually declare the types we're using. use detect types
db= sqlite3.connect("accounts_challenge.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    picked_zone = row[3]
    zone = pickle.loads(picked_zone)
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print(f"{utc_time}\t{local_time}\t{local_time.tzinfo}")


db.close()