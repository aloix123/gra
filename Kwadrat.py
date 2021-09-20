import pygame
import random

class Sqrt:
  def __init__(self,screen):
    self.screen=screen
    self.sqrtlist=[]
    self.hight=30
    self.startrect=pygame.rect.Rect(500,500,self.hight,self.hight)

    self.sqrtlist.append(self.startrect)
  def blitsqrt(self):
    for kwadrat in self.sqrtlist:
      pygame.draw.rect(self.screen,(160,160,160),kwadrat)
  
  def createSQRT(self):

    self.sqrtlist.append(pygame
                         .rect
                         .Rect(random.randint(0,self.screen.get_width())
                               ,random.randint(0,self.screen.get_height()),self.hight,

                                         self.hight))
  @staticmethod
  def getlist(self):
    return self.sqrtlist
