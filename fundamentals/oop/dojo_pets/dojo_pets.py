from Ninja import Ninja #have to use when file and class in that file have the same name!
from Pet import Pet
# import Ninja  # will not work since my class and file are named the same
# import Pet

butternut = Pet("Butternut", "dog", ["play dead", "shake", "roll over"])
ninja = Ninja("Mike", "stafford", ["ball", "bone", "pinecone"], "wet food", butternut)
print(ninja)

print(ninja.feed().walk().bathe())

#sub-class
class Cow(Pet):
    def __init__(self, name, type, tricks, fun_fact):
        super().__init__(name, type, tricks)
        self.fun_fact = fun_fact

    def noise(self):
        print(f"The noise a {self.type} makes! MOOOOOOOOOOOOOOOOOOOOOO, POLYMORPHISM!")
        return self

bessy = Cow("bessy", "cow", ["eat grass", "produce milk"], "cows live around 20 years")

print(bessy)
bessy.noise()
butternut.noise()