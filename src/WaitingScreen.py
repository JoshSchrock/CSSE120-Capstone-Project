import pygame
from start import start

class WaitingScreen(start):

    def __init__(self, Menu_Game):
        start.__init__(self, Menu_Game)
        image = pygame.image.load("StartImage.jpg")
        self.image = pygame.transform.scale(image,
                                            (self.Menu_Game.display.get_width(), self.Menu_Game.display.get_height()))

    def display_menu(self):
        self.Menu_Game.check_events()
        self.Menu_Game.display.fill((0, 0, 0))
        self.Menu_Game.display.blit(self.image, (0, 0))
        self.Menu_Game.draw_text('Loading Game...', 30, self.Menu_Game.display.get_width() / 2,
                                 self.Menu_Game.display.get_height() / 2 - 20)
        self.Menu_Game.draw_text('Game Code: ' + self.Menu_Game.game_code, 30, self.Menu_Game.display.get_width() / 2,
                                 self.Menu_Game.display.get_height() / 2 + 20)
        self.Menu_Game.close_button.draw()
        self.blit_screen()