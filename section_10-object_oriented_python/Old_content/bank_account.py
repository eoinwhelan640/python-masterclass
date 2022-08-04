import datetime as dt
import pytz


class Account:
    """ Simple Bank account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = dt.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_log = [(Account._current_time(), self.__balance)]
        #self.transaction_log = []
        #self.opening_balance = balance
        print(f"Account created for {self._name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_log.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_log.append((Account._current_time(), -1 * amount))
        else:
            print(f"The amount must be greater than 0 and no more than your current balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        #print(f"{self.opening_balance:6} Opening balance")
        for date, amount in self._transaction_log:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
                amount *= -1
            print(f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == '__main__':
    eoin = Account("Eoin", 0)
    eoin.show_balance()

    eoin.deposit(1500)
    eoin.deposit(500)
    eoin.withdraw(200)
    eoin.show_transactions()

    anet = Account("Annette", 800)
    anet.show_balance()
    anet.__balance = 1200
    anet.show_balance()
    anet.deposit(100)
    anet.withdraw(200)
    anet.show_transactions()
    anet.show_balance()
    print(anet.__dict__)

