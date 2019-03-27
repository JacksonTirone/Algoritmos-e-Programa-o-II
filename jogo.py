"""Implement a base class for games created using PyGame."""

import pygame


class Game:
    """Base class for a PyGAme game."""

    def __init__(self):
        """Initializes the game object."""
        self.running = False

    def run(self):
        """Runs the game."""
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False