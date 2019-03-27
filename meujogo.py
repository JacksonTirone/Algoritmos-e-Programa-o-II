"""Exmaple game."""

import pygame
from window import Window
from game import Game


if __name__ == "__main__":
    pygame.init()
    Window(800, 600).set_title("Olá, sou o PyGame.")
    Game().run()