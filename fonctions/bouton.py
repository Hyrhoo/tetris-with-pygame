# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:08:28 2022

@author: Hyrhoo
"""

try: 
    from fonctions.interact_object import *
except ModuleNotFoundError or ImportError:
    from interact_object import *


class Bouton(Interact_Object):
    """
    classe de gestion des boutons.
    permet de créée un bouton qui sera stocker dans le tableau de la classe *boutons*
    puis permet de gerer le bouton. en verifient si la souris passe dessus, si le bouton
    est selectionner par le clavier, si le bouton est presser ...
    """

    def __init__(self, fonc, texte = "",  pos_x = mid_screen(0), pos_y = mid_screen(1), hauteur = 70, largeur = 280, taille_texte = 40, texte_font = "franklin gothic heavy", texte_color = (255,255,255), back_color = (50,50,50), arrondissement = 100000, sound = "select"):
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
        Interact_Object.__init__(self, pos_x, pos_y, hauteur, largeur, back_color, arrondissement)
        # initialisation du texte du bouton
        self.texte = texte
        self.taille_texte = resize(taille_texte)
        self.font = pygame.font.SysFont(texte_font, self.taille_texte)
        self.texte_color = texte_color
        self.init_texte_color = texte_color
        self.emplacement_texte = self.font.size(self.texte)
        self.texte_surface = self.font.render(self.texte, True, self.texte_color)

        self.deca = ((self.largeur - self.emplacement_texte[0]) // 2, (self.hauteur - self.emplacement_texte[1]) // 2)
        self.sound = sound
        self.fonc = fonc
        Interact_Object.objects.append(self)
    
    def affichage(self):
        """
        The afficher_bouton function displays the button on the screen.
           It takes as input a pygame surface, and two rectangles. The first rectangle is for the background color of the button, while
           the second one is for text.
        
        :param self: Access variables that belongs to the class
        :return: The rectangle object
        :doc-author: Trelent
        """
        try: from fonctions.fonc import screen_pos
        except ModuleNotFoundError or ImportError: from fonc import screen_pos
        self.emplacement_texte = self.font.size(self.texte)
        self.deca = ((self.largeur - self.emplacement_texte[0]) // 2, (self.hauteur - self.emplacement_texte[1]) // 2)
        self.rectangle.y += screen_pos
        pygame.draw.rect(SCREEN, self.back_color, self.rectangle, 0 , self.arrondisement)
        pygame.draw.rect(SCREEN, changer_couleur_100(self.texte_color, 15), self.rectangle, resize(5) , self.arrondisement)
        SCREEN.blit(self.texte_surface, (self.pos_x + self.deca[0], self.pos_y + self.deca[1] + screen_pos))
        self.rectangle.y -= screen_pos

    def detect_survole(self):
        """
        The detect_bouton_survole function is a function that is called when the mouse is over a button. It changes the color of the button if it's hovered over and unselects any other buttons that may be selected.
        
        :param self: Refer to the object of the class
        :return: Nothing
        :doc-author: Trelent
        """
        survoler = self.objetc_survol()
        if survoler:
            self.texte_color = changer_couleur_100(self.init_texte_color, 5)
        else:
            self.texte_color = self.init_texte_color
        self.texte_surface = self.font.render(self.texte, True, self.texte_color)
        #self.texte_surface.set_colorkey(self.texte_color)
    
    def interact(self, event):
        """
        The bonton_presser function is a function that is called when the user presses the mouse button or presses enter.
        It checks if the bonton has been pressed and calls its fonc function.
        
        :param self: Access the object's attributes
        :param event: Check if the mouse is on the button or not
        :return: The function that is called when the button is pressed
        :doc-author: Trelent
        """
        survoler = self.objetc_survol()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if survoler:
                    play_sound(self.sound)
                    return self.fonc()
        elif event.type == pygame.KEYDOWN:
            if event.key == 13:
                if survoler:
                    play_sound(self.sound)
                    return self.fonc()
        return False