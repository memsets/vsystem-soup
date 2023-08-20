#!/usr/bin/env python3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys


class App:
    IS_RUNNING = True

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Something modelling system 0.001v.")

        self.scene = pygame.display.set_mode((1200, 800))

        pygame.font.init()
        self.my_font = pygame.font.SysFont("Arial", 18)
        self.caret_font = pygame.font.SysFont("Arial", 18)
        self.basic_loop()

    def basic_loop(self):
        while App.IS_RUNNING:
            self.basic_event_loop()
            self.input_handler()

            self.scene.fill((255, 50, 100))
            
            debug_position = self.my_font.render(f"distance: debug", False, (255, 255, 58))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            caret_position = self.caret_font.render(f"pos: {mouse_x} {mouse_y}", mouse_x, mouse_y)
            
            self.scene.blit(caret_position, (mouse_x + 30, mouse_y + 30))
            self.scene.blit(debug_position, (100, 100))
            
            
            # Draw logic
            
            # Draw shapes 

            pygame.display.flip()
            pygame.display.update()

    def basic_event_loop(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                App.IS_RUNNING = False

    def input_handler(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]
                or keys[pygame.K_RETURN]
                or keys[pygame.K_KP_PERIOD]
                or keys[pygame.K_END]):
            App.IS_RUNNING = False
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            print("Mouse clicked...")

def main():
    print(sys.platform)
    hello = App()
    pygame.quit()
    
if __name__ == '__main__':
    main()
