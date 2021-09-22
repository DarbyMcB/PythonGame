"""
Swamp File.

Specific class for Swamp Terrain

"""

from .Terrain import Terrain


class Swamp(Terrain):

    def __init__(self, index, radius):
        """
        Constructs characteristics for a Swamp.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        super().__init__(index, radius)
        self._type = "Swamp"
        self._gold = 0
        self._VP = 0
        self._defense_bonus = -2
        self._prerequisites = 1
        self._artillery = 0
        self._passable = True
        self._shoot_over = False

        self._color = (50, 50, 50)
