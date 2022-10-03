from start import start


class Credits_Info_Menu(start):
    def __init__(self, Menu_Game):
        start.__init__(self, Menu_Game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.Menu_Game.check_events()
            if self.Menu_Game.START_KEY or self.Menu_Game.BACK_KEY:
                self.Menu_Game.curr_menu = self.Menu_Game.main_menu
                self.run_display = False
            self.Menu_Game.display.fill(self.Menu_Game.BLACK)
            self.Menu_Game.draw_text('Credits & Info', 30, self.Menu_Game.screen.get_width() / 2, self.Menu_Game.screen.get_height() / 2 - 50)
            self.Menu_Game.draw_text('Credits: Josh Schrock, Anuj Suvarna, Junki Lee', 15, self.Menu_Game.screen.get_width() / 2, self.Menu_Game.screen.get_height() / 2 - 10)
            self.Menu_Game.draw_text('Info: This game is online tank game based on Tank Trouble.', 15, self.Menu_Game.screen.get_width() / 2, self.Menu_Game.screen.get_height() / 2 + 20)
            self.Menu_Game.draw_text('Intro Music: War by Hypnotic Brass Ensemble', 15, self.Menu_Game.screen.get_width() / 2,
                                     self.Menu_Game.screen.get_height() / 2 + 40)

            self.blit_screen()