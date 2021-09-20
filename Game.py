#trex xddddddd
import pygame
from Keymanager import Keymanager
from Kwadrat import Sqrt


class Game:
  def __init__(self):
    self.screen = pygame.display.set_mode((1200, 1000))
    self.keys=Keymanager()
    self.kwdr=Sqrt(self.screen)
    self.kwdr.createSQRT()

  def rungame(self):

    while (True):

      self.screenmake()
      self.kwdr.blitsqrt()
      self.keys.returnkeys()
      pygame.display.flip()
  def screenmake(self):
    self.screen.fill((41,41,41))