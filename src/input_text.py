import pygame

COLOR_INACTIVE = pygame.Color('white')
COLOR_ACTIVE = pygame.Color('yellow')

pygame.init()
class input_text():
    def __init__(self, x, y, width, height, max, text = ''):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = COLOR_INACTIVE
        self.max = max
        self.text = text
        self.font = pygame.font.SysFont('consolas', 120)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    output = self.text
                    self.text = ''
                    self.txt_surface = self.font.render(self.text, True, self.color)
                    return output
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < self.max:
                        self.text += event.unicode.upper()

                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


