import pygame


class Sprite:
    def __init__(self):
        self.image = pygame.Surface((10, 10))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
