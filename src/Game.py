import pygame
from Player import Player
from Map import Map
from External_Controller import ExternalController
import simpleMQTT as mq
from Game_Controller import GameController
from Scoreboard import Scoreboard
from Button import Button
import time
# Put each class in its own module, using the same name for both.
# Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
#     from Missiles import Missiles
#     from Enemies import Enemies

# Done: Anuj Suvarna, Josh Schrock, Junki Lee
# Josh Schrock, Junki Lee, Anuj Suvarna


class Game:
    def __init__(self, screen: pygame.Surface, who_am_i, players, game_code, menu):
        self.screen = screen
        self.who_am_i = who_am_i
        self.menu = menu
        # Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        #     self.enemies = Enemies(self.screen)

        self.map = Map(self.screen)
        self.scoreboard = Scoreboard(self.screen, list)

        if self.who_am_i == 1:
            self.map.generate_seed()
            self.map.generate_map(self.map.seed)

        self.connected_computers = [self.who_am_i]
        unique_id = "csse120-Epic-Tanks-JAJ-" + game_code
        self.sender = mq.Sender(who_am_i, len(players), verbosity=0)
        self.receiver = mq.Receiver(ExternalController(self), verbosity=0)
        mq.activate(unique_id, self.sender, self.receiver)

        self.players = []

        for i in range(len(players)):
            self.players.append(Player(self.screen, players[i], self.sender, self.map))

        self.controller = GameController(self, self.players[self.who_am_i - 1])  # the internal Controller

        self.gotten_start = False
        self.gotten_last = False
        self.time_of_win = None
        self.got_connection = False

        # Sound Bullet
        self.whoosh_sound = pygame.mixer.Sound("Whoosh.mp3")
        self.ticker_sound = pygame.mixer.Sound("Ching.mp3")

        if who_am_i == 1:
            self.sender.send_message("map?" + self.map.seed)
            self.set_start_positions()


        # Game Help Objects
        self.scoreboard = Scoreboard(self.screen, self.players)
        self.close_button = Button(self.screen, pygame.Color("red"), self.screen.get_width() - 100, 50, 50, 50, "X", font='comicsans', size=50)

    def set_start_positions(self):
        self.gotten_start = True
        for player in self.players:
            player.set_position(float(self.map.start_positions[self.who_am_i - 1][0]),
                                float(self.map.start_positions[self.who_am_i - 1][1]),
                                float(self.map.start_positions[self.who_am_i - 1][2]),
                                float(self.map.start_positions[self.who_am_i - 1][2]))
        self.ticker_sound.play()

    def get_connection(self):
        all_connected = True
        for i in range(len(self.players)):
            if i + 1 not in self.connected_computers:
                all_connected = False
        if not all_connected:
            self.sender.send_message("connection?" + str(self.who_am_i))
        else:
            self.got_connection = True
            self.menu.running = False
            pygame.mixer.music.pause()

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # Use something like the following, but for the objects in YOUR game:
        #     self.fighter.draw()
        #     self.missiles.draw()
        #     self.enemies.draw()
        self.map.draw()
        self.scoreboard.draw()
        for player in self.players:
            if not player.is_dead:
                player.tank.draw()
                player.turret.draw()
            player.explosion_group.draw(self.screen)
            player.explosion_group.update()
            for shell in player.shells:
                shell.draw()
        self.close_button.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # Use something like the following, but for the objects in YOUR game:
        #     self.missiles.move()
        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)
        if not self.got_connection:
            self.get_connection()
        self.controller.get_and_handle_events()
        self.players[self.who_am_i - 1].send_state_message()

        if not self.gotten_start:
            self.sender.send_message("maprequest? ")

        for player in self.players:
            delete_shells = []
            for s in range(len(player.shells)):
                player.shells[s].move()
                if player.shells[s].outside_of_map():
                    delete_shells.append(s)
            for x in range(len(delete_shells) - 1, - 1, - 1):
                player.shells.pop(delete_shells[x])
                self.whoosh_sound.play()

        for player in self.players:
            delete_shells = []
            for i in range(len(player.shells)):
                player.shells[i].bounce()
                if player.shells[i].time_alive() >= 15:
                    delete_shells.append(i)
                if self.players[self.who_am_i - 1].tank.is_hit("shell", player.shells[i]) and not self.players[self.who_am_i - 1].is_dead:
                    self.sender.send_message("death?{} {}".format(self.players[self.who_am_i - 1].player_number, player.player_number))
                    self.players[self.who_am_i - 1].score -= 1
                    player.score += 1
                    self.players[self.who_am_i - 1].explode()


            for x in range(len(delete_shells) - 1, - 1, - 1):
                player.shells.pop(delete_shells[x])
                self.whoosh_sound.play()

        # stuff for new game
        if not self.gotten_last:
            count_left = 0
            for player in self.players:
                if not player.is_dead:
                    count_left += 1
            if count_left <= 1:
                self.gotten_last = True
                self.time_of_win = time.time()

        if self.gotten_last:
            if time.time() - self.time_of_win >= 5:
                for player in self.players:
                    player.is_dead = False
                    player.shells = []
                self.gotten_last = False
                self.time_of_win = None
                if self.who_am_i == 1:
                    self.map.generate_seed()
                    self.map.generate_map(self.map.seed)
                    self.sender.send_message("map?" + self.map.seed)
                    self.set_start_positions()
