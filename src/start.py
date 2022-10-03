from menu_game import *

class start():
    def __init__(self, Menu_Game):
        self.Menu_Game = Menu_Game
        self.mid_w, self.mid_h = self.Menu_Game.screen.get_width() / 2, self.Menu_Game.screen.get_height() / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 110, 35)
        self.offset = - 100

    def draw_cursor(self):
        self.Menu_Game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)


    def blit_screen(self):
        self.Menu_Game.screen.blit(self.Menu_Game.display, (0, 0))
        pygame.display.update()
        self.Menu_Game.reset_keys()