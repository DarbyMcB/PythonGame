"""
Plains File.

Specific class for Plains Terrain

"""

from Terrain import Terrain


class Plains(Terrain):

    def __init__(self, index, radius):
        """
        Constructs characteristics for a Plains.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        super().__init__(index, radius)
        self._type = "Plains"
        self._gold = 0
        self._VP = 0
        self._defense_bonus = 0
        self._prerequisites = 1
        self._artillery = 0
        self._passable = True
        self._shoot_over = False

        self._color = (200, 200, 100)
