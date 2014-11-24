import pygame
from pygame.locals import *

class Note(object):

    def __init__(self, y = 0):
        self.y = y
        self.rect = (634, self.y,  98,   20)
        self.is_hit = False

    def get_rect(self):
        return self.rect

    def delete(self):
        self.y = 2000

    def hit(self):
        self.is_hit = True

    def update(self):
        self.y += 5
        self.rect = (634, self.y,  98,   20)

    def render(self,surface):
        pygame.draw.rect(surface, pygame.Color('orange'), self.rect)