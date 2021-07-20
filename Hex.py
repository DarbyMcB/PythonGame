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

    def __init__(self, index=0, active=0, radius=0, center_x=0, center_y=0):
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
        self._attribute = 0
        self._index = index
        self._radius = radius
        self._center = [center_x, center_y]
        self._active = active
        self._color = (128*active + 127 - (255 if self._index == 19 else 0),
                       128*active + 127 - (255 if self._index == 19 else 0),
                       128*active + 127 - (255 if self._index == 19 else 0))

    def get_index(self):
        return self._index

    def set_index(self, index):
        self._index = index

    def del_index(self):
        del self._index
    index = property(get_index, set_index, del_index)

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def del_radius(self):
        del self._radius
    radius = property(get_radius, set_radius, del_radius)

    def get_center(self):
        return self._center

    def set_center(self, center):
        self._center = center

    def del_center(self):
        del self._center
    center = property(get_center, set_center, del_center)

    def get_active(self):
        return self._active

    def set_active(self, active):
        self._active = active

    def del_active(self):
        del self._active
    active = property(get_active, set_active, del_active)

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def del_color(self):
        del self._color
    color = property(get_color, set_color, del_color)
