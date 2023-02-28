# -*- coding: utf-8 -*-
try:
    from fonctions.screen import Screen
    from fonctions.color import Color
except ModuleNotFoundError or ImportError:
    from screen import Screen
    from color import Color

import pygame

pygame.init()

class Interact_Object:
    def __init__(self, screen: Screen, x: float, y, width: float, height: float, object_color: Color, around_color: Color) -> None:
        self.screen = screen
        self.x = screen.resize(x)
        self.y = screen.resize(y)
        self.width = screen.resize(width)
        self.height = screen.resize(height)
        self.object_color = object_color
        self.around_color = around_color

        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
        self.is_select = False
        self.is_over = False
        self.is_cliqued = False
        self.is_soud_played = False

    def updat(self, event) -> None:
        pass

    def display(self) -> None:
        pass

    def is_select_fonc(self) -> None:
        pass

    def is_over_fonc(self) -> None:
        """
        this fonction change the value of self.is_over:
            - to True is the cursor is over the object
            - to False otherways
        it must be call at every loop
        """
        x, y = pygame.mouse.get_pos()
        self.is_over = pygame.Rect.collidepoint(self.rect, x, y)

    def is_cliqued_fonc(self, event) -> None:
        """
        the fonction change the value of self.is_cliqued:
            - to True if the mouse button is pressed over the object
            - to False if the mouse button is unpressed
        it must be call at every loop

        Args:
            event (pygame event): _description_
        """
        if self.is_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.is_cliqued = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_cliqued = False
        if not self.screen.screen.get_active():
            self.is_cliqued = False

    def si_sound_played_fonc(self) -> None:
        if not self.is_over and not self.is_cliqued:
            self.is_soud_played = False
        elif self.is_cliqued or self.is_over:
            self.is_soud_played = True

if __name__ == "__main__":
    screen = Screen()
    color = Color(0, 0, 255)
    i_object = Interact_Object(screen, screen.mid_screen(screen.DEFOLT_SCREEN_SIZE[0]), 
                               screen.mid_screen(screen.DEFOLT_SCREEN_SIZE[1]),
                               50, 20, color, color.lighter(20))
