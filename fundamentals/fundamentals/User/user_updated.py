class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member  = False
        self.gold_card_points = 0

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

new_user = User("michael", "stafford", "mstaff@email.com", 99)
new_user.display_info().enroll().display_info()     #chaining can only happen for instance methods that return self

print("\n")
new_user2 = User("Carrie", "stafford", "cstaff@email.com", 991)
new_user3 = User("butternut", "stafford", "bstaff@email.com", 9)
new_user2.display_info()
new_user3.display_info()

print("\n")
new_user.spend(50). display_info()                  #chaining can only happen for instance methods that return self

print("\n")
new_user2.enroll().spend(80).display_info()         #chaining can only happen for instance methods that return self

print("\n")
new_user.enroll()