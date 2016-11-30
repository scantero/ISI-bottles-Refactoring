class Bottles:

    def song(self):
        return self.verses(99,0)

    def verses(self, last, first):
        o = self.verse(last)
        for i in range (last-1, first-1, -1):
            o += "\n" + self.verse (i)
        return o

    def verse(self, number=None):
        c = ContainerNumber(number)
        c_ant = ContainerNumber(number-1)
        return "{0} of beer on the wall, ".format(c.upper_first_letter(c.set_of_drinks()) +\
        "{0} of beer.\n".format(c.set_of_drinks()) +\
        c.next_action() +\
        "{0} of beer on the wall.\n".format(c_ant.set_of_drinks())

class ContainerNumber:

    def __init__(self, containers):
        self.containers = containers

    def set_of_drinks(self):
        return "{0} {1}".format(self.units_left(self.containers), c.container(self.containers))

    def units_left(self):
        if self.containers == 0:
            return "no more"
        elif self.containers == -1:
            return str(99)
        else:
            return str(self.containers)

    def container(self):
        if self.containers == 1:
            return "bottle"
        else:
            return "bottles"

    def next_action(self):
        if self.containers == 0:
            return "Go to the store and buy some more, "
        elif self.containers == 1:
            return "Take it down and pass it around, "
        else:
            return "Take one down and pass it around, "

    def upper_first_letter(self, cadena):
        letra = cadena[0]
        cadena = cadena[1:]
        letra = letra.upper()
        return letra + cadena
