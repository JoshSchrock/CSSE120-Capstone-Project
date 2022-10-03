from Game import Game
from View import View
from menu_game import *


# DONE: Put your names here (entire team)
# Josh Schrock, Junki Lee, Anuj Suvarna


def main():
    pygame.init()
    players = []
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # DONE: Choose your own size
    clock = pygame.time.Clock()

    frame_rate = 30 # DONE: Choose your own frame rate

    g = Menu_Game(screen)
    game = None
    viewer = None
    set_up = False

    while True:
        clock.tick(frame_rate)
        if g.running:
            g.curr_menu.display_menu()
        if g.playing:
            if not set_up:
                for i in range(g.number_of_players):
                    players.append(i + 1)
                who_am_i = g.player_number
                game_code = g.game_code
                game = Game(screen, who_am_i, players, game_code, g)  # the Model
                viewer = View(screen, game)  # the View
                set_up = True
            game.run_one_cycle()
            if not g.running:
                viewer.draw_everything()


if __name__ == '__main__':
    main()  # On one computer, use 1.  On the other computer, use 2.
