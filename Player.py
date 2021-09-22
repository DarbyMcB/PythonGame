"""
A short description.

A bit longer description.

"""

from Unit import Unit


class Player:
    """
    A short description.

    A bit longer description.

    Args:
     variable (type): description

    Returns:
     type: description

    Raises:
     Exception: description

    """

    def __init__(self, name, location=(0, 0), color=(255, 255, 255)):
        """
        Initialize Player Entity.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        self._name = name
        self._coord = location
        self._color = color
        self._hand = []
        self._gold = 0
        self._gold_income = 0
        self._soldier = []
        self._tank = []
        self._artillery = []
        self.generate_starting_army()

    def generate_starting_army(self):
        for i in range(0, 9):
            self.add_soldier()
        for i in range(0, 4):
            self.add_tank()
        for i in range(0, 2):
            self.add_artillery()

    def draw_card(self, card):
        self._hand.append(card)

    def add_soldier(self):
        self._soldier.append(Unit("Soldier"))

    def add_tank(self):
        self._tank.append(Unit("Tank"))

    def add_artillery(self):
        self._artillery.append(Unit("Artillery"))

    def play_card(self, card_to_play):
        if(card_to_play > len(self._hand)):
            return
        print(self._hand[card_to_play])
        card_played = self._hand[card_to_play]
        self._hand.remove(card_played)
        return card_played

    def show_hand(self):
        for card in self._hand:
            card.display()

    def print_units(self):
        for tank in self._tank:
            print(tank._type)
        for artillery in self._artillery:
            print(artillery._type)
        for soldier in self._soldier:
            print(soldier._type)
