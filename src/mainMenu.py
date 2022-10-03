import pygame
from start import start

class MainMenu(start):
    def __init__(self, menu_game):
        start.__init__(self, menu_game)
        self.state = "Joingame"
        self.joingamex, self.joingamey = self.mid_w, self.mid_h + 30
        self.creategamex, self.creategamey = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.joingamex + self.offset, self.joingamey)
        image = pygame.image.load("StartImage.jpg")
        self.image = pygame.transform.scale(image, (self.Menu_Game.display.get_width(), self.Menu_Game.display.get_height()))


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.Menu_Game.check_events()
            self.check_input()
            self.Menu_Game.display.fill(self.Menu_Game.BLACK)
            self.Menu_Game.display.blit(self.image, (0, 0))
            self.Menu_Game.draw_text('JAJ Tanks', 40, self.Menu_Game.display.get_width() / 2, self.Menu_Game.display.get_height() / 2 - 60)
            self.Menu_Game.draw_text('Main Menu', 20, self.Menu_Game.display.get_width() / 2, self.Menu_Game.display.get_height() / 2 - 20)
            self.Menu_Game.draw_text("Joingame", 20, self.joingamex, self.joingamey)
            self.Menu_Game.draw_text("Creategame", 20, self.creategamex, self.creategamey)
            self.Menu_Game.draw_text('Credits & Info', 20, self.creditsx, self.creditsy)
            self.Menu_Game.close_button.draw()
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.Menu_Game.DOWN_KEY:
            if self.state == 'Joingame':
                self.cursor_rect.midtop = (self.creategamex + self.offset, self.creategamey)
                self.state = 'Creategame'
            elif self.state == 'Creategame':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits & Info'
            elif self.state == 'Credits & Info':
                self.cursor_rect.midtop = (self.joingamex + self.offset, self.joingamey)
                self.state = 'Joingame'
        elif self.Menu_Game.UP_KEY:
            if self.state == 'Joingame':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits & Info'
            elif self.state == 'Creategame':
                self.cursor_rect.midtop = (self.joingamex + self.offset, self.joingamey)
                self.state = 'Joingame'
            elif self.state == 'Credits & Info':
                self.cursor_rect.midtop = (self.creategamex + self.offset, self.creategamey)
                self.state = 'Creategame'


    def check_input(self):
        self.move_cursor()
        if self.Menu_Game.START_KEY:
            if self.state == 'Joingame':
                # self.Menu_Game.playing = True
                self.Menu_Game.curr_menu = self.Menu_Game.joingame
            elif self.state == 'Creategame':
                self.Menu_Game.curr_menu = self.Menu_Game.creategameMenu
            elif self.state == 'Credits & Info':
                self.Menu_Game.curr_menu = self.Menu_Game.credits_info
            self.run_display = False
