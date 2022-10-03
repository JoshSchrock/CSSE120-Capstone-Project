import pygame
import sys
from joingame import joingame
from mainMenu import MainMenu
from creategameMenu import CreateGameMenu
from credits_info import Credits_Info_Menu
from WaitingScreen import WaitingScreen
from Button import Button
from PlayerSelector import PlayerSelector

#다른 게임 파일
class Menu_Game():
    def __init__(self, screen):
        self.running, self.playing = True, False
        self.SPACE, self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False
        self.screen = screen
        self.display = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.font_name = 'font.ttf'
        # self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.joingame = joingame(self)
        self.creategameMenu = CreateGameMenu(self)
        self.credits_info = Credits_Info_Menu(self)
        self.waiting_screen = WaitingScreen(self)
        self.player_selector = PlayerSelector(self)
        self.curr_menu = self.main_menu
        pygame.mixer.music.load("Epic Tanks JAJ.mp3")
        pygame.mixer.music.play()
        self.close_button = Button(self.display, pygame.Color("red"), self.display.get_width() - 100,
                                   50, 50, 50, "X",
                                   font='comicsans', size=50)
        self.game_code = None
        self.player_number = 1
        self.number_of_players = 2


    def check_events(self):
        mousex, mousey = pygame.mouse.get_pos()
        if self.close_button.isOver((mousex, mousey)):
            self.close_button.outline = 20
        else:
            self.close_button.outline = 0

        for event in pygame.event.get():
            if not self.game_code:
                self.game_code = self.joingame.inputBox.handle_event(event)
                if self.game_code:
                    self.curr_menu = self.player_selector
                    self.joingame.run_display = False
                    self.number_of_players = int(self.game_code[0])
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

            if event.type == pygame.MOUSEBUTTONUP:
                if self.close_button.isOver((mousex, mousey)):
                    sys.exit()


    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False


    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
