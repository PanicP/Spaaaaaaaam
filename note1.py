import pygame
from pygame.locals import *

class Note1(object):

    def __init__(self, y = 0):
        self.y = y
        self.rect1 = (636, self.y,  96,   10)
        self.is_hit1 = False

    def get_rect1(self):
        return self.rect1

    def delete1(self):
        self.y = 2000

    def hit1(self):
        self.is_hit1 = True

    def update(self):
        self.y += 8
        self.rect1 = (636, self.y,  96,   10)

    def render(self,surface):
        pygame.draw.rect(surface, pygame.Color('orange'), self.rect1)