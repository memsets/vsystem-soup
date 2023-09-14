#!/usr/bin/env python3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from enum import Enum

class State(Enum):
    RUNNING = True,
    KILLED = False


class Engine:
    def __init__(self):
        self.window_sz = (1200, 800)
        self.title = "Something modelling system 0.001v."
        
        self.entities = dict()
        self.scene = None

        self.my_font = None
        self.caret_font = None

    def mainloop(self):
        self.load_thirdparty()
        self.load_fonts()

        # loop
        while State.RUNNING:
            self.process_events()
            self.process_input()
 
            self.scene.fill((255, 50, 100))
 
            self.process_entities()
            
            pygame.display.flip()
            pygame.display.update()
        pygame.quit()

    def load_thirdparty(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.scene = pygame.display.set_mode(self.window_sz)
        
    def load_fonts(self):
        pygame.font.init()
        self.my_font = pygame.font.SysFont("Arial", 24)
        self.caret_font = pygame.font.SysFont("Arial", 24)
    
    def process_events(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                State.RUNNING = False
    
    def process_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]
                or keys[pygame.K_RETURN]
                or keys[pygame.K_KP_PERIOD]
                or keys[pygame.K_END]):
            State.RUNNING = False
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            print("Mouse clicked...")
            
    def process_entities(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        debug_position = self.my_font.render(f"distance: debug", False, (255, 255, 58))
        caret_position = self.caret_font.render(f"pos: {mouse_x} {mouse_y}", mouse_x, mouse_y)
        
        self.scene.blit(caret_position, (mouse_x + 30, mouse_y + 30))
        self.scene.blit(debug_position, (100, 100))
        pygame.draw.circle(self.scene, (0, 0, 0), (200, 200), 50)


    def add_entity(self, hash_name, value):
        self.entities[hash_name] = value
    
    def delete_entity(self, hash_name):
        del self.entities[hash_name]


class App:
    def __init__(self):
        print("Starting application...")

    def start(self):
        eng = Engine()
        eng.mainloop()    


def main():
    application = App()
    application.start()
    
if __name__ == '__main__':
    main()
