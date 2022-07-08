import pygame
from ..Sprite import Sprite


class MenuButton(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('res/images/icon_mini.png'), (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
