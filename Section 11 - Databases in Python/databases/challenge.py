import sqlite3

conn = sqlite3.connect("contacts.sqlite")

user = input('Enter a name: ')

show_sql = "SELECT * FROM contacts WHERE contacts.name=?"

#conn.execute(show_sql, (user,))

for row in conn.execute(show_sql, (user,)):
    print(row)

conn.close()