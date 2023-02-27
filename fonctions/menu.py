# -*- coding: utf-8 -*-
try:
    from fonctions.screen import Screen
except ModuleNotFoundError or ImportError:
    from screen import Screen

import pygame

pygame.init()

class Menu:
    def __init__(self, screen: Screen, *objects) -> None:
        pass