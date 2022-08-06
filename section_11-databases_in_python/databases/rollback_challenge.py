import sqlite3
import datetime as dt
import pytz
import pickle

# approach is to store the orig tzinfo
# we use pickle to serialise(turn into a bytestream) the data and store it in the db

db = sqlite3.connect("accounts_challenge.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
# Add new column zone here
# want to store tzinfo object for local tz. Get it by converting utc to local time
# get by current_time method modified
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, zone INTEGER NOT NULL, PRIMARY KEY (time,account))")

# When we want to create the view
db.execute("CREATE VIEW IF NOT EXISTS localhistory as "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') "
           "AS localtime, history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod
    def _current_time():
        #origin - return pytz.utc.localize(dt.datetime.utcnow())
        # local_time = pytz.utc.localize(dt.datetime.utcnow())
        # return local_time.astimezone()
        utc_time = pytz.utc.localize(dt.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time, zone


    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute("SELECT name,balance FROM accounts WHERE (name=?)", (name,))
        row = cursor.fetchone()

        #if row is not None
        if row:
            self.name, self._balance = row
            print(f"Retrieved record for {self.name}", end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?,?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {name}.")
        self.show_balance()

    def _save_update(self,amount):
        new_balance = self._balance + amount
        deposit_time, zone = Account._current_time() # unpack the returned tuple
        picked_zone = pickle.dumps(zone)
        db.execute("UPDATE accounts SET balance = ? WHERE (name=?)",(new_balance, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?, ?)",
                   (deposit_time, self.name, amount, picked_zone))
        db.commit()
        self._balance = new_balance


    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = pytz.utc.localize(dt.datetime.utcnow())
            # db.execute("UPDATE accounts SET balance = ? WHERE (name=?)",(new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print(f"{amount} deposited")
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance= ? WHERE (name=?)",(new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print(f"{amount: .2f} withdrawn")
            return amount
        else:
            print(f"The amount must be greater than 0 and no more than the account balance")
            return 0.0

    def show_balance(self):
        print(f"Balance on the account {self.name} is {self._balance}")




# Write test
# Can see we get floating point error, would ideally use decimal class as done in rollback2
if __name__ == '__main__':
    john = Account("John")
    john.deposit(10.0)
    john.deposit(0.10)
    john.deposit(0.40)
    john.withdraw(0.30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 90)
    eric = Account("Eric", 70)
    michael = Account("Michael")
    terryG = Account("TerryG")
    db.close()