"""
Mountain File.

Specific class for Mountain Terrain

"""

from Terrain import Terrain


class Mountain(Terrain):

    def __init__(self, index, radius):
        """
        Constructs characteristics for a Mountain.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        super().__init__(index, radius)
        self._type = "Mountain"
        self._gold = 0
        self._VP = 0
        self._defense_bonus = 2
        self._prerequisites = 1
        self._artillery = 1  # adds 1 to Artillery rolls from this tile
        self._passable = True
        self._shoot_over = False

        self._color = (255, 0, 0)
