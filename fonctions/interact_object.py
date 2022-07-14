# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:08:28 2022

@author: Hyrhoo
"""

try: 
    from fonctions.fonc import *
    from fonctions.constantes import *
    from fonctions.sound import *
except ModuleNotFoundError or ImportError:
    from fonc import *
    from constantes import *
    from sound import *

class Interact_Object():

    objects = []
    select = -1

    def __init__(self, pos_x, pos_y, hauteur, largeur, back_color, arrondissement):
        self.largeur = resize(largeur)
        self.hauteur = resize(hauteur)
        self.pos_x = pos_x - self.largeur / 2
        self.pos_y = pos_y - self.hauteur / 2
        self.rectangle = pygame.Rect(self.pos_x, self.pos_y, self.largeur, self.hauteur)
        self.arrondisement = resize(arrondissement)
        self.back_color = back_color
        self.init_back_color = back_color
        self.sound_play = False

    def objetc_survol(self):
        try: from fonctions.fonc import screen_pos
        except ModuleNotFoundError or ImportError: from fonc import screen_pos
        survoler = False
        self.rectangle.y += screen_pos
        if self.rectangle.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(11)
            if not self.sound_play:
                play_sound("cursor")
                self.sound_play = True
            self.back_color = changer_couleur_100(self.init_back_color, -25)
            Interact_Object.select = -1
            survoler = True
        elif (Interact_Object.select != -1 and Interact_Object.objects[Interact_Object.select] is self):
            self.back_color = changer_couleur_100(self.init_back_color, -25)
            survoler = True
        else:
            self.back_color = self.init_back_color
            survoler = False
            self.sound_play = False
        self.rectangle.y -= screen_pos
        return survoler


    def deplacer_cursor(event):
        if event.key == 1073741906:
            play_sound("cursor")
            Interact_Object.select -= 1
            if Interact_Object.select < 0:
                Interact_Object.select = len(Interact_Object.objects)-1
        if event.key == 1073741905:
            play_sound("cursor")
            Interact_Object.select += 1
            if Interact_Object.select > len(Interact_Object.objects)-1:
                Interact_Object.select = 0

    def reset_objects():
        Interact_Object.objects.clear()
        Interact_Object.select = -1