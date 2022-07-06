
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

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member  = False
        self.gold_card_points = 0
        self.account = BankAccount(0.02)

    def display_info(self):
        print("First Name:",self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("rewards member:", self.is_rewards_member)
        print("points", self.gold_card_points)
        return self
    
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("Already rewards memeber!")
        return self

    def spend(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("not enough points :(")
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


# run code
michael_user = User("Michael", "Stafford", "123@email.com", 99)
michael_user.make_deposit(50).make_withdrawal(20).display_user_balance()