from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

while michelangelo.health > 0 and jack_sparrow.health > 0:
    print("1) Attack")
    print("2) Heal")
    option_jack = input("Jack Sparrow choose!")
   
    if option_jack == "1":
        if jack_sparrow.is_alive():
            jack_sparrow.attack(michelangelo)
            michelangelo.show_stats()
    elif option_jack == "2":
        if jack_sparrow.is_alive():
            jack_sparrow()
            jack_sparrow.show_stats()

    print("1) Attack")
    print("2) Heal")
    option_michael = input("Michael Angelo choose!")
    
    if option_michael == "1":
        if michelangelo.is_alive():
            michelangelo.attack(jack_sparrow)
            jack_sparrow.show_stats()
    elif option_michael == "2":
        if michelangelo.is_alive():
            michelangelo.heal()
            michelangelo.show_stats()
        
    if michelangelo.health <= 0:
        print("Jack Sparrow has won the battle")
    elif jack_sparrow.health <= 0:
        print("Michael Angelo has won the fight")

