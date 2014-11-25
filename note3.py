import pygame
from pygame.locals import *

class Note3(object):

    def __init__(self, y = 0):
        self.y = y
        self.rect3 = (636, self.y,  96,   10)
        self.is_hit3 = False

    def get_rect3(self):
        return self.rect3

    def delete3(self):
        self.y = 2000

    def hit3(self):
        self.is_hit3 = True

    def update(self):
        self.y += 8
        self.rect3 = (636, self.y,  96,   10)

    def render(self,surface):
        pygame.draw.rect(surface, pygame.Color('green'), self.rect3)