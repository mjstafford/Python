class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.has_enough_funds(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}\nInerest Rate: {self.int_rate}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1+ self.int_rate)
        return self

    #helper function
    @staticmethod
    def has_enough_funds(current_balance, withdraw_amount):
        if current_balance >= withdraw_amount:
            return True
        else:
            return False

    @classmethod
    def print_all_accounts(cls):
        count = 1 
        for account in cls.all_accounts:
            print("account", count)
            account.display_account_info()
            count += 1
            print("")

# run code
first_account = BankAccount(.01, 20)
second_account = BankAccount(.01)

first_account.deposit(5).deposit(5).deposit(79).withdraw(9).yield_interest().display_account_info()
second_account.deposit(25).deposit(20).withdraw(5).withdraw(7).withdraw(3).withdraw(20).yield_interest().display_account_info()

print("--------------- ALL ACCOUNTS ------------------")
BankAccount.print_all_accounts()