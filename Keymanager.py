
import pygame,sys
class Keymanager():
  def __init__(self):
    pass
  def returnkeys(self):
    for key in pygame.event.get():
      if key.type==pygame.QUIT:
        sys.exit()