# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:08:28 2022

@author: jojoj
"""

import sys
import random
from json import load, dump
from unicodedata import decimal

from fonctoions.bouton import *

ca_background = "data/images/background/"
main_menu_background = pygame.image.load(ca_background + "main_background.png").convert_alpha()
main_menu_background = pygame.transform.scale(main_menu_background, (resize(1536), resize(864)))

parametres_background = pygame.image.load(ca_background + "parametres_background.jpg").convert()
parametres_background = pygame.transform.scale(parametres_background, (resize(1536), resize(864)))

map_background = pygame.image.load(ca_background + "maps_background.jpg").convert()
map_background = pygame.transform.scale(map_background, (resize(1536), resize(864)))

scores_background = pygame.image.load(ca_background + "scores_background.jpg").convert()
scores_background = pygame.transform.scale(scores_background, (resize(1536), resize(864)))

jeu_background = pygame.image.load(ca_background + "jeu_background.jpg").convert()
jeu_background = pygame.transform.scale(jeu_background, (resize(1536), resize(864)))

init_music("- Tetris 99 - Switch", ".wav")

def kaka_proutprout():
    with open("map/map1.json", "r") as f:
        plateau,piece = load(f)
    print(plateau, piece)

plateau = [[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]


def reset_scroll_main():
    reset_scroll()
    global screen_pos
    screen_pos = 0

def derouler_screen_main(haut, bas, e):
    derouler_screen(haut, bas, e)
    global screen_pos
    scroll = resize(30)
    if e.button == 4:
        screen_pos += scroll
        if screen_pos > bas:
            screen_pos = bas
    elif e.button == 5:
        screen_pos -= scroll
        if screen_pos < haut:
            screen_pos = haut

def lecture_fichier(fichier, metod = "r"):
    with open("data/" + fichier + ".json", metod, encoding="UTF-8") as f:
        contenu = load(f)
    return contenu


def main_menu():
    global screen_pos
    screen_pos = 0
    reset_scroll_main()
    Bouton.reset()
    # initialisation des boutons
    Bouton(select_mod, "Jouer", pos_y=mid_screen(1)-resize(150), back_color=(249,198,54), texte_color=(50,50,15))
    Bouton(parametre, "Paramètres", pos_y=mid_screen(1)-resize(50), back_color=(23,147,231), texte_color=(15,23,50))
    Bouton(maps, "Maps", pos_y=mid_screen(1)+resize(50), back_color=(231, 147, 157), texte_color=(50,15,20))
    Bouton(scores, "Score", pos_y=mid_screen(1)+resize(150), back_color=(23,231,147), texte_color=(15,50,23))
    Bouton(quitter_jeu, "Quitter", pos_y=mid_screen(1)+resize(250), back_color=(255,123,76), texte_color=(50,15,23))
    # main loop du menu principale
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quitter_jeu()

            # gestion de la pression des boutons
            for bouton in Bouton.boutons:
                bouton.bonton_presser(e)

            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    quitter_jeu()
                Bouton.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen_main(0, 0, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(main_menu_background, (0, 0-screen_size[1]//2.8))
        pygame.mouse.set_cursor(0)
        # affichage des boutons
        for bouton in Bouton.boutons:
            bouton.detect_bouton_survole()
            bouton.afficher_bouton()
        pygame.display.flip()
        
        # set fps
        clock.tick(60)

def select_mod():
    global screen_pos
    screen_pos = 0
    reset_scroll_main()
    Bouton.reset()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back")

    Bouton(nul, "mode libre", pos_y=mid_screen(1)-resize(350), largeur=300, back_color=(175,215,54), texte_color=(40,50,15), sound="game_loanch")
    Bouton(nul, "40 lignes", pos_y=mid_screen(1)-resize(200), largeur=300, back_color=(215,198,54), texte_color=(50,45,15), sound="game_loanch")
    Bouton(nul, "150 lignes", pos_y=mid_screen(1)-resize(100), largeur=300, back_color=(234,173,52), texte_color=(62,40,12), sound="game_loanch")
    Bouton(nul, "300 lignes", pos_y=mid_screen(1), largeur=300, back_color=(255,129,32), texte_color=(73,32,7), sound="game_loanch")
    Bouton(nul, "1min (60s)", pos_y=mid_screen(1)+resize(150), largeur=300, back_color=(215,198,54), texte_color=(50,45,15), sound="game_loanch")
    Bouton(nul, "2min 30 (150s)", pos_y=mid_screen(1)+resize(250), largeur=300, back_color=(234,173,52), texte_color=(62,40,12), sound="game_loanch")
    Bouton(nul, "5min (300s)", pos_y=mid_screen(1)+resize(350), largeur=300, back_color=(255,129,32), texte_color=(73,32,7), sound="game_loanch")

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quitter_jeu()
        
            for bouton in Bouton.boutons:
                bouton.bonton_presser(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Bouton.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen_main(0, 0, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(jeu_background, (0,0))
        pygame.mouse.set_cursor(0)
        # affichage des boutons
        for bouton in Bouton.boutons:
            bouton.detect_bouton_survole()
            bouton.afficher_bouton()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def parametre():
    global screen_pos
    screen_pos = 0
    reset_scroll_main()
    Bouton.reset()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back")

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quitter_jeu()
        
            for bouton in Bouton.boutons:
                bouton.bonton_presser(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Bouton.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen_main(-100, 0, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(parametres_background, (0,0))
        pygame.mouse.set_cursor(0)
        # affichage des boutons
        for bouton in Bouton.boutons:
            bouton.detect_bouton_survole()
            bouton.afficher_bouton()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def maps():
    global screen_pos
    screen_pos = 0
    reset_scroll_main()
    Bouton.reset()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back")

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quitter_jeu()
        
            for bouton in Bouton.boutons:
                bouton.bonton_presser(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Bouton.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen_main(0, 0, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(map_background, (0,0))
        pygame.mouse.set_cursor(0)
        # affichage des boutons
        for bouton in Bouton.boutons:
            bouton.detect_bouton_survole()
            bouton.afficher_bouton()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def scores():
    global screen_pos
    screen_pos = 0
    reset_scroll_main()
    Bouton.reset()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back")

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quitter_jeu()
        
            for bouton in Bouton.boutons:
                bouton.bonton_presser(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Bouton.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen_main(-100, 0, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(scores_background, (0,0))
        pygame.mouse.set_cursor(0)
        # affichage des boutons
        for bouton in Bouton.boutons:
            bouton.detect_bouton_survole()
            bouton.afficher_bouton()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def quitter_jeu():
    pygame.time.wait(260)
    pygame.quit()
    sys.exit()

def nul():
    return

print(lecture_fichier("scores/scores_libre"))
touches = lecture_fichier("touches")
stop_all_sound()
play_sound("main_menu", -1)
main_menu()        
