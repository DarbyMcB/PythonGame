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

import random


class Hex:
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

    def __init__(self, index=0, radius=0, center_x=0, center_y=0):
        """
        Initialize Hex.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        self.index = index
        self.radius = radius
        self.center = [center_x, center_y]
        self.active = 0
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
