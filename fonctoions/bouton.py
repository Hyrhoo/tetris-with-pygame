# -*- coding: utf-8 -*-
try: 
    from fonctoions.fonc import *
    from fonctoions.constantes import *
    from fonctoions.sound import *
except ModuleNotFoundError or ImportError: 
    from fonc import *
    from constantes import *
    from sound import *

sound_play = [0, False]

class Bouton():
    """
    classe de gestion des boutons.
    permet de créée un bouton qui sera stocker dans le tableau de la classe *boutons*
    puis permet de gerer le bouton. en verifient si la souris passe dessus, si le bouton
    est selectionner par le clavier, si le bouton est presser ...
    """

    boutons = []
    select = -1

    def __init__(self, fonc, texte = "",  pos_x = mid_screen(0), pos_y = mid_screen(1), hauteur = 70, largeur = 280, taille_texte = 40, texte_font = "franklin gothic heavy", texte_color = (255,255,255), back_color = (50,50,50), arrondisement = 100000, sound = "select"):
        """
        The __init__ function is called automatically every time the class is being used to create a new object.
        The __init__ function can have arguments, some of which are defaulted (e.g., self). 
        The __init__ function is where instance attributes are defined and initialized.
        
        :param self: Reference the object itself
        :param fonc: Execute a function when the button is pressed
        :param texte=&quot;&quot;: Set the text of the button
        :param pos_x=mid_screen(0): Center the button on the x axis
        :param pos_y=mid_screen(1): Center the button on the y axis
        :param hauteur=70: Determine the height of the button
        :param largeur=280: Define the width of the button
        :param taille_texte=40: Set the size of the text on the button
        :param texte_font=&quot;franklingothicheavy&quot;: Choose the font of the text
        :param texte_color=(255: Change the color of the text
        :param 255: Make the color brighter
        :param 255): Define the transparency of the button
        :param back_color=(50: Change the color of the button
        :param 50: Resize the button
        :param 50): Determine the size of the button
        :param arrondisement=100000: Make the button look more round
        :return: ?
        :doc-author: Trelent
        """
        # initialisation du texte du bouton
        self.texte = texte
        self.taille_texte = resize(taille_texte)
        self.font = pygame.font.SysFont(texte_font, self.taille_texte)
        self.texte_color = texte_color
        self.init_texte_color = texte_color
        self.emplacement_texte = self.font.size(self.texte)
        self.texte_surface = self.font.render(self.texte, True, self.texte_color)

        # initialisation de la taille du bouton
        self.largeur = resize(largeur)
        self.hauteur = resize(hauteur)
        self.deca = ((self.largeur - self.emplacement_texte[0]) // 2, (self.hauteur - self.emplacement_texte[1]) // 2)

        # initialisation de l'emplacement du bouton
        self.pos_x = pos_x - self.largeur // 2
        self.pos_y = pos_y - self.hauteur // 2

        # initialisation du rectanle du bouton
        self.rectangle = pygame.Rect(self.pos_x, self.pos_y, self.largeur, self.hauteur)
        self.arrondisement = resize(arrondisement)
        self.back_color = back_color
        self.init_back_color = back_color

        self.sound = sound
        self.fonc = fonc
        Bouton.boutons.append(self)
    
    def afficher_bouton(self):
        """
        The afficher_bouton function displays the button on the screen.
           It takes as input a pygame surface, and two rectangles. The first rectangle is for the background color of the button, while
           the second one is for text.
        
        :param self: Access variables that belongs to the class
        :return: The rectangle object
        :doc-author: Trelent
        """
        self.emplacement_texte = self.font.size(self.texte)
        self.deca = ((self.largeur - self.emplacement_texte[0]) // 2, (self.hauteur - self.emplacement_texte[1]) // 2)
        self.rectangle.y += screen_pos
        pygame.draw.rect(SCREEN, self.back_color, self.rectangle, 0 , self.arrondisement)
        pygame.draw.rect(SCREEN, changer_couleur_100(self.texte_color, 15), self.rectangle, resize(5) , self.arrondisement)
        SCREEN.blit(self.texte_surface, (self.pos_x + self.deca[0], self.pos_y + self.deca[1] + screen_pos))
        self.rectangle.y -= screen_pos

    def detect_bouton_survole(self):
        """
        The detect_bouton_survole function is a function that is called when the mouse is over a button. It changes the color of the button if it's hovered over and unselects any other buttons that may be selected.
        
        :param self: Refer to the object of the class
        :return: Nothing
        :doc-author: Trelent
        """
        global sound_play
        self.rectangle.y += screen_pos
        if self.rectangle.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(11)
            if not sound_play[1]:
                play_sound("cursor")
                sound_play[1] = True
            sound_play[0] = len(Bouton.boutons) + 1
            self.back_color = changer_couleur_100(self.init_back_color, -25)
            self.texte_color = changer_couleur_100(self.init_texte_color, 5)
            Bouton.select = -1
        elif (Bouton.select != -1 and Bouton.boutons[Bouton.select] == self):
            self.back_color = changer_couleur_100(self.init_back_color, -25)
            self.texte_color = changer_couleur_100(self.init_texte_color, 5)
        else:
            self.back_color = self.init_back_color
            self.texte_color = self.init_texte_color
        sound_play[0] -= 1
        if sound_play[0] <= 0: sound_play[1] = False
        self.texte_surface =self.font.render(self.texte, True, self.texte_color)
        #self.texte_surface.set_colorkey(self.texte_color)
        self.rectangle.y -= screen_pos
    
    def bonton_presser(self, event):
        """
        The bonton_presser function is a function that is called when the user presses the mouse button or presses enter.
        It checks if the bonton has been pressed and calls its fonc function.
        
        :param self: Access the object's attributes
        :param event: Check if the mouse is on the button or not
        :return: The function that is called when the button is pressed
        :doc-author: Trelent
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.rectangle.y += screen_pos
            if event.button == 1:
                if self.rectangle.collidepoint(event.pos):
                    self.rectangle.y -= screen_pos
                    play_sound(self.sound)
                    return self.fonc()
            self.rectangle.y -= screen_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == 13:
                if Bouton.select != -1 and Bouton.boutons[Bouton.select] == self:
                    play_sound(self.sound)
                    return self.fonc()
        return False

    def deplacer_cursor(event):
        """
        The deplacer_cursor function is used to move the cursor around the screen.
        It takes an event as a parameter and will move the cursor up, down, left or right depending on what key is pressed.
        
        
        :param event: Get the key that was pressed
        :return: The value of the select variable
        :doc-author: Trelent
        """
        if event.key == 1073741906:
            play_sound("cursor")
            Bouton.select -= 1
            if Bouton.select < 0:
                Bouton.select = len(Bouton.boutons)-1
        if event.key == 1073741905:
            play_sound("cursor")
            Bouton.select += 1
            if Bouton.select > len(Bouton.boutons)-1:
                Bouton.select = 0

    def reset():
        """
        reset les bouton qui ont été créée par la classe
        """
        Bouton.boutons = []
        Bouton.select = -1

def reset_scroll():
    global screen_pos
    screen_pos = 0

def derouler_screen(haut, bas, e):
    """
    The derouler_screen function is used to scroll through the screen.
    It takes 3 arguments: haut, bas and e.
    h is the top of the screen, b is the bottom of it and e is an event.
    
    :param haut: Set the top of the scrolling region
    :param bas: Define the bottom of the screen
    :param e: Get the mouse position
    :return: The position of the scroll bar
    :doc-author: Trelent
    """
    global screen_pos
    scroll = resize(30)
    if e.button == 4:
        screen_pos += scroll
        if screen_pos > bas:
            screen_pos = bas
    elif e.button == 5:
        screen_pos -= scroll
        if screen_pos < haut:
            screen_pos = haut