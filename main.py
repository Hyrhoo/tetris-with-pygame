# -*- coding: utf-8 -*-
import os
import pathlib
import pygame

from fonctions.constantes import *
from fonctions.fonc import *
from fonctions.color import Color
from fonctions.sound import Sound
from fonctions.screen import Screen
from fonctions.interact_object import Interact_Object
from fonctions.menu import Menu

Sound("data/sound/" + DEFAULT_FOLDER).audio

color = Color(0, 0, 255)
screen = Screen()
objects = [
    Interact_Object(screen, screen.mid_screen(screen.DEFOLT_SCREEN_SIZE[0]), screen.mid_screen(screen.DEFOLT_SCREEN_SIZE[1]), 100, 20, color, color.lighter(20))
]

