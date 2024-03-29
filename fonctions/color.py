# -*- coding: utf-8 -*-
try:
    from fonctions.init import *
except ModuleNotFoundError or ImportError:
    from init import *

class Color(pygame.color.Color):

    def __init__(self, r, g, b, a=255) -> None:
        super().__init__(r, g, b, a)
        self.__initial_r = r
        self.__initial_g = g
        self.__initial_b = b
        self.__initial_a = a
    
    def lighter(self, aditiv_pourcent):
        self.r += round(((255 - self.r)/100) * aditiv_pourcent)
        self.g += round(((255 - self.g)/100) * aditiv_pourcent)
        self.b += round(((255 - self.b)/100) * aditiv_pourcent)
        return self
    
    def lighter_values(self, r, g, b):
        self.r += round(((255 - self.r)/100) * r)
        self.g += round(((255 - self.g)/100) * g)
        self.b += round(((255 - self.b)/100) * b)
        return self
    

    def darcker(self, soustraciv_pourcent):
        self.r = round((self.r/100) * (100-soustraciv_pourcent))
        self.g = round((self.g/100) * (100-soustraciv_pourcent))
        self.b = round((self.b/100) * (100-soustraciv_pourcent))
        return self
    
    def darcker_values(self, r, g, b):
        self.r = round((self.r/100) * (100-r))
        self.g = round((self.g/100) * (100-g))
        self.b = round((self.b/100) * (100-b))
        return self
    
    def restor_color(self):
        self.r = self.__initial_r
        self.g = self.__initial_g
        self.b = self.__initial_b
        self.a = self.__initial_a
        return self


if __name__ == "__main__":
    color1 = Color(1, 125, 255)
    color = Color(100, 100, 100)
    print(color.darcker(90))
    print(color)
    for i in range(5):
        print(color1)
        color1.lighter(10)
        print(color1)
        color1.darcker(10)
    print(color1)