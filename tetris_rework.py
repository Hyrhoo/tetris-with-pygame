# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:08:28 2022

@author: Hyrhoo
"""

import sys
import random
from unicodedata import decimal

from fonctions.bouton import *
from fonctions.tirette import *

titre_font = pygame.font.SysFont("franklin gothic heavy", resize(40))
menu_font = pygame.font.SysFont("franklin gothic heavy", resize(25))

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

init_music("- Tetris 99 - Switch", ".mp3")

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



def main_menu():
    reset_scroll()
    Interact_Object.reset_objects()
    # initialisation des boutons
    Bouton(select_mod, "Jouer", pos_y=mid_screen(1)-resize(150), back_color=(249,198,54), texte_color=(50,50,15))
    Bouton(parametre, "Param??tres", pos_y=mid_screen(1)-resize(50), back_color=(23,147,231), texte_color=(15,23,50))
    Bouton(maps, "Maps", pos_y=mid_screen(1)+resize(50), back_color=(231, 147, 157), texte_color=(50,15,20))
    Bouton(scores, "Score", pos_y=mid_screen(1)+resize(150), back_color=(23,231,147), texte_color=(15,50,23))
    Bouton(quitter_jeu, "Quitter", pos_y=mid_screen(1)+resize(250), back_color=(255,123,76), texte_color=(50,15,23), sound="quit")
    # main loop du menu principale
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("game_loanch")
                quitter_jeu()

            # gestion de la pression des boutons
            for object_ in Interact_Object.objects:
                object_.interact(e)

            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("game_loanch")
                    quitter_jeu()
                Interact_Object.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen(0, 864, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(main_menu_background, (0, 0-screen_size[1]/2.8))
        pygame.mouse.set_cursor(0)
        # affichage des objets
        for object_ in Interact_Object.objects:
            object_.detect_survole()
            object_.affichage()
        pygame.display.flip()
        
        # set fps
        clock.tick(60)

def select_mod():
    reset_scroll()
    Interact_Object.reset_objects()

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
                play_sound("game_loanch")
                quitter_jeu()
        
            for object_ in Interact_Object.objects:
                object_.interact(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Interact_Object.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen(0, 864, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(jeu_background, (0,0))
        pygame.mouse.set_cursor(0)
        # affichage des objets
        for object_ in Interact_Object.objects:
            object_.detect_survole()
            object_.affichage()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def affichage_para_vol():
    from fonctions.fonc import screen_pos
    back_rect = pygame.Rect(resize((1536 - 750) / 2), resize(100) + screen_pos, resize(750), resize(430))
    pygame.draw.rect(SCREEN, (55,37,54), back_rect, 0, 20)
    
    place_texte_1 = titre_font.size("Param??tres de volumes")
    texte_1 = titre_font.render("Param??tres de volumes", True, (200,200,255))
    texte_2 = menu_font.render("Volume g??n??rale :", True, (200,200,255))
    texte_3 = menu_font.render("Volume musique :", True, (200,200,255))
    texte_4 = menu_font.render("Volume ??ffets sonnors :", True, (200,200,255))

    SCREEN.blit(texte_1, (mid_screen(0) - place_texte_1[0] / 2, resize(130) + screen_pos))
    SCREEN.blit(texte_2, (resize((1536 - 650) / 2), resize(200) + screen_pos))
    SCREEN.blit(texte_3, (resize((1536 - 650) / 2), resize(300) + screen_pos))
    SCREEN.blit(texte_4, (resize((1536 - 650) / 2), resize(400) + screen_pos))

def affichage_para_control():
    from fonctions.fonc import screen_pos
    back_rect = pygame.Rect(resize((1536 - 750) / 2), resize(600) + screen_pos, resize(750), resize(470))
    pygame.draw.rect(SCREEN, (55,37,54), back_rect, 0, 20)

    place_texte_1 = titre_font.size("Controles")
    texte_1 = titre_font.render("Controles", True, (200,200,255))
    SCREEN.blit(texte_1, (mid_screen(0) - place_texte_1[0] / 2, resize(630) + screen_pos))

    keys = list(parametres["touches"].keys())
    for i in range(len(keys)):
        texte = menu_font.render(keys[i], True, (200,200,255))
        SCREEN.blit(texte, (resize((1536 - 650) / 2), resize(700 + 50 * i) + screen_pos))

def parametre():
    reset_scroll()
    Interact_Object.reset_objects()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back")
    tirette_global_volum = Tirette(init_valiu=int(parametres["volume"]["global_volume"]*10), pos_y=resize(265))
    tirette_music_volum = Tirette(init_valiu=int(parametres["volume"]["music_volume"]*10), pos_y=resize(365))
    tirette_sound_volum = Tirette(init_valiu=int(parametres["volume"]["sound_volume"]*10), pos_y=resize(465))

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("game_loanch")
                quitter_jeu()
        
            for object_ in Interact_Object.objects:
                value = object_.interact(e)
                if object_ is tirette_global_volum:
                    parametres["volume"]["global_volume"] = float(value / 10)
                    lecture_fichier("parametres", "w", parametres)
                    set_volum_music(parametres["volume"]["global_volume"] * parametres["volume"]["music_volume"])
                    set_volum_sounds(parametres["volume"]["global_volume"] * parametres["volume"]["sound_volume"])
                elif object_ is tirette_music_volum:
                    parametres["volume"]["music_volume"] = float(value / 10)
                    lecture_fichier("parametres", "w", parametres)
                    set_volum_music(parametres["volume"]["global_volume"] * parametres["volume"]["music_volume"])
                elif object_ is tirette_sound_volum:
                    parametres["volume"]["sound_volume"] = float(value / 10)
                    lecture_fichier("parametres", "w", parametres)
                    set_volum_sounds(parametres["volume"]["global_volume"] * parametres["volume"]["sound_volume"])
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Interact_Object.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen(0, 1170, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(parametres_background, (0,0))
        affichage_para_vol()
        affichage_para_control()
        pygame.mouse.set_cursor(0)
        # affichage des objets
        for object_ in Interact_Object.objects:
            object_.detect_survole()
            object_.affichage()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def maps():
    reset_scroll()
    Interact_Object.reset_objects()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back")

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("game_loanch")
                quitter_jeu()
        
            for object_ in Interact_Object.objects:
                object_.interact(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Bouton.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen(0, 864, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(map_background, (0,0))
        pygame.mouse.set_cursor(0)
        # affichage des objets
        for object_ in Interact_Object.objects:
            object_.detect_survole()
            object_.affichage()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def scores():
    reset_scroll()
    Interact_Object.reset_objects()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back")

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("game_loanch")
                quitter_jeu()
        
            for object_ in Interact_Object.objects:
                object_.interact(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Bouton.deplacer_cursor(e)
                print(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                derouler_screen(0, 964, e)
        
        # update affichage
        SCREEN.fill((54,57,63))
        SCREEN.blit(scores_background, (0,0))
        pygame.mouse.set_cursor(0)
        # affichage des objets
        for object_ in Interact_Object.objects:
            object_.detect_survole()
            object_.affichage()
        pygame.display.flip()
        
        # set fps
        clock.tick(FPS)

def quitter_jeu():
    pygame.time.wait(550)
    pygame.quit()
    sys.exit()

def nul():
    return

parametres = lecture_fichier("parametres")

stop_all_sound()
play_music("main_menu", -1)
set_volum_music(parametres["volume"]["global_volume"] * parametres["volume"]["music_volume"])
set_volum_sounds(parametres["volume"]["global_volume"] * parametres["volume"]["sound_volume"])

main_menu()        
