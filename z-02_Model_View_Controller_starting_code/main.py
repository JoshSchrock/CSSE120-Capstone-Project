import pygame
from Game import Game
from Game_Controller import GameController
from External_Controller import ExternalController
from View import View
import simpleMQTT as mq

# DONE: Put your names here (entire team)
# Josh Schrock, Junki Lee, Anuj Suvarna


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # TODO: Choose your own size
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = GameController(game)  # the Controller

    unique_id = "csse120-david-mutchler"
    sender = mq.Sender(who_am_i)
    controller = ExternalController(zombie)
    receiver = mq.Receiver(controller)
    mq.activate(unique_id, sender, receiver)

    frame_rate = 60  # TODO: Choose your own frame rate

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()


main()
