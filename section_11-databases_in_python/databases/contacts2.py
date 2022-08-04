import sqlite3
db = sqlite3.connect('contacts.sqlite')


new_email = "new_email@update.com"
phone = input("Enter new phone number: ")

#update_sql = f"UPDATE contacts SET email = '{new_email}' WHERE contacts.phone={phone}"

# Using placeholder value
update_sql = f"UPDATE contacts SET email = ? WHERE contacts.phone=?"

print(update_sql)
# WHERE contacts.phone=1234"

update_cursor = db.cursor()
#update_cursor.executescript(update_sql)
update_cursor.execute(update_sql, (new_email, phone))
print(f"{update_cursor.rowcount} rows updated")

update_cursor.connection.commit()
update_cursor.close()


for name, phone,email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-"*20)

db.close()
