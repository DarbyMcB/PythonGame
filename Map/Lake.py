"""
Lake File.

Specific class for Lake Terrain

"""

from .Terrain import Terrain


class Lake(Terrain):

    def __init__(self, index, radius):
        """
        Constructs characteristics for a Lake.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        super().__init__(index, radius)
        self._type = "Lake"
        self._gold = 0
        self._VP = 0
        self._defense_bonus = 0
        self._prerequisites = 0
        self._artillery = 0  # adds 1 to Artillery rolls from this tile
        self._passable = False
        self._shoot_over = True

        self._color = (0, 0, 255)
