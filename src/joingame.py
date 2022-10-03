import pygame
from start import start
from input_text import input_text

class joingame(start):

    def __init__(self, Menu_Game):
        start.__init__(self, Menu_Game)
        # self.inputBox = input_text(self.mid_w - 150, self.mid_h + 50, 300, 600)
        self.inputBox = input_text((self.Menu_Game.display.get_width() / 2) - 200, (self.Menu_Game.display.get_height() / 2), 400, 120, 6)
        image = pygame.image.load("StartImage.jpg")
        self.image = pygame.transform.scale(image,
                                            (self.Menu_Game.display.get_width(), self.Menu_Game.display.get_height()))


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.Menu_Game.check_events()
            self.check_input()
            self.Menu_Game.display.fill((0, 0, 0))
            self.Menu_Game.display.blit(self.image, (0, 0))
            self.inputBox.draw(self.Menu_Game.display)
            self.Menu_Game.draw_text('Type in Code', 30, self.Menu_Game.display.get_width() / 2, self.Menu_Game.display.get_height() / 2 - 20)
            self.Menu_Game.close_button.draw()
            self.blit_screen()

    def check_input(self):
        if self.Menu_Game.BACK_KEY and not self.inputBox.active:
            self.Menu_Game.curr_menu = self.Menu_Game.main_menu
            self.run_display = False
