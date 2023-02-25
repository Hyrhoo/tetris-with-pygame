# -*- coding: utf-8 -*-

try:
    from fonctions.screen import *
except ModuleNotFoundError or ImportError:
    from screen import *

class Menu:
    def __init__(self, screen:Screen, objects) -> None:
        pass