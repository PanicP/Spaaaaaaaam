import pygame
from pygame.locals import *
from random import randint

class SimpleGame(object):

    def __init__(self,
                 title,
                 background_color,
                 window_size=(420,700),
                 fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.is_terminated = False
        self.background_color = background_color

    def terminate(self):
        self.is_terminated = True

    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)        

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.terminate()

    def run(self):
        self.init()
        while not self.is_terminated :
            self.__handle_events()
            self.update()
            self.surface.fill(self.background_color)
            self.render(self.surface)
            pygame.display.update()
            self.clock.tick(self.fps)
   
    
    def init(self):
        self.__game_init()

    def update(self):
        pass

    def render(self):
        pass


