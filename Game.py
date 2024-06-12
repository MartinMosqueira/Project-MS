import pygame
from pygame.locals import *
from GameBoard import GameBoard
from Store import Store
from Client import Client
from Menu import Menu
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

        # cost variables
        self.costBoxes = 0
        self.lost = 0
        self.earn = 0
        
        # clients variables
        self.initClients = 0
        self.servedClients = 0
        self.unservedClients = 0

        # initialize time
        self.sim_time = 12*3600 # 12pm
        self.time = 8*3600 # 8am

        self.clock = pygame.time.Clock()
        self.running = True
    
    def show_menu(self):
        menu = Menu(self.x, self.y)
        num_boxes = menu.run()

        if num_boxes is not None and num_boxes <= 10:
            self.store = Store(num_boxes)
            
            # initialize boxes
            self.store.start_boxes()

            # initialize time boxes
            self.store.start_time_boxes()

            # calculate cost boxes
            self.costBoxes = self.store.cost_boxes()
        else:
            pygame.quit()
            sys.exit()

    def run(self):
        self.show_menu()

        while self.running:
            
            if self.time >= self.sim_time:
                self.running = False
                continue

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            # draw board
            self.board.draw()

            # draw boxes
            for i in range(1, self.store.numberBoxes + 1):
                self.board.draw_box(50 + (i * 100), 100)
            
            # draw clients
            for i, clients in self.store.boxes.items():
                for j, client in enumerate(clients):
                    self.board.draw_client(50 + (i * 100), 100 + ((j + 1) * 50),client)

            # draw clients in row
            for i, client in enumerate(self.store.row):
                self.board.draw_client(50, 100 + ((i + 1) * 50),client)

            # client arrival simulation
            if self.store.start_client(self.time):
                #print("Client arrived")
                newClient = Client()
                self.initClients += 1

                # assign client to a box or row
                for i in range(0, self.store.numberBoxes):
                    if len(self.store.boxes[i+1]) == 0:
                        self.store.boxes[i+1].append(newClient)
                        #print("Client assigned to box", i+1)
                        self.servedClients += 1
                        break
                else:
                    self.store.row.append(newClient)
                    #print("Client assigned to row")

                    self.store.timeRow.append(newClient.timeSeconds)
                    
            
            # check if a client arrives
            if len(self.store.row) > 0:
                for i in range(0, self.store.numberBoxes):
                    if len(self.store.boxes[i+1]) == 0:
                        if self.store.row:
                            self.store.boxes[i+1].append(self.store.row.pop(0))
                            #print("Client assigned to box", i+1)
                            self.servedClients += 1
                            self.store.timeRowLimits.append(self.store.timeRow.pop(0))
                
                for time in range(0, len(self.store.timeRow)-1):
                    self.store.timeRow[time] -= 1
                    if self.store.timeRow[time] < 0:
                        self.store.row.pop(0)
                        self.store.timeRow.pop(0)
                        self.lost += Client().costClient
                        self.unservedClients += 1
                        #print("Client finished in row!!")
                
            
            # attention time simulation
            for i in range(0, self.store.numberBoxes):
                if len(self.store.boxes[i+1]) > 0:
                    if self.store.timeBoxes[i+1] == None:
                        self.store.timeBoxes[i+1] = self.store.attention_time_box()
                        self.store.max_attention_time_box(self.store.timeBoxes[i+1])
                        self.store.min_attention_time_box(self.store.timeBoxes[i+1])
                        #print("Attention time box", i+1, ":", self.store.timeBoxes[i+1])
                    
                    elif self.store.timeBoxes[i+1] < 0:
                        self.store.boxes[i+1].pop(0)
                        self.store.timeBoxes[i+1] = None
                        self.earn += Client().costClient
                        #print("Client finished in box", i+1)

                    else:
                        self.store.timeBoxes[i+1] -= 1
                        #print("Attention time box", i+1, ":", self.store.timeBoxes[i+1])
                        
            pygame.display.update()

            self.clock.tick(48)
            self.time += 1
            
        pygame.quit()
        #sys.exit()
    
    def print_results(self):
        print("Clientes totales: ", self.initClients)
        print("Clientes atendidos: ", self.servedClients)
        print("Clientes no atendidos: ", self.unservedClients)
        print("Tiempo minimo de atencion: ", self.store.min_time)
        print("Tiempo maximo de atencion: ", self.store.max_time)
        print("Tiempo minimo en fila: ", self.store.min_time_row())
        print("Tiempo maximo en fila: ", self.store.max_time_row())
        print("Costo de operacion: ", self.store.cost_boxes()+self.lost)
        print("Costo: ", self.costBoxes)
        print("Perdida: ", self.lost)
        print("Ganancia: ", self.earn)

if __name__ == "__main__":
    game = Game()
    game.run()
    game.print_results()
