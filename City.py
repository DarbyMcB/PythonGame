"""
City File.

City class for City Terrain

"""

from Terrain import Terrain


class City(Terrain):

    def __init__(self, index, radius):
        """
        Constructs characteristics for a City

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        super().__init__(index, radius)
        self._type = "City"
        self._gold = 2
        self._VP = 1
        self._defense_bonus = 2
        self._prerequisites = 2
        self._artillery = 0
        self._passable = True
        self._shoot_over = False

        self._color = (0, 200, 200)
