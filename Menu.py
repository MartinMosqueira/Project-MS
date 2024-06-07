import pygame
from pygame.locals import *
from InputBox import InputBox

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def run(self):
        small_font = pygame.font.Font(None, 36)

        input_boxes = InputBox(350, 300, 140, 32)
        input_time = InputBox(350, 400, 140, 32)

        start_button = pygame.Rect(350, 500, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')

        input_boxes_text = small_font.render('Boxes:', True, (255, 255, 255))
        input_time_text = small_font.render('Time simulation:', True, (255, 255, 255))
        button_text = small_font.render('Start', True, (255, 255, 255))

        input_boxes.active = False
        input_time.active = False

        while True:
            self.screen.fill((8, 4, 36))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return None, None
                input_boxes.handle_event(event)
                input_time.handle_event(event)

                if event.type == MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        # start the simulation
                        try:
                            num_boxes = int(input_boxes.text)
                            sim_time = int(input_time.text)
                            return num_boxes, sim_time
                        except ValueError:
                            pass

            input_boxes.update()
            input_time.update()

            self.screen.blit(input_boxes_text, (100, 300))
            self.screen.blit(input_time_text, (100, 400))
            pygame.draw.rect(self.screen, color_active if start_button.collidepoint(pygame.mouse.get_pos()) else color_inactive, start_button)
            self.screen.blit(button_text, (start_button.x + 10, start_button.y + 5))

            input_boxes.draw(self.screen)
            input_time.draw(self.screen)

            pygame.display.flip()
            pygame.time.Clock().tick(30)
