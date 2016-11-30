class Bottles:

    def song(self):
        return self.verses(99,0)

    def verses(self, last, first):
        o = self.verse(last)
        for i in range (last-1, first-1, -1):
            o += "\n" + self.verse (i)
        return o

    def units_left(self, number):
        if number == 0:
            return "no more"
        elif number == -1:
            return str(99)
        else:
            return str(number)

    def container(self, number):
        if number == 1:
            return "bottle"
        else:
            return "bottles"

    def next_action(self, number):
        if number == 0:
            return "Go to the store and buy some more, "
        elif number == 1:
            return "Take it down and pass it around, "
        else:
            return "Take one down and pass it around, "

    def upper_first_letter(self, cadena):
        letra = cadena[0]
        cadena = cadena[1:]
        letra = letra.upper()
        return letra + cadena

    def verse(self, number = None):
        return "{0} {1} of beer on the wall, ".format(self.upper_first_letter(self.units_left(number)), self.container(number)) +\
        "{0} {1} of beer.\n".format(self.units_left(number), self.container(number)) +\
        self.next_action(number) +\
        "{0} {1} of beer on the wall.\n".format(self.units_left(number-1), self.container(number-1))
