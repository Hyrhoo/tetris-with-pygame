# -*- coding: utf-8 -*-
import pygame
try:
    from fonctions.fonc import *
except ModuleNotFoundError or ImportError:
    from fonc import *

class Screen:
    DEFOLT_SCREEN_SIZE = (1920, 1080)
    SCREEN_INFO = pygame.display.Info()
    SCREEN_SIZE = SCREEN_INFO.current_w, SCREEN_INFO.current_h # (650, 500) (1536, 864)
    MULTI_RESO = min(SCREEN_SIZE[0] // 1920, SCREEN_SIZE[1] // 1080)
    SCROLL = 50
    
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.screen_pos = 0

    def resize(self, value):
        return value * self.MULTI_RESO

    def set_scroll(self, scroll=0):
        self.scroll = scroll

    def scroll_screen(self, maxi, mini, mov):
        self.screen_pos += mov
        if not mini <= self.screen_pos <= maxi:
            self.screen_pos = mini if self.screen_pos < mini else maxi
        self.screen.scroll(0, self.screen_pos)

    @staticmethod
    def mid_screen(value, nb_cut):
        return value / nb_cut
