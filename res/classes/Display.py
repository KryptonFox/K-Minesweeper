import pygame
from .Sprite import Sprite
from .Cut import Cutter


class Display(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = Cutter().load(pygame.image.load('res/images/numbers.png').convert_alpha(), [13, 23])
        self.image = pygame.Surface((39, 23))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.value = 0
        self.visible = True

        self.setValue(self.value)

    def setValue(self, value):
        if value > 999: value = 999
        elif value < -99: value = -99
        self.value = value
        val = str(self.value)
        if len(val) < 3:
            val = '0' * (3 - len(val)) + val
            if -10 < self.value < 0:
                val = '-0' + val[2]
        for i, n in enumerate(val):
            self.image.blit(self.images[9 if n == '0' else 10 if n == '-' else int(n) - 1], (i * 13, 0))

    def draw(self, display):
        if self.visible:
            display.blit(self.image, (self.rect.x, self.rect.y))
