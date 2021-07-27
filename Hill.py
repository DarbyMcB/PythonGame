"""
Hill File.

Specific class for Hill Terrain

"""

from Terrain import Terrain


class Hill(Terrain):

    def __init__(self, index, radius):
        """
        Constructs characteristics for a Hill.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        super().__init__(index, radius)
        self._type = "Hill"
        self._gold = 0
        self._VP = 0
        self._defense_bonus = 1
        self._prerequisites = 1
        self._artillery = 1  # adds 1 to Artillery rolls from this tile
        self._passable = True
        self._shoot_over = False

        self._color = (200, 100, 0)
