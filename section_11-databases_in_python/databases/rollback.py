import sqlite3

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account, TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY (time,account))")



class Account(object):

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

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount} deposited")
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn")
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

    terry = Account("Terry")
    graham = Account("Graham")
    eric = Account("Eric")