class Bottles:

    def song(self):
        return self.verses(99,0)

    def verses(self, last, first):
        o = self.verse(last)
        for i in range (last-1, first-1, -1):
            o += "\n" + self.verse (i)
        return o

    def verse(self, number = None):
        bottle_number = self.bottleNumberFactory(number)
        next_bottle_number = self.bottleNumberFactory(bottle_number.successor())
        result = \
            "{0} {1} of beer on the wall, ".format(bottle_number.quantity().capitalize(), bottle_number.container()) + \
            "{0} {1} of beer.\n".format(bottle_number.quantity(), bottle_number.container()) + \
            "{0}, ".format(bottle_number.action()) + \
            "{0} {1} of beer on the wall.\n".format(next_bottle_number.quantity(), next_bottle_number.container())

        return result

    def bottleNumberFactory(self, number):
        if number == 0:
            return BottleZero(number)
        elif number == 1:
            return BottleOne(number)
        elif number == 6:
            return BottleSixPack(number)
        else:
            return BottleNumber(number)

class BottleNumber:
    def __init__(self, number):
        self.number = number

    def container(self):
        return "bottles"

    def quantity(self):
        return str(self.number)

    def action(self):
        return "Take {0} down and pass it around".format(self.pronoun())

    def pronoun(self):
        return "one"

    def successor(self):
        return self.number - 1


class BottleOne(BottleNumber):
    def container(self):
        return "bottle"

    def pronoun(self):
        return "it"


class BottleZero(BottleNumber):
    def quantity(self):
        return "no more"

    def action(self):
        return "Go to the store and buy some more"

    def successor(self):
        return 99

class BottleSixPack(BottleNumber):
    def container(self):
        return "six-pack"

    def quantity(self):
        return str(1)
