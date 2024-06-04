import pygame
from pygame.locals import *
from GameBoard import GameBoard
from Store import Store
import sys

class Game:
    def __init__(self):
        # initialize the game engine
        pygame.init()

        self.x = 800
        self.y = 800

        # sets the initial map
        self.board = GameBoard(self.x, self.y)

        # initialize the grid
        self.grid = [[False for _ in range(self.x // 20)] for _ in range(self.y // 20)]

        # initialize store
        self.store = Store(5, 30)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            # draw board
            self.board.draw()
            
            # initialize boxes
            self.store.start_boxes()

            self.clock.tick(15)
            pygame.display.update()
            
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()