import pygame.font


class Scoreboard:

    def __init__(self, screen, list):
        self.list = list
        self.screen = screen
        self.font = pygame.font.Font(None, 35)

    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), (0, 0, 200, 100))
        pygame.draw.rect(self.screen, (255, 165, 0), ((self.screen.get_width() / 4), 0, 200, 100))
        pygame.draw.rect(self.screen, (0, 100, 255), (self.screen.get_width() / 2, 0, 200, 100))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.screen.get_width() - 390, 0, 200, 100))
        for i in range(len(self.list)):
            score_string = "Player " + str(i + 1) + ": " + str(self.list[i].score)
            score_image = self.font.render(score_string, True, (0, 0, 0))
            self.screen.blit(score_image, (((self.screen.get_width() / 4) * i) + 30, 30))


