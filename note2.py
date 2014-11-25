import pygame
from pygame.locals import *

class Note2(object):

    def __init__(self, y = 0):
        self.y = y
        self.rect2 = (636, self.y,  96,   10)
        self.is_hit2 = False

    def get_rect2(self):
        return self.rect2

    def delete2(self):
        self.y = 2000

    def hit2(self):
        self.is_hit2 = True

    def update(self):
        self.y += 8
        self.rect2 = (636, self.y,  96,   10)

    def render(self,surface):
        pygame.draw.rect(surface, pygame.Color('Cyan'), self.rect2)