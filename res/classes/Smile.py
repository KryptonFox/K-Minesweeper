import pygame
from .Cut import Cutter
from .Sprite import Sprite


class Smile(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = Cutter().load(pygame.image.load('res/images/smiles.png'), [24, 24])
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.state = 0

    def setState(self, state):
        self.state = state
        self.image = self.images[state]
