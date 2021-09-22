

class Unit(object):

    def __init__(self, type):
        if (type == "Tank"):
            self._type = "Tank"
            self._damage = 10
            self._range = 1
        elif (type == "Artillery"):
            self._type = "Artillery"
            self._damage = 10
            self._range = 2
        elif (type == "Soldier"):
            self._type = "Soldier"
            self._damage = 6
            self._range = 1
