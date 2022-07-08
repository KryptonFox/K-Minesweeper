import pygame


class Cutter:
    def __init__(self):
        self.image = None
        self.size = [16, 16]

    def load(self, image, size=[16, 16]):
        self.image = image
        self.size = size
        return self.load_tileset()

    @staticmethod
    def clip(surf, x, y, x_size, y_size):
        clipR = pygame.Rect(x, y, x_size, y_size)
        image = surf.subsurface(clipR).convert_alpha()
        return image

    def load_tileset(self):
        rows = self.image.get_height() // self.size[1]
        cols = self.image.get_width() // self.size[0]
        images = []
        for row in range(rows):
            for tile in range(cols):
                images.append(self.clip(self.image, tile * (self.size[0] + 1), row * (self.size[1] + 1), self.size[0], self.size[1]))
        return images
