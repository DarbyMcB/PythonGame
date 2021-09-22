"""
Terrain File.

Base class for all inherited terrain types

"""
from .Hex import Hex


class Terrain(Hex):
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

    def __init__(self, index=0, radius=0, center=[0, 0], axial=[0, 0], active=0):
        """
        Initialize terrain type for the hex.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description
        """
        super().__init__(index, radius, center, axial, active)
        self._type = ""
        self._gold = 0
        self._VP = 0
        self._prerequisites = 0
        self._defense_bonus = 0
        self._artillery = 0
        self._passable = 0
        self._shoot_over = 0

    """
    PROPERTIES
    """

    if True:
        def get_type(self):
            return self._type

        def set_type(self, type):
            self._type = type

        def del_type(self):
            del self._type
        type = property(get_type, set_type, del_type)

    if True:
        def get_gold(self):
            return self._gold

        def set_gold(self, gold):
            self._gold = gold

        def del_gold(self):
            del self._gold
        gold = property(get_gold, set_gold, del_gold)

    if True:
        def get_VP(self):
            return self._VP

        def set_VP(self, VP):
            self._VP = VP

        def del_VP(self):
            del self._VP
        VP = property(get_VP, set_VP, del_VP)

    if True:
        def get_defense_bonus(self):
            return self._defense_bonus

        def set_defense_bonus(self, defense_bonus):
            self._defense_bonus = defense_bonus

        def del_defense_bonus(self):
            del self._defense_bonus
        defense_bonus = property(get_defense_bonus, set_defense_bonus, del_defense_bonus)

    if True:
        def get_prerequisites(self):
            return self._prerequisites

        def set_prerequisites(self, prerequisites):
            self._prerequisites = prerequisites

        def del_prerequisites(self):
            del self._prerequisites
        prerequisites = property(get_prerequisites, set_prerequisites, del_prerequisites)

    if True:
        def get_artillery(self):
            return self._artillery

        def set_artillery(self, artillery):
            self._artillery = artillery

        def del_artillery(self):
            del self._artillery
        artillery = property(get_artillery, set_artillery, del_artillery)

    if True:
        def get_passable(self):
            return self._passable

        def set_passable(self, passable):
            self._passable = passable

        def del_passable(self):
            del self._passable
        passable = property(get_passable, set_passable, del_passable)

    if True:
        def get_shoot_over(self):
            return self._shoot_over

        def set_shoot_over(self, shoot_over):
            self._shoot_over = shoot_over

        def del_shoot_over(self):
            del self._shoot_over
        shoot_over = property(get_shoot_over, set_shoot_over, del_shoot_over)
