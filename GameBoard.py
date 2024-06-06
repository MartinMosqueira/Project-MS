import pygame
import random


class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.icon = pygame.image.load("img/money.png")
        self.screen = pygame.display.set_mode((width, height))

        # title and icon
        pygame.display.set_caption("Tron")
        pygame.display.set_icon(self.icon)

        # colors
        self.boxColor = (0, 255, 0)
        self.clientColor = self.generate_random_color()
        self.lineColor = (0, 0, 0)
        self.backgroundColor = (8, 4, 36)

    def generate_random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

    def draw_box(self, x, y):
        pygame.draw.rect(self.screen, self.boxColor, pygame.Rect(x, y, 50, 50))

    def draw_client(self, x, y):
        pygame.draw.circle(self.screen, self.clientColor, (x, y), 10)

    def draw(self):
        self.screen.fill(self.backgroundColor)
        for i in range(0, self.width, 20):
            pygame.draw.line(self.screen, self.lineColor, [i, 0], [i, self.width], 1)
            pygame.draw.line(self.screen, self.lineColor, [0, i], [self.height, i], 1)