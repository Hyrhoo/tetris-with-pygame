# -*- coding: utf-8 -*-
"""

"""

try: 
    from fonctions.constantes import DEFAULT_FOLDER, DEFAULT_EXTENTION
except ModuleNotFoundError or ImportError: 
    from constantes import DEFAULT_FOLDER, DEFAULT_EXTENTION

import os
from os.path import exists, normpath
import pathlib
for i in pathlib.Path("data/sound/- Tetris 99 - Switch/menu").iterdir():
    print(i.match("back.mp3"))
import pygame
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.set_num_channels(32)
mix = pygame.mixer.Sound

sounds = {} # name: sound object
musics = {} # name: music folder

class Sound:
    def __init__(self, path) -> None:
        self.not_load_musics = ["main_menu", "game_theme_1", "game_theme_2", "game_theme_3"]
        self.not_load_sounds = ["back", "select", "cursor", "cursor1", "game_loanch", "quit", "pause",
                                "start_1", "start_2", "lvl_up_1", "lvl_up_1", "danger", "win", "lose",
                                "single", "double", "triple", "tetris", "all_clear",
                                "combo_1", "combo_2", "combo_3", "combo_4", "combo_5", "combo_6", "combo_7", "combo_8",
                                "combo_9", "combo_10", "combo_11", "combo_12", "combo_13", "combo_14", "combo_15+",
                                "move", "rotate", "soft_drop", "hard_drop", "verouillage", "blocked", "T-spin", "hold"]
        self.audio = {}
        self.audio["sounds"] = {}
        self.audio["musics"] = {}
        self.init_audio(path)
    
    def init_audio(self, path):
        for file in pathlib.Path(path).iterdir():
            if file.is_dir():
                self.init_audio(file)
            else:
                name = file.name()
                cut = os.path.splitext(name)
                is_music = cut[0] in self.not_load_musics
                if is_music:
                    pass

def test_folder(name, folder, suite, extention, music = False):
    """
    The test_folder function takes a name, folder, suite and extention as arguments. 
    It then creates a sound object from the mix function using the given folder and suite. 
    The sound object is stored in sounds with the given name.
    
    :param name: Store the name of the sound
    :param folder: Specify the folder where the sound files are located
    :param suite: Select the folder that contains the sounds
    :param extention: Select the correct folder
    :return: The value of the sounds dictionary
    :doc-author: Trelent
    """
    global musics
    global sounds
    fichier = folder+suite+extention
    exist = exists(fichier)
    if not exist: 
        print("/!\ fichier \"{}\" manquant ou introuvable.\n".format(fichier))
        fichier = "data/sound/"+DEFAULT_FOLDER+suite+DEFAULT_EXTENTION
    if music: musics[name] = fichier
    if not music: sounds[name] = mix(fichier)

def init_music(folder, extention):
    """
    The init_music function initializes the music for the game.
    It takes a folder and an extention as parameters.
    The function loads all sounds in this folder with this extention, and stores them in a dictionary called sounds.
    
    :param folder: Specify the folder where the sounds are located
    :param extention: Determine the file type of the sound files
    :return: A dictionary of all the sounds
    :doc-author: Trelent
    """
    print("")
    folder = "data/sound/"+folder

    global sounds
    global musics
    sounds.clear()
    musics.clear()

    # dossier menu
    test_folder("main_menu",   folder, "/menu/main_menu", extention, True)
    test_folder("back",        folder, "/menu/back", extention)
    test_folder("select",      folder, "/menu/select", extention)
    test_folder("cursor",      folder, "/menu/cursor", extention)
    test_folder("cursor1",     folder, "/menu/cursor1", extention)
    test_folder("game_loanch", folder, "/menu/game_loanch", extention)
    test_folder("quit",        folder, "/menu/quit", extention)
    test_folder("pause",       folder, "/menu/pause", extention)


    # dossier game
    test_folder("theme_1", folder, "/game/game_theme_1", extention, True)
    test_folder("theme_2", folder, "/game/game_theme_2", extention, True)
    test_folder("theme_3", folder, "/game/game_theme_3", extention, True)

    # dossier game_start du dossier game
    test_folder("pres",       folder, "/game/game_start/start_1", extention)
    test_folder("cest_parti", folder, "/game/game_start/start_2", extention)

    # dossier level_up du dossier game
    test_folder("lvl_up_1", folder, "/game/level_up/lvl_up_1", extention)
    test_folder("lvl_up_2", folder, "/game/level_up/lvl_up_2", extention)

    # dossier line_clear du dossier game
    test_folder("single",    folder, "/game/line_clear/single", extention)
    test_folder("double",    folder, "/game/line_clear/double", extention)
    test_folder("triple",    folder, "/game/line_clear/triple", extention)
    test_folder("tetris",    folder, "/game/line_clear/tetris", extention)
    test_folder("all_clear", folder, "/game/line_clear/all_clear", extention)

    # dossier combo du dossier game
    test_folder("1",   folder, "/game/combo/combo_1", extention)
    test_folder("2",   folder, "/game/combo/combo_2", extention)
    test_folder("3",   folder, "/game/combo/combo_3", extention)
    test_folder("4",   folder, "/game/combo/combo_4", extention)
    test_folder("5",   folder, "/game/combo/combo_5", extention)
    test_folder("6",   folder, "/game/combo/combo_6", extention)
    test_folder("7",   folder, "/game/combo/combo_7", extention)
    test_folder("8",   folder, "/game/combo/combo_8", extention)
    test_folder("9",   folder, "/game/combo/combo_9", extention)
    test_folder("10",  folder, "/game/combo/combo_10", extention)
    test_folder("11",  folder, "/game/combo/combo_11", extention)
    test_folder("12",  folder, "/game/combo/combo_12", extention)
    test_folder("13",  folder, "/game/combo/combo_13", extention)
    test_folder("14",  folder, "/game/combo/combo_14", extention)
    test_folder("15+", folder, "/game/combo/combo_15+", extention)

    # dossier parti_end du dossier game
    test_folder("danger", folder, "/game/parti_end/danger", extention)
    test_folder("win",    folder, "/game/parti_end/win", extention)
    test_folder("lose",   folder, "/game/parti_end/lose", extention)

    # dossier move du dossier game
    test_folder("move",        folder, "/game/move/move", extention)
    test_folder("rotate",      folder, "/game/move/rotate", extention)
    test_folder("soft_drop",   folder, "/game/move/soft_drop", extention)
    test_folder("hard_drop",   folder, "/game/move/hard_drop", extention)
    test_folder("verouillage", folder, "/game/move/verouillage", extention)
    test_folder("blocked",     folder, "/game/move/blocked", extention)
    test_folder("T-spin",      folder, "/game/move/T-spin", extention)
    test_folder("hold",        folder, "/game/move/hold", extention)


    #a = pygame.mixer.Sound(folder+"01 Title"+extention)
    #a.play(fade_ms=)

def play_sound(sound, repetition = 0):
    sounds[sound].play(repetition)

def play_music(music, repetition = 0):
    pygame.mixer.music.load(musics[music])
    pygame.mixer.music.play(repetition)

def stop_all_sound():
    """
    The stop_all_sound function stops all sounds currently playing.
    
    
    :return: The value none
    :doc-author: Trelent
    """
    for sound in sounds.values():
        sound.stop()

def set_volum_music(volum):
    pygame.mixer.music.set_volume(volum)

def set_volum_sounds(volum):
    for sound in sounds.values():
        sound.set_volume(volum)