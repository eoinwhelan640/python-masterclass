import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name,phone,email) VALUES('Eoin', 662390240, 'eoin@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@gmail.com')")

cursor = db.cursor()

#print(cursor.fetchall())
#print(cursor.fetchone())


for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)

cursor.close()
db.commit()
db.close()