class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

    def __repr__(self):
        return f"first name: {self.first_name}\nTreats:{self.treats}\nPet food: {self.pet_food}\nPet:\n{self.pet}"
