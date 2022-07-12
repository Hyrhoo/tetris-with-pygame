# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:08:28 2022

@author: Hyrhoo
"""

def calcule_multi_reso(screen_size):
    """
    The calcule_multi_reso function calculates the resolution of a screen based on the size of an image.
        Args:
            screen_size (tuple): A tuple containing the width and height of a screen in pixels.
        Returns:
            diff_x (float): The ratio between 1536 and width.
    
    :param screen_size: Calculate the difference between the screen resolution and the image resolution
    :return: The difference between the screen size and the image size
    :doc-author: Trelent
    """
    diff_x = screen_size[0]/1536
    diff_y = screen_size[1]/864
    return min(diff_x, diff_y)

from json import load, dump
try:import pygame
except ImportError: raise ImportError("""
>>> La bibliothèque pygame n'est pas installer sur votre ordinateur
Pour l'installer utilisez la commende "pip install pygame" dans une invite de commande""")

pygame.init()
screen_info = pygame.display.Info()
screen_size = (650, 500)
screen_size = screen_info.current_w, screen_info.current_h
SCREEN = pygame.display.set_mode(screen_size)#, pygame.FULLSCREEN)
screen_pos = 0
clock = pygame.time.Clock()

MULTI_RESO = calcule_multi_reso(screen_size)
screen_size = (1536*MULTI_RESO, 864*MULTI_RESO)

def lecture_fichier(fichier, metod = "r", donner = None):
    if metod == "r":
        with open("data/" + fichier + ".json", metod, encoding="UTF-8") as f:
            contenu = load(f)
        return contenu
    elif metod == "w":
        with open("data/" + fichier + ".json", metod, encoding="UTF-8") as f:
            dump(donner, f, ensure_ascii=False, indent=2)

def resize(valiu: int):
    return int(round(valiu * MULTI_RESO, 0))

def mid_screen(valiu: int, divi: int = 2):
    mid = int(round(screen_size[valiu] // divi, 0))
    return mid

def reset_scroll():
    global screen_pos
    screen_pos = 0

def derouler_screen(haut, bas, e):
    """
    The derouler_screen function is used to scroll through the screen.
    It takes 3 arguments: haut, bas and e.
    h is the top of the screen, b is the bottom of it and e is an event.
    
    :param haut: Set the top of the scrolling region
    :param bas: Define the bottom of the screen
    :param e: Get the mouse position
    :return: The position of the scroll bar
    :doc-author: Trelent
    """
    global screen_pos
    scroll = resize(30)
    if e.button == 4:
        screen_pos += scroll
        if screen_pos > - haut:
            screen_pos = - haut
    elif e.button == 5:
        screen_pos -= scroll
        if screen_pos < - bas:
            screen_pos = - bas

def changer_couleur(couleur, opperation):
    """
    The changer_couleur function takes a list of integers representing the RGB values of a color, and an integer
    representing the amount by which those values should be changed. It returns a new list with each value modified
    by the specified amount.
    
    :param couleur: Define the color to be changed
    :param opperation: Change the color by a certain value
    :return: A list of integers
    :doc-author: Trelent
    """
    n_coul = []
    for i in couleur:
        if opperation < 0:
            n_coul.append(int(round((i / 255) * (255 + opperation), 0)))
        else:
            n_coul.append(int(round(i + ((255 - i) / 255) * opperation, 0)))
    return tuple(n_coul)

def changer_couleur_100(couleur, opperation):
    """
    pareille que l'autre mais avec un pourcentage 

    Args:
        couleur (tuple, list): la couleur a changer
        opperation (int): le pourcentage par lequel changer la couleur

    Returns:
        tuple: nouvel couleur
    """
    n_coul = []
    for i in couleur:
        if opperation < 0:
            n_coul.append(int(round((i / 100) * (100 + opperation), 0)))
        else:
            n_coul.append(int(round(i + ((255 - i) / 100) * opperation, 0)))
    return tuple(n_coul)
