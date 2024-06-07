import pygame


class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # load images
        self.icon = pygame.image.load("img/money.png")
        self.screen = pygame.display.set_mode((width, height))

        self.box_image = pygame.image.load("img/cash.png")
        self.box_image = pygame.transform.scale(self.box_image, (100, 100))

        # title and icon
        pygame.display.set_caption("Simulation")
        pygame.display.set_icon(self.icon)

        # colors
        self.lineColor = (0, 0, 0)
        self.backgroundColor = (8, 4, 36)

    def draw_box(self, x, y):
        self.screen.blit(self.box_image, (x, y))

    def draw_client(self, x, y, client):
        pygame.draw.circle(self.screen, client.color, (x, y), 10)

    def draw(self):
        self.screen.fill(self.backgroundColor)
        for i in range(0, self.width, 20):
            pygame.draw.line(self.screen, self.lineColor, [i, 0], [i, self.width], 1)
            pygame.draw.line(self.screen, self.lineColor, [0, i], [self.height, i], 1)
            