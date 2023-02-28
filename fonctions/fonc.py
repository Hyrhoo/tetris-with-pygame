# -*- coding: utf-8 -*-
from json import load, dump
#try:import pygame
#except ImportError: raise ImportError("""
#>>> La bibliothèque pygame n'est pas installer sur votre ordinateur
#Pour l'installer utilisez la commende "pip install pygame" dans une invite de commande""")

def lecture_fichier(fichier, metod = "r", donner = None):
    if metod == "r":
        with open("data/" + fichier + ".json", metod, encoding="UTF-8") as f:
            contenu = load(f)
        return contenu
    elif metod == "w":
        with open("data/" + fichier + ".json", metod, encoding="UTF-8") as f:
            dump(donner, f, ensure_ascii=False, indent=2)
