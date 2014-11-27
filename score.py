import pygame
from pygame.locals import *
from note1 import Note1
from note2 import Note2
from note3 import Note3

class Score(object):

    def __init__(self):
        self.score = 0
        self.percentage = 0

    def get_score(self):
        return int(self.score)

    def get_percentage(self):
        return float(self.percentage)

    def note_collide1(self, note):
        checkbox1 = []
        checkbox1.append(Rect(636,  675,   60,   50))

        if checkbox1[0].colliderect(note.get_rect1()) and not note.is_hit1 :
            if pygame.key.get_pressed()[K_SPACE]:
                note.hit1()
                note.delete1()
                self.score += 100
                self.percentage += (100.00/336.00)
            #elif pygame.key.get_pressed()[K_f] and i == 1:
                #note.hit()
                #self.score += 100

    def note_collide2(self, note):
        checkbox2 = []
        checkbox2.append(Rect(636,  675,   60,   50))

        if checkbox2[0].colliderect(note.get_rect2()) and not note.is_hit2 :
            if pygame.key.get_pressed()[K_f]:
                note.hit2()
                note.delete2()
                self.score += 100
                self.percentage += (100.00/336.00)
                #increase_percentage()

    def note_collide3(self, note):
        checkbox3 = []
        checkbox3.append(Rect(636,  675,   60,   50))

        if checkbox3[0].colliderect(note.get_rect3()) and not note.is_hit3 :
            if pygame.key.get_pressed()[K_j]:
                note.hit3()
                note.delete3()
                self.score += 100
                self.percentage += (100.00/336.00)
                #increase_percentage()
            

    def update1(self, note):
        self.note_collide1(note)

    def update2(self, note):
        self.note_collide2(note)

    def update3(self, note):
        self.note_collide3(note)

