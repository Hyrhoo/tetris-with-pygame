try:
    from fonctions.fonc import *
except ModuleNotFoundError or ImportError:
    from fonc import *

import pygame

pygame.init()


class Screen:
    DEFOLT_SCREEN_SIZE = (1920, 1080)
    SCREEN_INFO = pygame.display.Info()
    SCREEN_SIZE = SCREEN_INFO.current_w, SCREEN_INFO.current_h # (650, 500) (1536, 864)
    MULTI_RESO = min(SCREEN_SIZE[0] // DEFOLT_SCREEN_SIZE[0], SCREEN_SIZE[1] // DEFOLT_SCREEN_SIZE[1])
    SCROLL = 50
    clock = pygame.time.Clock()

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.screen_pos = 0

    def resize(self, value) -> float:
        return value * self.MULTI_RESO

    def set_scroll(self, scroll=0) -> None:
        self.scroll = scroll

    def scroll_screen(self, maxi, mini, mov) -> None:
        self.screen_pos += mov
        if not mini <= self.screen_pos <= maxi:
            self.screen_pos = mini if self.screen_pos < mini else maxi
        self.screen.scroll(0, self.screen_pos)

    @staticmethod
    def mid_screen(value, nb_cut) -> float:
        return value / nb_cut

if __name__ == "__main__":
    Screen()