# -*- coding: utf-8 -*-
try:
    from fonctions.screen import Screen
    from fonctions.init import *
except ModuleNotFoundError or ImportError:
    from screen import Screen
    from init import *

class Menu:
    def __init__(self, screen: Screen, *objects) -> None:
        pass