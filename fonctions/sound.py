# -*- coding: utf-8 -*-
try:
    from fonctions.constantes import DEFAULT_FOLDER, DEFAULT_EXTENTION, SOUND_FOLDER
    from fonctions.init import *
except ModuleNotFoundError or ImportError:
    from constantes import DEFAULT_FOLDER, DEFAULT_EXTENTION, SOUND_FOLDER
    from init import *

class Sound:
    def __init__(self, path) -> None:
        self.not_load_musics = ["/menu/main_menu", "/game/game_theme_1", "/game/game_theme_2", "/game/game_theme_3"]
        self.not_load_sounds = ["/menu/back", "/menu/select", "/menu/cursor", "/menu/cursor1", "/menu/game_loanch", "/menu/quit", "/menu/pause",
                                "/game/game_start/start_1", "/game/game_start/start_2", "/game/level_up/lvl_up_1", "/game/level_up/lvl_up_2", "/game/parti_end/danger", "/game/parti_end/win", "/game/parti_end/lose",
                                "/game/line_clear/single", "/game/line_clear/double", "/game/line_clear/triple", "/game/line_clear/tetris", "/game/line_clear/all_clear",
                                "/game/combo/combo_1", "/game/combo/combo_2", "/game/combo/combo_3", "/game/combo/combo_4", "/game/combo/combo_5", "/game/combo/combo_6", "/game/combo/combo_7", "/game/combo/combo_8",
                                "/game/combo/combo_9", "/game/combo/combo_10", "/game/combo/combo_11", "/game/combo/combo_12", "/game/combo/combo_13", "/game/combo/combo_14", "/game/combo/combo_15+",
                                "/game/move/move", "/game/move/rotate", "/game/move/soft_drop", "/game/move/hard_drop", "/game/move/verouillage", "/game/move/blocked", "/game/move/T-spin", "/game/move/hold"]
        self.audio = {}
        self.audio["sounds"] = {}
        self.audio["musics"] = {}
        self.init_audio(path)
        self.load_not_found()
    
    def init_audio(self, path) -> None:
        for file in pathlib.Path(path).iterdir():
            if file.is_dir():
                self.init_audio(file)
            else:
                name = os.path.splitext(file.name)[0]
                self.load_audio(name, file)
        

    def load_not_found(self) -> None:
        for sound in self.not_load_sounds + self.not_load_musics:
            name = os.path.splitext(pathlib.Path(sound).name)[0]
            print("/!\ fichier \"{}\" manquant ou introuvable.".format(name))
            path = SOUND_FOLDER + DEFAULT_FOLDER + sound + DEFAULT_EXTENTION
            self.load_audio(name, path)

    def load_audio(self, name, path) -> None:
        m = [name in i for i in self.not_load_musics]
        s = [name in i for i in self.not_load_sounds]
        is_music = any(m)
        is_sound = any(s)
        if is_music: 
            self.audio["musics"][name] = os.path.normpath(path)
            del self.not_load_musics[m.index(True)]
        if is_sound: 
            self.audio["sounds"][name] = pygame.mixer.Sound(path)
            del self.not_load_sounds[s.index(True)]
    
    def play_music(self, music, repetition=0) -> None:
        pygame.mixer.music.load(self.audio["musics"][music])
        pygame.mixer.music.play(repetition)
    
    def play_sound(self, sound, repetition=0) -> None:
        self.audio["sounds"][sound].play(repetition)
    

    def set_volum_sounds(self, volum) -> None:
        for sound in self.audio["sounds"].values():
            sound.set_volume(volum)
    
    def stop_all_sounds(self) -> None:
        for sound in self.audio["sounds"].values():
            sound.stop()
    
    @staticmethod
    def set_volum_music(volum) -> None:
        pygame.mixer.music.set_volume(volum)
    
    @staticmethod
    def stop_music() -> None:
        pygame.mixer.music.stop()

if __name__ == "__main__":
    Sound("data/sound/" + DEFAULT_FOLDER)