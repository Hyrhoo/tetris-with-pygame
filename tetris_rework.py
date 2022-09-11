# -*- coding: utf-8 -*-
"""

"""


import sys
import random
import traceback

from fonctions.bouton import *
from fonctions.tirette import *

annonce_font = pygame.font.SysFont("franklin gothic heavy", resize(50))
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
    Bouton(parametre, "Paramètres", pos_y=mid_screen(1)-resize(50), back_color=(23,147,231), texte_color=(15,23,50))
    Bouton(maps, "Maps", pos_y=mid_screen(1)+resize(50), back_color=(231, 147, 157), texte_color=(50,15,20))
    Bouton(scores, "Score", pos_y=mid_screen(1)+resize(150), back_color=(23,231,147), texte_color=(15,50,23))
    Bouton(ask_quitte, "Quitter", pos_y=mid_screen(1)+resize(250), back_color=(255,123,76), texte_color=(50,15,23))
    # main loop du menu principale
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("select")
                ask_quitte()

            # gestion de la pression des boutons
            for object_ in Interact_Object.objects:
                object_.interact(e)

            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("select")
                    ask_quitte()
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
        clock.tick(FPS)

def select_mod():
    reset_scroll()
    Interact_Object.reset_objects()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back", scroll=False)

    Bouton(nul, "Mode Libre", pos_y=mid_screen(1)-resize(350), largeur=300, back_color=(175,215,54), texte_color=(40,50,15), sound="game_loanch")
    Bouton(nul, "40 Lignes", pos_y=mid_screen(1)-resize(200), largeur=300, back_color=(215,198,54), texte_color=(50,45,15), sound="game_loanch")
    Bouton(nul, "150 Lignes", pos_y=mid_screen(1)-resize(100), largeur=300, back_color=(234,173,52), texte_color=(62,40,12), sound="game_loanch")
    Bouton(nul, "300 Lignes", pos_y=mid_screen(1), largeur=300, back_color=(255,129,32), texte_color=(73,32,7), sound="game_loanch")
    Bouton(nul, "1min (60s)", pos_y=mid_screen(1)+resize(150), largeur=300, back_color=(215,198,54), texte_color=(50,45,15), sound="game_loanch")
    Bouton(nul, "2min 30 (150s)", pos_y=mid_screen(1)+resize(250), largeur=300, back_color=(234,173,52), texte_color=(62,40,12), sound="game_loanch")
    Bouton(nul, "5min (300s)", pos_y=mid_screen(1)+resize(350), largeur=300, back_color=(255,129,32), texte_color=(73,32,7), sound="game_loanch")

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("select")
                ask_quitte()
        
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
    
    place_texte_1 = titre_font.size("Paramètres Sonore")
    texte_1 = titre_font.render("Paramètres Sonore", True, (200,200,255))
    texte_2 = menu_font.render("Volume générale :", True, (200,200,255))
    texte_3 = menu_font.render("Volume musique :", True, (200,200,255))
    texte_4 = menu_font.render("Volume éffets sonnors :", True, (200,200,255))

    SCREEN.blit(texte_1, (mid_screen(0) - place_texte_1[0] / 2, resize(130) + screen_pos))
    SCREEN.blit(texte_2, (resize((1536 - 650) / 2), resize(200) + screen_pos))
    SCREEN.blit(texte_3, (resize((1536 - 650) / 2), resize(300) + screen_pos))
    SCREEN.blit(texte_4, (resize((1536 - 650) / 2), resize(400) + screen_pos))

def save_para_vol():
    lecture_fichier("parametres", "w", parametres)
    set_volum_music(parametres["volume"]["global_volume"] * parametres["volume"]["music_volume"])
    set_volum_sounds(parametres["volume"]["global_volume"] * parametres["volume"]["sound_volume"])

def get_touche_name(key, value):
    try:
        name = EQUIVALENT_TOUCHES[key]
    except:
        name = value
    
    return name.title()

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

def changer_touche():
    #from tetris_rework import parametres
    pygame.mouse.set_cursor(0)
    Clock = pygame.time.Clock()
    
    rect = pygame.Rect(mid_screen(0) - resize(350), mid_screen(1) - resize(70), resize(700), resize(140))
    pygame.draw.rect(SCREEN, (50, 50, 50), rect, 0, resize(20))
    pygame.draw.rect(SCREEN, changer_couleur_100((50,50,50), 15), rect, resize(5), resize(20))
    
    place_texte = annonce_font.size("Appuyiez Sur Une Touche")
    texte = annonce_font.render("Appuyiez Sur Une Touche", True, (200, 255, 255))
    SCREEN.blit(texte, (mid_screen(0) - place_texte[0] / 2, mid_screen(1) - place_texte[1] / 2))
    
    pygame.display.flip()
    touche = None
    while touche is None:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                touche = [e.key, e.unicode]
                print(touche, e)
        Clock.tick(FPS)
    play_sound("pause")
    return touche

