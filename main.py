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

        #0 ~ 2000 intro
        #2000 ~ 8600 verse 1.1
        #8600 ~ 15900 verse 1.2
        #15900 ~ 17600 chorus 1.1
        #17600 ~ 19300 chorus 1.2
        #19300 ~ 20920 chorus 1.3
        #20920 ~ 22520 chorus 1.4
        #22520 ~ 24110 verse 2.1
        #24110 ~ 25810 verse 2.2
        #25810 ~ 27460 verse 2.3
        #27460 ~ 29100 verse 2.4
        #29100 ~ 31360 verse 3.1
        #31360 ~ 35700 verse 3.2
        #35700 ~ 40520 verse 4.1
        #40520 ~ 42200 verse 4.2
        #42200 ~ 43870 chorus 2.1
        #43870 ~ 45570 chorus 2.2
        #45570 ~ 47220 chorus 2.3
        #47220 chorus 2.4 to outro

        #note1 mid note
        notes1 =  [Note1(-520), 
                   Note1(-2200), Note1(-2470), Note1(-2570), Note1(-2860), Note1(-2960), Note1(-3800), Note1(-4400), Note1(-5300), Note1(-5500), Note1(-5800), Note1(-6650), Note1(-6900), Note1(-7170), Note1(-7380), Note1(-7590), Note1(-7800), Note1(-8010), Note1(-8220), Note1(-8520),
                   Note1(-8750), Note1(-8960), Note1(-9170), Note1(-9380), Note1(-9590), Note1(-9800), Note1(-10010), Note1(-10220), Note1(-10430), Note1(-10640), Note1(-10850), Note1(-11060), Note1(-11310), Note1(-11460), Note1(-11610), Note1(-11800), Note1(-12010), Note1(-12220), Note1(-12430), Note1(-12640), Note1(-12850), Note1(-13060), Note1(-13270), Note1(-13480), Note1(-13720), Note1(-13860), Note1(-14000), Note1(-14140), Note1(-14280), Note1(-14420), Note1(-14560), Note1(-14700), Note1(-14840), Note1(-14980),
                   Note1(-16100), Note1(-16300), Note1(-16500), Note1(-16850), Note1(-17050), Note1(-17330), Note1(-17490), 
                   Note1(-17800), Note1(-18000), Note1(-18200), Note1(-18550), Note1(-18750), Note1(-19030), Note1(-19190), 
                   Note1(-19500), Note1(-19800), Note1(-19900), Note1(-20000), Note1(-20200), Note1(-20400), Note1(-20680), Note1(-20840),
                   Note1(-21150), Note1(-21450), Note1(-21550), Note1(-21750), Note1(-21900), Note1(-22000), Note1(-22280), Note1(-22440),
                   Note1(-22640), Note1(-22840), Note1(-23040), Note1(-23390), Note1(-23590), Note1(-23870), Note1(-24030),
                   Note1(-24340), Note1(-24540), Note1(-24740), Note1(-25090), Note1(-25290), Note1(-25570), Note1(-25730),
                   Note1(-26040), Note1(-26240), Note1(-26440), Note1(-26540), Note1(-26740), Note1(-26940), Note1(-27220), Note1(-27380),
                   Note1(-27700), Note1(-29100),
                   Note1(-29400), Note1(-29900),
                   Note1(-31900), Note1(-32400),
                   Note1(-36120), Note1(-36920), Note1(-37720), Note1(-38520), Note1(-39320), Note1(-40120),
                   Note1(-40870), Note1(-41010), Note1(-41150), Note1(-41290), Note1(-41430), Note1(-41570), Note1(-41710), Note1(-41850), Note1(-41990), Note1(-42130),
                   Note1(-42400), Note1(-42600), Note1(-42800), Note1(-43150), Note1(-43350), Note1(-43630), Note1(-43790),
                   Note1(-44100), Note1(-44300), Note1(-44500), Note1(-44850), Note1(-45050), Note1(-45330), Note1(-45490),
                   Note1(-45800), Note1(-46100), Note1(-46200), Note1(-46300), Note1(-46500), Note1(-46700), Note1(-46980), Note1(-47140),
                   Note1(-47450), Note1(-47750), Note1(-47850), Note1(-48050), Note1(-48250), Note1(-48550), Note1(-48650), Note1(-48850), Note1(-49050), Note1(-49350), Note1(-49450), Note1(-49650), Note1(-49650), Note1(-49800), Note1(-49900), Note1(-50180), Note1(-50340), Note1(-50670), Note1(-50870), Note1(-51070)]
        
        #note2 left note
        notes2 =  [Note2(-850), Note2(-1350), Note2(-1650), Note2(-1710), Note2(-1770), Note2(-1830), Note2(-1890), 
                   Note2(-3300), Note2(-3400), Note2(-4150), Note2(-4600), Note2(-4700), Note2(-4800), Note2(-5000), Note2(-5750), Note2(-6200), Note2(-6600), Note2(-7100), Note2(-7310), Note2(-7520), Note2(-7730), Note2(-7940), Note2(-8150),
                   Note2(-11260), Note2(-11410), Note2(-11560), Note2(-13650), Note2(-13930), Note2(-14210), Note2(-14490), Note2(-14770), Note2(-15050), Note2(-15400), Note2(-15820), 
                   Note2(-17250), Note2(-17570),
                   Note2(-18950), Note2(-19270),
                   Note2(-20600), Note2(-20920),
                   Note2(-22200), Note2(-22520),
                   Note2(-23790), Note2(-24110),
                   Note2(-25490), Note2(-25810),
                   Note2(-27140), Note2(-27460),
                   Note2(-27900), Note2(-28300), Note2(-28700),
                   Note2(-29300), Note2(-29800), Note2(-30450), Note2(-30880), Note2(-31310),
                   Note2(-31800), Note2(-32300), Note2(-32700), Note2(-33100), Note2(-33500), Note2(-33900), Note2(-34300), Note2(-34700), Note2(-35100), Note2(-35500),
                   Note2(-35920), Note2(-36320), Note2(-36720), Note2(-37120), Note2(-37520), Note2(-37920), Note2(-38320), Note2(-38720), Note2(-39120), Note2(-39520), Note2(-39920), Note2(-40320),
                   Note2(-40800), Note2(-41080), Note2(-41360), Note2(-41640), Note2(-41920), Note2(-42200),
                   Note2(-43550), Note2(-43870),
                   Note2(-45250), Note2(-45570),
                   Note2(-46900), Note2(-47220),
                   Note2(-50100), Note2(-50420)]
        
        #note3 right note
        notes3 =  [Note3(-900), Note3(-1130), Note3(-1430), Note3(-1680), Note3(-1740), Note3(-1800), Note3(-1860), Note3(-1920), 
                   Note3(-3350), Note3(-4100), Note3(-4200), Note3(-4650), Note3(-4750), Note3(-4850), Note3(-5050), Note3(-5850), Note3(-6250), Note3(-6700), Note3(-7240), Note3(-7450), Note3(-7660), Note3(-7870), Note3(-8080), Note3(-8290),
                   Note3(-11360), Note3(-11510), Note3(-11660), Note3(-13790), Note3(-14070), Note3(-14350), Note3(-14630), Note3(-14910), Note3(-15500), Note3(-15870), 
                   Note3(-17410),
                   Note3(-19110),
                   Note3(-20760),
                   Note3(-22360),
                   Note3(-23950),
                   Note3(-25650),
                   Note3(-27300),
                   Note3(-28100), Note3(-28500), Note3(-28900),
                   Note3(-29500), Note3(-30000), Note3(-30500), Note3(-30930), Note3(-31360),
                   Note3(-32000), Note3(-32500), Note3(-32900), Note3(-33300), Note3(-33700), Note3(-34100), Note3(-34500), Note3(-34900), Note3(-35300), Note3(-35700),
                   Note3(-36520), Note3(-37320), Note3(-38120), Note3(-38920), Note3(-39720), Note3(-40520),
                   Note3(-40940), Note3(-41220), Note3(-41500), Note3(-41780), Note3(-42060),
                   Note3(-43710),
                   Note3(-45410),
                   Note3(-47060),
                   Note3(-50260)]

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
