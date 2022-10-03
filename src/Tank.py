import pygame
import math


class Tank:
    def __init__(self, screen, image, x, y, angle):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.rotate(self.image, -90)
        self.angle = angle
        self.size = self.image.get_size()
        self.hit_box = self.image.get_rect(center=(20 + self.x, 25 + self.y))

    def draw(self):
        img = pygame.transform.rotate(self.image, math.degrees(self.angle))
        self.size = self.image.get_size()
        self.hit_box = img.get_rect(center=(20 + self.x, 25 + self.y))
        self.screen.blit(img, self.hit_box)


        # TESTNG CODE BELOW
        # pygame.draw.circle(self.screen, pygame.Color("blue"), (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi/2))),
        #           (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi/2))))), 10)
        # pygame.draw.circle(self.screen, pygame.Color("red"),
        #                    (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2))),
        #                     (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))), 10)
        # pygame.draw.circle(self.screen, pygame.Color("green"),
        #                    (self.hit_box.center[0] - (25 * math.cos(-self.angle)),
        #                     (self.hit_box.center[1] - (25 * math.sin(-self.angle)))), 10)
        # pygame.draw.circle(self.screen, pygame.Color("yellow"),
        #                    (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi)),
        #                     (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))), 10)


        # for x in range(int(self.screen.get_width()) // 4):
        #     for y in range(int(self.screen.get_height()) // 4):
        #         if self.angle == math.pi or self.angle == -math.pi or self.angle == 0:
        #             if x > self.hit_box.center[0] - 25 and x < self.hit_box.center[0] + 25 \
        #                     and y > self.hit_box.center[1] - 20 and y < self.hit_box.center[1] + 20:
        #                 pygame.draw.circle(self.screen, pygame.Color("blue"), (x, y), 2)
        #         elif self.angle == math.pi / 2 or self.angle == -math.pi / 2:
        #             if x > self.hit_box.center[0] - 20 and x < self.hit_box.center[0] + 20 \
        #                     and y > self.hit_box.center[1] - 25 and y < self.hit_box.center[1] + 25:
        #                 pygame.draw.circle(self.screen, pygame.Color("blue"), (x, y), 2)
        #         elif self.angle < math.pi / 2 and self.angle > 0:
        #             if round(y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi/2))))) <= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi/2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) >= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) <= round((math.cos(self.angle) / math.sin(self.angle)) * (x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) >= round((math.cos(self.angle) / math.sin(self.angle)) * (x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
        #                 pygame.draw.circle(self.screen, pygame.Color("blue"), (x, y), 2)
        #         elif self.angle < 0 and self.angle > -math.pi/2:
        #             if round(y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi/2))))) <= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi/2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) >= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) >= round((math.cos(self.angle) / math.sin(self.angle)) * (x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) <= round((math.cos(self.angle) / math.sin(self.angle)) * (x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
        #                 pygame.draw.circle(self.screen, pygame.Color("blue"), (x, y), 2)
        #         elif self.angle > math.pi/2:
        #             if round(y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi/2))))) >= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi/2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) <= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) <= round((math.cos(self.angle) / math.sin(self.angle)) * (x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) >= round((math.cos(self.angle) / math.sin(self.angle)) * (x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
        #                 pygame.draw.circle(self.screen, pygame.Color("blue"), (x, y), 2)
        #         else:
        #             if round(y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi/2))))) >= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi/2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) <= round((-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) >= round((math.cos(self.angle) / math.sin(self.angle)) * (x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
        #                     and round(y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) <= round((math.cos(self.angle) / math.sin(self.angle)) * (x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
        #                 pygame.draw.circle(self.screen, pygame.Color("blue"), (x, y), 2)

    def is_hit(self, type, shell):
        if type == "shell":
            x = shell.x
            y = shell.y
        else:
            x = shell[0]
            y = shell[1]
        if self.angle == math.pi or self.angle == -math.pi or self.angle == 0:
            if x > self.hit_box.center[0] - 25 and x < self.hit_box.center[0] + 25 \
                    and y > self.hit_box.center[1] - 20 and y < self.hit_box.center[1] + 20:
                return True
        elif self.angle == math.pi / 2 or self.angle == -math.pi / 2:
            if x > self.hit_box.center[0] - 20 and x < self.hit_box.center[0] + 20 \
                    and y > self.hit_box.center[1] - 25 and y < self.hit_box.center[1] + 25:
                return True
        elif self.angle < math.pi / 2 and self.angle > 0:
            if (y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi / 2))))) <= (
                    (-math.tan(self.angle)) * (
                            x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) >= (
                (-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) <= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) >= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
                return True
        elif self.angle < 0 and self.angle > -math.pi / 2:
            if (y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi / 2))))) <= (
                    (-math.tan(self.angle)) * (
                            x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) >= (
                (-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) >= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) <= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
                return True
        elif self.angle > math.pi / 2:
            if (y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi / 2))))) >= (
                    (-math.tan(self.angle)) * (
                            x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) <= (
                (-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) <= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) >= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
                return True
        else:
            if (y - (self.hit_box.center[1] + (20 * math.sin(-self.angle + (math.pi / 2))))) >= (
                    (-math.tan(self.angle)) * (
                            x - (self.hit_box.center[0] + (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (20 * math.sin(-self.angle + (math.pi / 2))))) <= (
                (-math.tan(self.angle)) * (x - (self.hit_box.center[0] - (20 * math.cos(-self.angle + (math.pi / 2)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle)))) >= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - ((self.hit_box.center[0] - (25 * math.cos(-self.angle)))))) \
                    and (y - (self.hit_box.center[1] - (25 * math.sin(-self.angle + math.pi)))) <= (
                (math.cos(self.angle) / math.sin(self.angle)) * (
                        x - (self.hit_box.center[0] - (25 * math.cos(-self.angle + math.pi))))):
                return True

        return False