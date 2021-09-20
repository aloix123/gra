import pygame
from Kwadrat import Sqrt

class ClikManager:
  def __init__(self,screen):
    self.screen=screen
    self.kwdr = Sqrt(self.screen)
    pass
  def clikcheck(self):

    if pygame.mouse.get_pressed() and Sqrt.getlist()[0].collidepoint(pygame.mouse.get_pos()):
      Sqrt.createSQRT()
      Sqrt.getlist().remove(0)