
import pygame
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.set_num_channels(32)

sounds = {}
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
    mix = pygame.mixer.Sound
    folder = "data/sound/"+folder

    global sounds
    sounds.clear()

    # dossier menu
    sounds["main_menu"] = mix(folder+"/menu/main_menu"+extention)
    sounds["back"] = mix(folder+"/menu/back"+extention)
    sounds["select"] = mix(folder+"/menu/select"+extention)
    sounds["cursor"] = mix(folder+"/menu/cursor"+extention)
    sounds["game_loanch"] = mix(folder+"/menu/game_loanch"+extention)
    sounds["pause"] = mix(folder+"/menu/pause"+extention)


    # dossier game
    sounds["theme_1"] = mix(folder+"/game/game_theme_1"+extention)
    sounds["theme_2"] = mix(folder+"/game/game_theme_2"+extention)
    sounds["theme_3"] = mix(folder+"/game/game_theme_3"+extention)

    # dossier game_start du dossier game
    sounds["pres"] = mix(folder+"/game/game_start/start_1"+extention)
    sounds["cest_parti"] = mix(folder+"/game/game_start/start_2"+extention)

    # dossier level_up du dossier game
    sounds["lvl_up_1"] = mix(folder+"/game/level_up/lvl_up_1"+extention)
    sounds["lvl_up_2"] = mix(folder+"/game/level_up/lvl_up_2"+extention)

    # dossier line_clear du dossier game
    sounds["single"] = mix(folder+"/game/line_clear/single"+extention)
    sounds["double"] = mix(folder+"/game/line_clear/double"+extention)
    sounds["triple"] = mix(folder+"/game/line_clear/triple"+extention)
    sounds["tetris"] = mix(folder+"/game/line_clear/tetris"+extention)
    sounds["all_clear"] = mix(folder+"/game/line_clear/all_clear"+extention)

    # dossier parti_end du dossier game
    sounds["danger"] = mix(folder+"/game/parti_end/danger"+extention)
    sounds["win"] = mix(folder+"/game/parti_end/win"+extention)
    sounds["lose"] = mix(folder+"/game/parti_end/lose"+extention)

    # dossier move du dossier game
    sounds["move"] = mix(folder+"/game/move/move"+extention)
    sounds["rotate"] = mix(folder+"/game/move/rotate"+extention)
    sounds["soft_drop"] = mix(folder+"/game/move/soft_drop"+extention)
    sounds["hard_drop"] = mix(folder+"/game/move/hard_drop"+extention)
    sounds["verouillage"] = mix(folder+"/game/move/verouillage"+extention)
    sounds["blocked"] = mix(folder+"/game/move/blocked"+extention)
    sounds["T-spin"] = mix(folder+"/game/move/T-spin"+extention)
    sounds["hold"] = mix(folder+"/game/move/hold"+extention)


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