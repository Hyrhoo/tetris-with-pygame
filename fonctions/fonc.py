# -*- coding: utf-8 -*-
"""

"""

from json import load, dump
try:import pygame
except ImportError: raise ImportError("""
>>> La bibliothèque pygame n'est pas installer sur votre ordinateur
Pour l'installer utilisez la commende "pip install pygame" dans une invite de commande""")

pygame.init()

main_clock = pygame.time.Clock()

def lecture_fichier(fichier, metod = "r", donner = None):
    if metod == "r":
        with open("data/" + fichier + ".json", metod, encoding="UTF-8") as f:
            contenu = load(f)
        return contenu
    elif metod == "w":
        with open("data/" + fichier + ".json", metod, encoding="UTF-8") as f:
            dump(donner, f, ensure_ascii=False, indent=2)


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
