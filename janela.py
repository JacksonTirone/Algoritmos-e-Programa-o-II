"""Implements a Window object using PyGame."""

import pygame


class Window:
    """Implements a Window object that uses PyGame."""

    def __init__(self, width, height):
        """
        Initialize the window object given its width and height.
        Params:
            width - The window width
            height - The window height
        """
        self._width, self._height = size = (width, height)
        self.screen = pygame.display.set_mode(size)

    def set_title(self, title):
        pygame.display.set_caption(title)

    @property
    def width(self):
        """Return the width of the window."""
        return self._width

    @property
    def height(self):
        """Return the height of the window."""
        return self._height