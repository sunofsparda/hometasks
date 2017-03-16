# Task1
# https://www.codewars.com/kata/fractions-class/train/python


# Task 2
# https://www.codewars.com/kata/professor-oaks-trouble-new-pokedex-prototype
# Description:
# Professor Oak has just begun learning Python and he wants to program his new Pokedex prototype with it.
# For a starting point, he wants to instantiate each scanned Pokemon as an object that is stored at Pokedex's memory. He needs your help!
# Your task is to:
# 1) Create a PokeScan class that takes in 3 arguments: name, level and pkmntype.
# 2) Create a info method for this class that returns some comments about the Pokemon, specifying it's name, an observation about the pkmntype and other about the level.
# 3) Keep in mind that he has in his possession just three Pokemons for you to test the scanning function: Squirtle, Charmander and Bulbasaur, of pkmntypes water, fire and grass, respectively.
# 4) The info method shall return a string like this: Charmander, a fiery and strong Pokemon.
# 5) If the Pokemon level is less than or equal to 20, it's a weak Pokemon. If greater than 20 and less than or equal to 50, it's a fair one. If greater than 50, it's a strong Pokemon.
# 6) For the pkmntypes, the observations are wet, fiery and grassy Pokemon, according to each Pokemon type.
# IMPORTANT: The correct spelling of "Pokémon" is "Pokémon", with the "é", but to maximize the compatibility of the code I've had to write it as "Pokemon", without the "é". So, in your code, don't use the "é".
class PokeScan(object):
    pkmntypes = {'water': 'wet', 'fire': 'fiery', 'grass': 'grassy'}

    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = PokeScan.pkmntypes[pkmntype]

    def info(self):
        #FIXME: add check on minus lvl (ex. level = -10)
        if self.level <= 20:
            power = "weak"
        elif 20 < self.level <= 50:
            power = "fair"
        else:
            power = "strong"
        result = "{}, a {} and {} Pokemon.".format(self.name, self.pkmntype, power)
        return result

poke1 = PokeScan("Charmander", 88, "fire")
print(poke1.info())

# Task 3
# https://www.codewars.com/kata/anything
class anything(object):
    def __init__(self, x):
        pass
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return True
    def __gt__(self, other):
        return True
    def __ge__(self, other):
        return True
    def __lt__(self, other):
        return True
    def __le__(self, other):
        return True

class anything2(object):
    def __init__(self, x):
        pass
    def __eq__(self, other):
        return True
    __ne__ = __gt__ = __ge__ = __lt__ = __eq__

# Task 4
# https://www.codewars.com/kata/shop-inventory-manager (Optional)

