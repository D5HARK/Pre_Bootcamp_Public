balance_list = []


class Bank_account:

    def __init__(self, int_rate, balance=0):
        if balance > 0:
            self.balance = balance
        else:
            self.balance = 0
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance_log(self.balance)
        self.balance = (self.balance + amount)
        return self

    def withdraw(self, amount):
        self.balance_log(self.balance)
        if (self.balance - amount) > 0:
            self.balance = (self.balance - amount)
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = (self.balance - 5)
            return self

    def display_account_info(self):
        self.balance_log(self.balance)
        print("Balance:", self.balance)
        print(balance_list)
        balance_list.clear()
        return self

    @classmethod
    def balance_log(cls, balance):
        balance_list.append(balance)

    def yield_interest(self):
        self.balance_log(self.balance)
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self


def main():
    account_one = Bank_account(.01)
    account_two = Bank_account(.04)
    account_one.deposit(100).deposit(50).deposit(25).withdraw(10).yield_interest().display_account_info()
    account_two.deposit(200).deposit(500).withdraw(20).withdraw(40).withdraw(60).withdraw(
        80).yield_interest().display_account_info()


if __name__ == "__main__":
    main()
