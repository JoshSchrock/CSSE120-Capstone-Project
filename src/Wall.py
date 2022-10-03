import pygame

class Wall:
    def __init__(self, screen, start, end, position):
        self.screen = screen
        self.start = start
        self.end = end
        self.position = position
        self.width = 4

    def draw(self):
        pygame.draw.line(self.screen, pygame.Color("Grey"), self.start, self.end, self.width)
