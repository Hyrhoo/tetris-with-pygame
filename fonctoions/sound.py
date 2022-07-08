try: from fonctoions.constantes import DEFAULT_FOLDER, DEFAULT_EXTENTION
except ModuleNotFoundError or ImportError: from constantes import DEFAULT_FOLDER, DEFAULT_EXTENTION
import pygame
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.set_num_channels(32)
mix = pygame.mixer.Sound

sounds = {}

def test_folder(name, folder, suite, extention):
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
    global sounds
    try: sounds[name] = mix(folder+suite+extention)
    except FileNotFoundError: 
        print("/!\ fichier \"{}\" manquant ou introuvable.\n".format(folder+suite+extention))
        sounds[name] = mix("data/sound/"+DEFAULT_FOLDER+suite+DEFAULT_EXTENTION)

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
    sounds.clear()

    # dossier menu
    test_folder("main_menu",   folder, "/menu/main_menu", extention)
    test_folder("back",        folder, "/menu/back", extention)
    test_folder("select",      folder, "/menu/select", extention)
    test_folder("cursor",      folder, "/menu/cursor", extention)
    test_folder("game_loanch", folder, "/menu/game_loanch", extention)
    test_folder("pause",       folder, "/menu/pause", extention)


    # dossier game
    test_folder("theme_1", folder, "/game/game_theme_1", extention)
    test_folder("theme_2", folder, "/game/game_theme_2", extention)
    test_folder("theme_3", folder, "/game/game_theme_3", extention)

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

    # dossier parti_end du dossier game
    test_folder("danger", folder, "/game/parti_end/danger", extention)
    test_folder("win", folder, "/game/parti_end/win", extention)
    test_folder("lose", folder, "/game/parti_end/lose", extention)

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

def stop_all_sound():
    """
    The stop_all_sound function stops all sounds currently playing.
    
    
    :return: The value none
    :doc-author: Trelent
    """
    for sound in sounds.values():
        sound.stop()