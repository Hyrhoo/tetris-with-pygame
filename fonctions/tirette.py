# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:08:28 2022

@author: Hyrhoo
"""

try: 
    from fonctions.interact_object import *
except ModuleNotFoundError or ImportError:
    from interact_object import *

class Tirette(Interact_Object):

    def __init__(self, valiu = (0,10), init_valiu = 0, pos_x = mid_screen(0), pos_y = mid_screen(1), hauteur = 40, largeur = 400, eppesseur = 3, taille_boule = 20, back_color = (50,50,50), boule_color = (255,255,255), trait_color = (100,100,100), arrondissement = 100000):
        Interact_Object.__init__(self, pos_x, pos_y, hauteur, largeur, back_color, arrondissement)
        self.valius = range(valiu[0], valiu[1]-1)
        self.first_valiu = self.valius[0]
        self.init_valiu = init_valiu

        self.eppesseur = resize(eppesseur)
        self.start = int(round(self.pos_x + (self.largeur * 0.06), 0))
        self.end = int(round(self.pos_x + (self.largeur * 0.94), 0))
        self.trais_pos_y = (self.pos_y + self.hauteur // 2) - 1
        self.trait_color = trait_color
        self.longueur_trait = self.end - self.start

        self.deca_valiu = self.longueur_trait // (len(self.valius)+1)

        self.taille_boule = resize(taille_boule)
        self.boule_pos_x = self.start - self.taille_boule // 2
        self.boule_pos_y = (self.trais_pos_y + 1) - self.taille_boule // 2
        self.boule = pygame.Rect(self.boule_pos_x, self.boule_pos_y, self.taille_boule, self.taille_boule)
        self.boule_color = boule_color

        Interact_Object.objects.append(self)
    
    def affichage(self):
        try: from fonctions.fonc import screen_pos
        except ModuleNotFoundError or ImportError: from fonc import screen_pos
        self.rectangle.y += screen_pos
        self.boule.y += screen_pos
        pygame.draw.rect(SCREEN, self.back_color, self.rectangle, 0 , self.arrondisement)
        pygame.draw.rect(SCREEN, changer_couleur_100(self.back_color, 15), self.rectangle, resize(5) , self.arrondisement)
        pygame.draw.line(SCREEN, self.trait_color, (self.start, self.trais_pos_y + screen_pos), (self.end, self.trais_pos_y + screen_pos), self.eppesseur)
        self.boule.x += self.deca_valiu * (self.init_valiu - self.first_valiu)
        pygame.draw.rect(SCREEN, self.boule_color, self.boule, 0, self.taille_boule)
        self.boule.x -= self.deca_valiu * (self.init_valiu - self.first_valiu)
        self.rectangle.y -= screen_pos
        self.boule.y -= screen_pos
    
    def detect_survole(self):
        pass

    def interact(self, event):
        pass