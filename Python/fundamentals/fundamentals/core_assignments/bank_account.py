class Bank_account:

    def __init__(self, int_rate, balance=0):
        if balance > 0:
            self.balance = balance
        else:
            self.balance = 0
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance = (self.balance + amount)
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance = (self.balance - amount)
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = (self.balance - 5)
            return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    @classmethod
    def print_balances(cls, balance):
        print("Balance:", balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self


def main():
    first_account = Bank_account(0.01)
    second_account = Bank_account(.04)

    first_account.deposit(110).deposit(50).deposit(25).withdraw(10).yield_interest().print_balances(
        first_account.balance)

    second_account.deposit(200).deposit(500).withdraw(20).withdraw(40).withdraw(60).withdraw(
        80).yield_interest().print_balances(second_account.balance)


if __name__ == "__main__":
    main()
