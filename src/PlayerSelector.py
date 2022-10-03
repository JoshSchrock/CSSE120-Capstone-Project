import pygame
from start import start

class PlayerSelector(start):
    def __init__(self, Menu_Game):
        start.__init__(self, Menu_Game)
        self.state = 'Player 2'
        self.twoplayerx, self.twoplayery = self.mid_w, self.mid_h + 30
        self.threeplayerx, self.threeplayery = self.mid_w, self.mid_h + 60
        self.fourplayerx, self.fourplayery = self.mid_w, self.mid_h + 90
        self.instructionx, self.instructiony = self.mid_w, self.mid_h
        image = pygame.image.load("StartImage.jpg")
        self.image = pygame.transform.scale(image,
                                            (self.Menu_Game.display.get_width(), self.Menu_Game.display.get_height()))

        self.cursor_rect.midtop = (self.twoplayerx + self.offset, self.twoplayery)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.Menu_Game.check_events()
            self.check_input()
            self.check_how_many_players()
            self.Menu_Game.display.fill((0, 0, 0))
            self.Menu_Game.display.blit(self.image, (0, 0))
            self.Menu_Game.draw_text('Choose a UNIQUE player', 30, self.Menu_Game.screen.get_width() / 2, self.Menu_Game.screen.get_height() / 2 - 30)
            self.Menu_Game.draw_text("Player 2", 20, self.twoplayerx, self.twoplayery)
            self.Menu_Game.draw_text("Player 3", 20, self.threeplayerx, self.threeplayery)
            self.Menu_Game.draw_text("Player 4", 20, self.fourplayerx, self.fourplayery)
            self.draw_cursor()
            self.Menu_Game.close_button.draw()
            self.blit_screen()

    def check_input(self):
        if self.Menu_Game.BACK_KEY:
            self.Menu_Game.curr_menu = self.Menu_Game.main_menu
            self.run_display = False

        if self.Menu_Game.DOWN_KEY:
            if self.state == 'Player 2':
                self.cursor_rect.midtop = (self.threeplayerx + self.offset, self.threeplayery)
                self.state = 'Player 3'
            elif self.state == 'Player 3':
                self.cursor_rect.midtop = (self.fourplayerx + self.offset, self.fourplayery)
                self.state = 'Player 4'
            elif self.state == 'Player 4':
                self.cursor_rect.midtop = (self.twoplayerx + self.offset, self.twoplayery)
                self.state = 'Player 2'
        elif self.Menu_Game.UP_KEY:
            if self.state == 'Player 2':
                self.cursor_rect.midtop = (self.fourplayerx + self.offset, self.fourplayery)
                self.state = 'Player 4'
            elif self.state == 'Player 3':
                self.cursor_rect.midtop = (self.twoplayerx + self.offset, self.twoplayery)
                self.state = 'Player 2'
            elif self.state == 'Player 4':
                self.cursor_rect.midtop = (self.threeplayerx + self.offset, self.threeplayery)
                self.state = 'Player 3'

    def check_how_many_players(self):
        if self.Menu_Game.START_KEY:
            if self.state == 'Player 2':
                self.Menu_Game.player_number = 2
            elif self.state == 'Player 3':
                self.Menu_Game.player_number = 3
            elif self.state == 'Player 4':
                self.Menu_Game.player_number = 4
            self.Menu_Game.curr_menu = self.Menu_Game.waiting_screen
            self.run_display = False
            self.Menu_Game.playing = True