def changer_para_touche(touche, nouv_touche, nom):
    texte = get_touche_name(touche[0], touche[1])
    if nouv_touche[0] not in TOUCHES_INTERDITE:
        parametres["touches"][nom] = nouv_touche
        texte = get_touche_name(nouv_touche[0], nouv_touche[1])
        lecture_fichier("parametres", "w", parametres)
    return texte


def parametre():
    reset_scroll()
    Interact_Object.reset_objects()

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back", scroll=False)
    tirette_global_volum = Tirette(init_valiu=int(parametres["volume"]["global_volume"]*10), pos_y=resize(265))
    tirette_music_volum = Tirette(init_valiu=int(parametres["volume"]["music_volume"]*10), pos_y=resize(365))
    tirette_sound_volum = Tirette(init_valiu=int(parametres["volume"]["sound_volume"]*10), pos_y=resize(465))
    touche = parametres["touches"]["Chute instantané"]
    touches = [None,]*8
    touches[0] = Bouton(changer_touche, get_touche_name(touche[0], touche[1]), pos_x=resize(1000), pos_y=resize(720), back_color=(120, 220, 255), texte_color=(30, 55, 70), hauteur=40, largeur=130, taille_texte=30, arrondissement=20)
    touche = parametres["touches"]["Chute rapide"]
    touches[1] = Bouton(changer_touche, get_touche_name(touche[0], touche[1]), pos_x=resize(1000), pos_y=resize(768), back_color=(120, 220, 255), texte_color=(30, 55, 70), hauteur=40, largeur=130, taille_texte=30, arrondissement=20)
    touche = parametres["touches"]["Déplacement à droit"]
    touches[2] = Bouton(changer_touche, get_touche_name(touche[0], touche[1]), pos_x=resize(1000), pos_y=resize(816), back_color=(120, 220, 255), texte_color=(30, 55, 70), hauteur=40, largeur=130, taille_texte=30, arrondissement=20)
    touche = parametres["touches"]["Déplacement à gauche"]
    touches[3] = Bouton(changer_touche, get_touche_name(touche[0], touche[1]), pos_x=resize(1000), pos_y=resize(864), back_color=(120, 220, 255), texte_color=(30, 55, 70), hauteur=40, largeur=130, taille_texte=30, arrondissement=20)
    touche = parametres["touches"]["Rotation horair"]
    touches[4] = Bouton(changer_touche, get_touche_name(touche[0], touche[1]), pos_x=resize(1000), pos_y=resize(912), back_color=(120, 220, 255), texte_color=(30, 55, 70), hauteur=40, largeur=130, taille_texte=30, arrondissement=20)
    touche = parametres["touches"]["Rotation anti-horair"]
    touches[5] = Bouton(changer_touche, get_touche_name(touche[0], touche[1]), pos_x=resize(1000), pos_y=resize(960), back_color=(120, 220, 255), texte_color=(30, 55, 70), hauteur=40, largeur=130, taille_texte=30, arrondissement=20)
    touche = parametres["touches"]["Réserve"]
    touches[6] = Bouton(changer_touche, get_touche_name(touche[0], touche[1]), pos_x=resize(1000), pos_y=resize(1008), back_color=(120, 220, 255), texte_color=(30, 55, 70), hauteur=40, largeur=130, taille_texte=30, arrondissement=20)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("select")
                ask_quitte()
        
            for object_ in Interact_Object.objects:
                value = object_.interact(e)
                if object_ is tirette_global_volum:
                    parametres["volume"]["global_volume"] = float(value / 10)
                    save_para_vol()
                elif object_ is tirette_music_volum:
                    parametres["volume"]["music_volume"] = float(value / 10)
                    save_para_vol()
                elif object_ is tirette_sound_volum:
                    parametres["volume"]["sound_volume"] = float(value / 10)
                    save_para_vol()
                if object_ in touches and type(value) == list:
                    nom = noms_touches[touches.index(object_)]
                    texte = changer_para_touche(parametres["touches"][nom], value, nom)
                    object_.texte = texte
            
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

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back", scroll=False)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("select")
                ask_quitte()
        
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

    Bouton(main_menu, "BACK", back_color=(150,100,100), texte_color=(50,0,0), pos_x=resize(55), pos_y=resize(25), hauteur=40, largeur=100, taille_texte=30, sound="back", scroll=False)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play_sound("select")
                ask_quitte()
        
            for object_ in Interact_Object.objects:
                object_.interact(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    main_menu()
                Interact_Object.deplacer_cursor(e)
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

def ask_quitte():
    dic_fonc = {"main_menu": main_menu,
                "select_mod": select_mod,
                "parametre": parametre,
                "maps": maps,
                "scores": scores}

    last_fonc = str(traceback.extract_stack()[-2]).split()[-1].strip(">")
    if last_fonc == "interact": last_fonc = str(traceback.extract_stack()[-3]).split()[-1].strip(">")
    last_fonc = dic_fonc[last_fonc]

    reset_scroll()
    Interact_Object.reset_objects()
    Bouton(quitter_jeu, "Oui", pos_y=mid_screen(1) - resize(10), hauteur=100, largeur=275, taille_texte=60, back_color=(255,123,76), texte_color=(50,15,23), arrondissement=40, sound="quit", scroll=False)
    Bouton(last_fonc, "Annuler", pos_y=mid_screen(1) + resize(110), hauteur=100, largeur=275, taille_texte=60, back_color=(23,231,147), texte_color=(15,50,23), arrondissement=40, sound="back", scroll=False)
    Clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quitter_jeu()

            for object_ in Interact_Object.objects:
                object_.interact(e)

            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    play_sound("back")
                    last_fonc()
                Interact_Object.deplacer_cursor(e)

        # update affichage
        rect = pygame.Rect(mid_screen(0) - resize(300), mid_screen(1) - resize(200), resize(600), resize(400))
        pygame.draw.rect(SCREEN, (50,50,50), rect, 0, resize(20))
        pygame.draw.rect(SCREEN, changer_couleur_100((50,50,50), 15), rect, resize(5), resize(20))

        place_texte_1 = annonce_font.size("Voulez-vous Quitter ?")
        texte_1 = annonce_font.render("Voulez-vous Quitter ?", True, (255,225,225))
        SCREEN.blit(texte_1, (mid_screen(0) - place_texte_1[0] / 2, resize(270) + screen_pos))
        pygame.mouse.set_cursor(0)

        # affichage des objets
        for object_ in Interact_Object.objects:
            object_.detect_survole()
            object_.affichage()

        pygame.display.flip()
        Clock.tick(FPS)


def quitter_jeu():
    pygame.mouse.set_cursor(0)
    stop_all_sound()
    play_sound("quit")
    #time = int(sounds["quit"].get_length() * 1000)
    time = 1500
    pygame.mixer.fadeout(time)
    pygame.mixer.music.fadeout(time)
    pygame.time.wait(time)
    pygame.quit()
    sys.exit()

def nul():
    return

parametres = lecture_fichier("parametres")
noms_touches = ["Chute instantané", "Chute rapide", "Déplacement à droit", "Déplacement à gauche", "Rotation horair", "Rotation anti-horair", "Réserve"]

stop_all_sound()
play_music("main_menu", -1)
set_volum_music(parametres["volume"]["global_volume"] * parametres["volume"]["music_volume"])
set_volum_sounds(parametres["volume"]["global_volume"] * parametres["volume"]["sound_volume"])

try:
    main_menu()        
except RecursionError:
    stop_all_sound()
    pygame.mixer.music.stop()
    pygame.mouse.set_cursor(0)
    smilet_font = pygame.font.SysFont("Segoe UI", resize(170))
    info_font = pygame.font.SysFont("Segoe UI", resize(35))
    error_font = pygame.font.SysFont("Segoe UI", resize(15))

    Clock = pygame.time.Clock()
    nbr = 10
    while nbr:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == 13:
                    nbr -= 1
        
        SCREEN.fill((0, 120, 215))
        
        smilet = smilet_font.render(":(", True, (255,255,255))
        error_1 = info_font.render("Votre PC a rencontré une erreur et doit redémarrer.", True, (255,255,255))
        error_2 = info_font.render("Nous faisons notre possible pour récupérer les", True, (255,255,255))
        error_3 = info_font.render("information à propos de cette erreur.", True, (255,255,255))
        pourcent = info_font.render("20 % achevé", True, (255, 255, 255))
        error_5 = error_font.render("Erreur : Vous avez passé trop de temps à jouer et avez (peut être) trop joué avec les menus.", True, (255, 255, 255))
        error_6 = error_font.render("Vous devez arrêter de jouer et profiter un peu du reste de votre vie.", True, (255, 255, 255))
        error_7 = error_font.render("Cette erreur n'est pas sensée arriver en temps normal, merci de bien vouloir arrêter de jouer avec les menus.", True, (255, 255, 255))
        lien = error_font.render("pour plus d'informations complémentaires, merci de consulter https://www.tetris.error.org", True, (255, 255, 255))

        SCREEN.blit(smilet, (resize(150), resize(70)))
        SCREEN.blit(error_1, (resize(150), resize(300)))
        SCREEN.blit(error_2, (resize(150), resize(350)))
        SCREEN.blit(error_3, (resize(150), resize(400)))
        SCREEN.blit(pourcent, (resize(150), resize(490)))
        SCREEN.blit(error_5, (resize(150), resize(600)))
        SCREEN.blit(error_6, (resize(150), resize(620)))
        SCREEN.blit(error_7, (resize(150), resize(640)))
        SCREEN.blit(lien, (resize(150), resize(700)))
        
        pygame.display.flip()
        Clock.tick(10)