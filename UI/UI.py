"""
UI Object File.

UI is a general class containing some content element

"""

import pygame


class UI(object):

    def __init__(self, location, size, content, interactable=False):
        self._location = location
        self._size = size
        self._content = content
        self._interactable = interactable
        self._surface = pygame.Surface(self._size)

    def update(self, content):
        self._content = content
        GAME_FONT = pygame.font.SysFont('Comic Sans MS', 15)
        self._surface.fill((0, 0, 0))
        self._surface = GAME_FONT.render(self._content, False, (255, 255, 255))
        return self._surface
