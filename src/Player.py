from Tank import Tank
from Turret import Turret
from Shell import Shell
import math
import pygame
from Explosion import Explosion


class Player:
    """ A Player in the game.  For now, simply a filled circle. """

    def __init__(self, screen, who_am_i, sender, map):
        self.screen = screen
        self.player_number = who_am_i
        self.map = map
        self.score = 0
        self.x = 0
        self.y = 0
        self.tank_angle = 0
        self.turret_angle = self.tank_angle
        tank_images = ["Tank1.png", "Tank2.png", "Tank3.png", "Tank4.png"]
        turret_images = ["Turret1.png", "Turret2.png", "Turret3.png", "Turret4.png"]
        self.tank = Tank(self.screen, tank_images[self.player_number - 1], self.x, self.y, self.tank_angle)
        self.turret = Turret(self.screen, turret_images[self.player_number - 1], self.x, self.y, self.turret_angle)
        self.shells = []
        self.is_dead = False
        self.explosion_group = pygame.sprite.Group()
        self.score = 0
        self.shoot_sound = pygame.mixer.Sound("Pew.mp3")
        self.explosion_sound = pygame.mixer.Sound("Explosion.mp3")
        self.restrict_backward = False
        self.restrict_forward = False
        self.speed = 2

        self.sender = sender

    def set_position(self, x, y, tank_angle, turret_angle):
        self.x = x
        self.y = y
        self.tank_angle = tank_angle
        self.turret_angle = turret_angle
        self.tank.x = self.x
        self.tank.y = self.y
        self.tank.angle = self.tank_angle
        self.turret.angle = self.turret_angle
        self.turret.x = self.x
        self.turret.y = self.y

    def fire(self):
        x = self.x + 20 + (35 * math.cos(self.turret_angle))
        y = self.y + 25 - (35 * math.sin(self.turret_angle))
        self.shells.append(Shell(self.screen, x, y, - self.turret_angle, self.map))
        self.shoot_sound.play()

    def send_fire_message(self):
        self.sender.send_message("fire?{} {} {} {}".format(self.player_number, self.x, self.y, self.turret_angle))

    def send_state_message(self):
        self.sender.send_message(
            "state?{} {} {} {} {}".format(self.player_number, self.x, self.y,
                                             self.tank_angle, self.turret_angle))

    def turn_right(self):
        self.tank_angle -= (5 / 180) * self.speed
        if self.tank_angle <= -(math.pi):
            self.tank_angle = math.pi
        self.tank.angle = self.tank_angle

    def turn_left(self):
        self.tank_angle += (5 / 180) * self.speed
        if self.tank_angle >= math.pi:
            self.tank_angle = -(math.pi)
        self.tank.angle = self.tank_angle

    def forward(self):
        xchange = 0
        ychange = 0

        if self.restricted_movement()[0] == 0 and math.cos(self.tank_angle) > 0:
            self.x += math.cos(self.tank_angle) * self.speed
            xchange = math.cos(self.tank_angle) * self.speed
        if self.restricted_movement()[2] == 0 and math.cos(self.tank_angle) < 0:
            self.x += math.cos(self.tank_angle) * self.speed
            xchange = math.cos(self.tank_angle) * self.speed
        if self.restricted_movement()[3] == 0 and - math.sin(self.tank_angle) > 0:
            self.y += - math.sin(self.tank_angle) * self.speed
            ychange = - math.sin(self.tank_angle) * self.speed
        if self.restricted_movement()[1] == 0 and - math.sin(self.tank_angle) < 0:
            self.y += - math.sin(self.tank_angle) * self.speed
            ychange = - math.sin(self.tank_angle) * self.speed

        if self.check_point_collision() and 1 not in self.restricted_movement() and not self.restrict_backward:
            self.restrict_forward = True
            self.x -= xchange
            self.y -= ychange
        else:
            self.restrict_forward = False

        self.tank.x = self.x
        self.tank.y = self.y
        self.turret.x = self.x
        self.turret.y = self.y

    def check_point_collision(self):
        for point in self.map.end_points:
            if self.tank.is_hit("point", point):
                return True
        return False


    def backward(self):
        xchange = 0
        ychange = 0

        if self.restricted_movement()[0] == 0 and math.cos(self.tank_angle) < 0:
            self.x -= math.cos(self.tank_angle) * self.speed
            xchange = math.cos(self.tank_angle) * self.speed
        if self.restricted_movement()[2] == 0 and math.cos(self.tank_angle) > 0:
            self.x -= math.cos(self.tank_angle) * self.speed
            xchange = math.cos(self.tank_angle) * self.speed
        if self.restricted_movement()[3] == 0 and - math.sin(self.tank_angle) < 0:
            self.y -= - math.sin(self.tank_angle) * self.speed
            ychange = - math.sin(self.tank_angle) * self.speed
        if self.restricted_movement()[1] == 0 and - math.sin(self.tank_angle) > 0:
            self.y -= - math.sin(self.tank_angle) * self.speed
            ychange = - math.sin(self.tank_angle) * self.speed

        if self.check_point_collision() and 1 not in self.restricted_movement() and not self.restrict_forward:
            self.restrict_backward = True
            self.x += xchange
            self.y += ychange
        else:
            self.restrict_backward = False

        self.tank.x = self.x
        self.tank.y = self.y
        self.turret.x = self.x
        self.turret.y = self.y

    def point_turret(self, mouse_x, mouse_y):
        if (mouse_x - (self.x + 20)) != 0:
            tan_theta = (mouse_y - (self.y + 25)) / (mouse_x - (self.x + 20))
            self.turret_angle = - math.atan(tan_theta)
        elif (mouse_x - (self.x + 20)) == 0 and (mouse_y - (self.y + 25)) > 0:
            self.turret_angle = - math.pi / 2
        elif (mouse_x - (self.x + 20)) == 0 and (mouse_y - (self.y + 25)) < 0:
            self.turret_angle = math.pi / 2
        else:
            pass

        if (mouse_x - (self.x + 20)) < 0:
            self.turret_angle = math.pi + self.turret_angle
        self.turret.angle = self.turret_angle

    def fix_turret_pos(self, mouse_x, mouse_y):
        x = self.x + 20 + (35 * math.cos(self.turret_angle))
        y = self.y + 25 - (35 * math.sin(self.turret_angle))
        col, row = self.map.get_col_row(self.x + 20, self.y + 25)
        box = self.map.walls_listed[col][row]
        if box[0]:
            if x >= box[0].start[0] - 6:
                mouse_x = box[0].start[0] - 6
                if self.turret_angle > 0:
                    mouse_y = self.y + 25 - math.sqrt(35 ** 2 - ((mouse_x - (self.x + 20)) ** 2))
                else:
                    mouse_y = self.y + 25 + math.sqrt(35 ** 2 - ((mouse_x - (self.x + 20)) ** 2))
        if box[2]:
            if x <= box[2].start[0] + 6:
                mouse_x = box[2].start[0] + 6
                if self.turret_angle > 0 and self.turret_angle < math.pi:
                    mouse_y = self.y + 25 - math.sqrt(35 ** 2 - ((mouse_x - (self.x + 20)) ** 2))
                else:
                    mouse_y = self.y + 25 + math.sqrt(35 ** 2 - ((mouse_x - (self.x + 20)) ** 2))
        if box[3]:
            if y >= box[3].start[1] - 6:
                mouse_y = box[3].start[1] - 6
                if self.turret_angle > - math.pi / 2 and self.turret_angle < 0:
                    mouse_x = self.x + 20 + math.sqrt(35 ** 2 - ((mouse_y - (self.y + 25)) ** 2))
                else:
                    mouse_x = self.x + 20 - math.sqrt(35 ** 2 - ((mouse_y - (self.y + 25)) ** 2))
        if box[1]:
            if y <= box[1].start[1] + 6:
                mouse_y = box[1].start[1] + 6
                if self.turret_angle < math.pi / 2:
                    mouse_x = self.x + 20 + math.sqrt(35 ** 2 - ((mouse_y - (self.y + 25)) ** 2))
                else:
                    mouse_x = self.x + 20 - math.sqrt(35 ** 2 - ((mouse_y - (self.y + 25)) ** 2))
        self.point_turret(mouse_x, mouse_y)

    def restricted_movement(self):
        col, row = self.map.get_col_row(self.x + 20, self.y + 25)
        box = self.map.walls_listed[col][row]
        list = [0, 0, 0, 0]
        if box[0]:
            if self.x + 20 + (self.tank.size[0] / 2) + 6 >= box[0].start[0]:
                list[0] = 1
        if box[2]:
            if self.x + 20 - (self.tank.size[0] / 2) - 6 <= box[2].start[0]:
                list[2] = 1
        if box[3]:
            if self.y + 25 + (self.tank.size[1] / 2) + 6 >= box[3].start[1]:
                list[3] = 1
        if box[1]:
            if self.y + 25 - (self.tank.size[1] / 2) - 6 <= box[1].start[1]:
                list[1] = 1
        return list


    def explode(self):
        self.explosion_sound.play()
        self.is_dead = True
        self.explosion_group.add(Explosion(self.x + 20, self.y + 25))
