import pygame, pygame.mixer
from pygame.locals import *
from gamelib import SimpleGame
from note1 import Note1
from note2 import Note2
from note3 import Note3
from score import Score

class Spaaaaaaaam(SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    BLUE = pygame.Color('blue')
    RED = pygame.Color('red')
    WINDOW_SIZE = (1366,768)
    #pygame.mixer.pre_init(11025, -16, 2, 256)
    pygame.mixer.pre_init(44100, -16, 2, 4196)
    #pygame.mixer.pre_init(48000, -16, 1, 1024)

    def __init__(self):
  
        super(Spaaaaaaaam, self).__init__('Spaaaaaaaam [pre-alpha]', Spaaaaaaaam.BLACK, Spaaaaaaaam.WINDOW_SIZE)

    def init(self):

        super(Spaaaaaaaam, self).init()

        global notes1, notes2, notes3, score, sound
        score = Score() 

        #-0 ~ -2000 intro
        #-2000 ~ 8600 verse 1.1
        notes1 = [Note1(-520), 
                  Note1(-2200), Note1(-2470), Note1(-2570), Note1(-2860), Note1(-2960), Note1(-3800), Note1(-4400), Note1(-5300), Note1(-5500), Note1(-5800), Note1(-6650), Note1(-6900), Note1(-7170), Note1(-7380), Note1(-7590), Note1(-7800), Note1(-8010), Note1(-8220), Note1(-8520),
                  Note1(-8750), Note1(-8960), Note1(-9170), Note1(-9380), Note1(-9590), Note1(-9800), Note1(-10010), Note1(-10220), Note1(-10430), Note1(-10640), Note1(-10850), Note1(-11060), Note1(-11210)]
        notes2 = [Note2(-850), Note2(-1350), Note2(-1650), Note2(-1710), Note2(-1770), Note2(-1830), Note2(-1890), 
                  Note2(-3300), Note2(-3400), Note2(-4150), Note2(-4600), Note2(-4700), Note2(-4800), Note2(-5000), Note2(-5750), Note2(-6200), Note2(-6600), Note2(-7100), Note2(-7310), Note2(-7520), Note2(-7730), Note2(-7940), Note2(-8150),
                  Note2(-11160)]
        notes3 = [Note3(-900), Note3(-1130), Note3(-1430), Note3(-1680), Note3(-1740), Note3(-1800), Note3(-1860), Note3(-1920), 
                  Note3(-3350), Note3(-4100), Note3(-4200), Note3(-4650), Note3(-4750), Note3(-4850), Note3(-5050), Note3(-5850), Note3(-6250), Note3(-6700), Note3(-7240), Note3(-7450), Note3(-7660), Note3(-7870), Note3(-8080), Note3(-8290),
                  Note3(-11260)]

        sound = pygame.mixer.Sound('Brahms.wav')


    def render(self,surface):
        #pygame.draw.rect(self.surface, Spaaaaaaaam.RED, (0,  0,   60,   768))
        pygame.draw.rect(self.surface, Spaaaaaaaam.BLACK, (633,  0,   100,   768))
        pygame.draw.line(self.surface, Spaaaaaaaam.RED, (633, 700), (733, 700), 9)
        for i in range(1,3):
            pygame.draw.line(self.surface, Spaaaaaaaam.BLUE, (533+(100*i), 0), (533+(100*i), 768), 5)
        for note1 in notes1:
            note1.render(surface)
        for note2 in notes2:
            note2.render(surface)
        for note3 in notes3:
            note3.render(surface)
        surface.blit(score_image, (1000,10))
        sound.play()


    def update(self):
        global score_image
        for note1 in notes1:
            note1.update()
            score.update1(note1)
        for note2 in notes2:
            note2.update()
            score.update2(note2)
        for note3 in notes3:
            note3.update()
            score.update3(note3)
        score_image = self.font.render("Score = %d" % score.get_score() , 0, Spaaaaaaaam.WHITE)
            
        #amixer set PCM -- 1000

def main():
    game = Spaaaaaaaam()
    game.run()
    #title = 'Spaaaaaaaam' put it into game - Spaaaaaaaam()

if __name__ == '__main__':
    main()
