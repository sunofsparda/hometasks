# Task1
# https://www.codewars.com/kata/fractions-class/train/python


class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

    def __add__(self, add_fract):
        numerator_x = self.top * add_fract.bottom + self.bottom * add_fract.top
        denominator_x = self.bottom * add_fract.bottom
        for i in range(min(numerator_x, denominator_x), 1, -1):
            if (numerator_x % i == 0) and (denominator_x % i == 0):
                numerator_x /= i
                denominator_x /= i
        return Fraction(int(numerator_x), int(denominator_x))


# Task 2
# https://www.codewars.com/kata/professor-oaks-trouble-new-pokedex-prototype


class PokeScan(object):
    pkmntypes = {'water': 'wet', 'fire': 'fiery', 'grass': 'grassy'}

    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = PokeScan.pkmntypes[pkmntype]

    def info(self):
        # FIXME: add check on minus lvl (ex. level = -10)
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
