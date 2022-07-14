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

    def __init__(self, valiu = (0,10), init_valiu = 0, pos_x = mid_screen(0), pos_y = mid_screen(1), hauteur = 40, largeur = 400, eppesseur = 3, taille_boule = 20, texte_font = "franklin gothic heavy", texte_color = (150,150,150), back_color = (50,50,50), boule_color = (255,255,255), trait_color = (100,100,100), arrondissement = 100000):
        Interact_Object.__init__(self, pos_x, pos_y, hauteur, largeur, back_color, arrondissement)
        self.valius = range(valiu[0], valiu[1]+1)
        self.init_valiu = init_valiu

        self.eppesseur = resize(eppesseur)
        self.start = self.pos_x + (self.largeur * 0.15)
        self.end = self.pos_x + (self.largeur * 0.85)
        self.trais_pos_y = (self.pos_y + self.hauteur / 2) - 1
        self.trait_color = trait_color
        self.longueur_trait = self.end - self.start

        self.place_texte = self.start - (self.pos_x + self.hauteur / 4)
        self.taille_texte = min(int(round(self.hauteur * 0.75, 0)), int(round(self.place_texte / len(str(self.valius[-1])) * 0.75, 0)))
        self.font = pygame.font.SysFont(texte_font, self.taille_texte)
        self.texte_color = texte_color

        self.deca_valiu = self.longueur_trait / (len(self.valius)-1)

        self.taille_boule = resize(taille_boule)
        self.boule_pos_x = self.start - self.taille_boule / 2
        self.boule_pos_y = (self.trais_pos_y + 1) - self.taille_boule / 2
        self.boule = pygame.Rect(self.boule_pos_x, self.boule_pos_y, self.taille_boule, self.taille_boule)
        self.boule_color = boule_color

        # pos x = début + arrondi + moitier de la place disspo - moitier de la taille du texte
        self.pos_x_texte_1 = self.pos_x + self.hauteur / 4 + self.place_texte / 2 - self.font.size(str(self.valius[0]))[0] / 2
        self.pos_x_texte_2 = self.end + self.place_texte / 2 - self.font.size(str(self.valius[-1]))[0] / 2
        self.pos_y_texte = self.pos_y + self.hauteur / 2 - self.font.size(str(self.valius[0]))[1] / 2
        self.texte_1 = self.font.render(str(self.valius[0]), True, self.texte_color)
        self.texte_2 = self.font.render(str(self.valius[-1]), True, self.texte_color)

        Interact_Object.objects.append(self)

    def calcul_indication(self):
        try: from fonctions.fonc import screen_pos
        except ModuleNotFoundError or ImportError: from fonc import screen_pos
        taille = self.font.size(str(self.init_valiu))
        hauteur = taille[1] + taille[1] / 3
        largeur = taille[0] + taille[1] / 1.5
        y = self.pos_y - hauteur / 0.78
        x = self.boule_pos_x + self.deca_valiu * (self.init_valiu - self.valius[0]) + self.taille_boule / 2 - largeur / 2
        self.rectangle_indic = pygame.Rect(x, y + screen_pos, largeur, hauteur)
        self.texte_indic = self.font.render(str(self.init_valiu), True, self.texte_color)
        self.pos_texte_indic_x = x + largeur / 2 - taille[0] / 2
        self.pos_texte_indic_y = y + hauteur / 2 - taille[1] / 2 + screen_pos


    def affichage(self):
        try: from fonctions.fonc import screen_pos
        except ModuleNotFoundError or ImportError: from fonc import screen_pos
        self.rectangle.y += screen_pos
        self.boule.y += screen_pos
        pygame.draw.rect(SCREEN, self.back_color, self.rectangle, 0 , self.arrondisement)
        pygame.draw.rect(SCREEN, changer_couleur_100(self.back_color, 15), self.rectangle, resize(5) , self.arrondisement)

        SCREEN.blit(self.texte_1, (self.pos_x_texte_1, self.pos_y_texte + screen_pos))
        SCREEN.blit(self.texte_2, (self.pos_x_texte_2, self.pos_y_texte + screen_pos))

        pygame.draw.line(SCREEN, self.trait_color, (self.start, self.trais_pos_y + screen_pos), (self.end, self.trais_pos_y + screen_pos), self.eppesseur)
        self.boule.x += self.deca_valiu * (self.init_valiu - self.valius[0])
        pygame.draw.rect(SCREEN, self.boule_color, self.boule, 0, self.taille_boule)
        self.boule.x -= self.deca_valiu * (self.init_valiu - self.valius[0])
        self.rectangle.y -= screen_pos
        self.boule.y -= screen_pos
    
    def detect_survole(self):
        survoler = self.objetc_survol()
        if survoler:
            self.calcul_indication()
            pygame.draw.rect(SCREEN, self.init_back_color, self.rectangle_indic, 0 , resize(10))
            pygame.draw.rect(SCREEN, changer_couleur_100(self.init_back_color, 15), self.rectangle_indic, resize(3) , resize(10))
            SCREEN.blit(self.texte_indic, (self.pos_texte_indic_x, self.pos_texte_indic_y + screen_pos))

    def interact(self, event):
        survoler = self.objetc_survol()
        value = self.init_valiu
        if pygame.mouse.get_pressed()[0]:
                if survoler:
                    self.init_valiu = int(round((pygame.mouse.get_pos()[0] - self.start) / self.deca_valiu, 0))
                    if self.init_valiu < self.valius[0]: self.init_valiu = self.valius[0]
                    elif self.init_valiu > self.valius[-1]: self.init_valiu = self.valius[-1]
        if event.type == pygame.KEYDOWN:
            if survoler:
                if event.key == pygame.K_RIGHT:
                    self.init_valiu += 1
                elif event.key == pygame.K_LEFT:
                    self.init_valiu -= 1
                if self.init_valiu < self.valius[0]: self.init_valiu = self.valius[0]
                elif self.init_valiu > self.valius[-1]: self.init_valiu = self.valius[-1]
        if value != self.init_valiu:
            play_sound("cursor1")
        return self.init_valiu