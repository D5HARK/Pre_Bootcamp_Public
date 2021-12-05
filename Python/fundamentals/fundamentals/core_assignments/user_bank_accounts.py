balance_list = []


class User:
    def __init__(self, name, email, user_int_rate, user_account_balance=0):
        self.name = name
        self.email = email
        self.account = Bank_account(user_int_rate, user_account_balance)

    def user_deposit(self, amount):
        if amount > 0:
            self.account.deposit(amount)
        return self

    def user_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_info(self):
        print("Name: ", self.name, "\n", "Email: ", self.email, sep="")
        self.account.display_account_info()
        return self

    def user_interest(self):
        self.account.yield_interest()
        return self


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
    bob = User("Bob", "bob@email.com", .01)
    bertha = User("Bertha", "bertha@email.com", .04)

    bob.user_deposit(100).user_deposit(50).user_deposit(25).user_withdraw(
        10).user_interest().display_user_info()

    bertha.user_deposit(200).user_deposit(500).user_withdraw(20).user_withdraw(40).user_withdraw(60).user_withdraw(
        80).user_interest().display_user_info()


if __name__ == "__main__":
    main()
