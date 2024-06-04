import pygame
from pygame.locals import *
from GameBoard import GameBoard
from Store import Store
from Client import Client
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

        # initialize boxes
        self.store.start_boxes()

        # initialize time boxes
        self.store.start_time_boxes()

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            # draw board
            self.board.draw()

            # client arrival simulation
            if self.store.start_client():
                print("Client arrived")
                newClient = Client()

                # assign client to a box or row
                for i in range(0, self.store.numberBoxes):
                    if len(self.store.boxes[i+1]) == 0:
                        self.store.boxes[i+1].append(newClient)
                        print("Client assigned to box", i+1)
                        break
                else:
                    self.store.row.append(newClient)
                    print("Client assigned to row")
                    
            
            # check if a client arrives
            if len(self.store.row) > 0:
                for i in range(0, self.store.numberBoxes):
                    if len(self.store.boxes[i+1]) == 0:
                        self.store.boxes[i+1].append(self.store.row.pop(0))
                        print("Client assigned to box", i+1)
                        break
            
            # attention time simulation
            for i in range(0, self.store.numberBoxes):
                if len(self.store.boxes[i+1]) > 0:
                    if self.store.timeBoxes[i+1] == None:
                        self.store.timeBoxes[i+1] = self.store.attention_time_box()
                        print("Attention time box", i+1, ":", self.store.timeBoxes[i+1])
                    
                    elif self.store.timeBoxes[i+1] < 0:
                        self.store.boxes[i+1].pop(0)
                        self.store.timeBoxes[i+1] = None
                        print("Client finished in box", i+1)

                    else:
                        self.store.timeBoxes[i+1] -= 1
                        print("Attention time box", i+1, ":", self.store.timeBoxes[i+1])
                        
                
            self.clock.tick(15)
            pygame.display.update()
            
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()