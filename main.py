import pygame
from pygame.locals import *
from gamelib import SimpleGame
from note import Note

class Spaaaaaaaam(SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    BLUE = pygame.Color('blue')
    RED = pygame.Color('red')
    WINDOW_SIZE = (1366,768)

    def __init__(self):
  
        super(Spaaaaaaaam, self).__init__('Spaaaaaaaam [pre-alpha]', Spaaaaaaaam.BLACK, Spaaaaaaaam.WINDOW_SIZE)

    def init(self):

        super(Spaaaaaaaam, self).init()

        global notes, score

        notes = [Note(0),Note(100)]

    def render(self,surface):
        #pygame.draw.rect(self.surface, Spaaaaaaaam.RED, (0,  0,   60,   768))
        pygame.draw.rect(self.surface, Spaaaaaaaam.BLACK, (633,  0,   100,   768))
        pygame.draw.line(self.surface, Spaaaaaaaam.RED, (633, 700), (733, 700), 9)
        for i in range(1,3):
            pygame.draw.line(self.surface, Spaaaaaaaam.BLUE, (533+(100*i), 0), (533+(100*i), 768), 5)
        for note in notes:
            note.render(surface)

    def update(self):
        for note in notes:
            note.update()
        


def main():
    game = Spaaaaaaaam()
    game.run()
    #title = 'Spaaaaaaaam' put it into game - Spaaaaaaaam()

if __name__ == '__main__':
    main()
