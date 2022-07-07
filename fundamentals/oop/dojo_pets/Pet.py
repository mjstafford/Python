class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print(f"The noise a {self.type} makes!")
        return self

    def __repr__(self):
        return f"\tname: {self.name}\n\tType: {self.type}\n\tTricks: {self.tricks}\n\tHealth: {self.health}\n\tEnergy: {self.energy}"