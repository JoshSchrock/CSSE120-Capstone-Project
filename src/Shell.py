import pygame
import math
import time

class Shell:
    def __init__(self, screen, x, y, angle, mapp):
        self.screen = screen
        self.map = mapp
        self.x = x
        self.y = y
        self.radius = 2
        self.color = pygame.Color("BLACK")
        self.speed_x = math.cos(angle) * 3
        self.speed_y = math.sin(angle) * 3
        self.has_exploded = False
        self.start_time = time.time()
        self.bounce_sound = pygame.mixer.Sound("Dong.mp3")

    def time_alive(self):
        return time.time() - self.start_time

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def bounce(self):
        col, row = self.map.get_col_row(self.x, self.y)
        box = self.map.walls_listed[col][row]
        if box[0]:
            if self.x + self.radius >= box[0].start[0] - (box[0].width / 2):
                self.speed_x = -self.speed_x
                self.bounce_sound.play()
        if box[2]:
            if self.x - self.radius <= box[2].start[0] + (box[2].width / 2):
                self.speed_x = -self.speed_x
                self.bounce_sound.play()
        if box[3]:
            if self.y + self.radius >= box[3].start[1] - (box[3].width / 2):
                self.speed_y = -self.speed_y
                self.bounce_sound.play()
        if box[1]:
            if self.y - self.radius <= box[1].start[1] + (box[1].width / 2):
                self.speed_y = -self.speed_y
                self.bounce_sound.play()

        for wall in self.map.walls:
            if self.x <= wall.start[0] + 2 and self.x >= wall.start[0] - 2 and self.y <= wall.start[1] + 2 and self.y >= wall.start[1] - 2:
                self.speed_y = -self.speed_y
                self.speed_x = -self.speed_x
                self.bounce_sound.play()

    def outside_of_map(self):
        if self.x < self.map.left_x or self.x > self.map.left_x + self.map.width \
                or self.y < self.map.top_y or self.y > self.map.top_y + self.map.height:
            return True





