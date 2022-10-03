import math

import pygame.image


class Turret:
    def __init__(self, screen, image, x, y, turret_angle):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.image = pygame.transform.rotate(self.image, -90)
        self.x = x
        self.y = y
        self.angle = turret_angle

    def draw(self):
        # self.screen.blit()
        img = pygame.transform.rotate(self.image, math.degrees(self.angle))
        rect = img.get_rect(center=(20 + self.x + (13 * math.cos(self.angle)), 25 + self.y - (13 * math.sin(self.angle))))
        self.screen.blit(img, rect)


