"""
Forest File.

Specific class for Forest Terrain

"""

from Terrain import Terrain


class Forest(Terrain):

    def __init__(self, index, radius):
        """
        Constructs characteristics for a Forest.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        super().__init__(index, radius)
        self._type = "Forest"
        self._gold = 0
        self._VP = 0
        self._defense_bonus = 1
        self._prerequisites = 1
        self._artillery = 0
        self._passable = True
        self._shoot_over = False

        self._color = (0, 255, 0)
