import pygame
import sys
from Player import Player

# TODO: Put your names here (entire team)


class GameController:
    def __init__(self, game, player: Player):
        self.game = game
        self.player = player

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        mousex, mousey = pygame.mouse.get_pos()
        if self.game.close_button.isOver((mousex, mousey)):
            self.game.close_button.outline = 20
        else:
            self.game.close_button.outline = 0

        if self.game.gotten_start:
            if not self.player.is_dead:
                self.player.point_turret(mousex, mousey)
                self.player.fix_turret_pos(mousex, mousey)

                pressed_keys = pygame.key.get_pressed()

                if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_w]:
                    self.player.turn_left()
                    self.player.forward()
                elif pressed_keys[pygame.K_d] and pressed_keys[pygame.K_w]:
                    self.player.turn_right()
                    self.player.forward()
                elif pressed_keys[pygame.K_a] and pressed_keys[pygame.K_s]:
                    self.player.turn_right()
                    self.player.backward()
                elif pressed_keys[pygame.K_d] and pressed_keys[pygame.K_s]:
                    self.player.turn_left()
                    self.player.backward()
                elif pressed_keys[pygame.K_a]:
                    self.player.turn_left()
                elif pressed_keys[pygame.K_d]:
                    self.player.turn_right()
                elif pressed_keys[pygame.K_w]:
                    self.player.forward()
                elif pressed_keys[pygame.K_s]:
                    self.player.backward()

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.game.gotten_start:
                    if mousex > self.game.map.left_x and mousex < self.game.map.left_x + self.game.map.width \
                        and mousey > self.game.map.top_y and mousey < self.game.map.top_y + self.game.map.height:
                        if not self.player.is_dead and len(self.player.shells) < 6:
                            self.player.send_fire_message()
                            self.player.fire()
                if self.game.close_button.isOver((mousex, mousey)):
                    sys.exit()


    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
