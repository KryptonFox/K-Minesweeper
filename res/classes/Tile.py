import pygame
from .Cut import Cutter
from .Sprite import Sprite
from ..Scripts.getnearest import getNearest


class Tile(Sprite):
    def __init__(self, images, x, y, index):
        super().__init__()
        # image and rect
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # variables
        self.count = 0
        self.opened = False
        self.flagged = False
        self.preclicked = False
        self.bomb = False
        self.index = index
        self.destroyed = False

    def click_right(self, field):
        if not self.opened:
            if not self.flagged:
                field.bomb_meter -= 1
                self.flagged = True
                self.image = self.images[2]
            else:
                field.bomb_meter += 1
                self.flagged = False
                self.image = self.images[0]

    def click_left(self, field, real=True):
        if not field.bombed:
            exclude = getNearest(self.index)
            exclude_list = []
            for nearRow in exclude:
                for nearTile in nearRow:
                    if -1 in nearTile or field.width == nearTile[1] or field.height == nearTile[0]:
                        continue
                    exclude_list.append(nearTile)
            field.bombGenerator(exclude_list)
            field.bombed = True
        if not self.flagged and not self.opened:
            self.image = self.images[1]
            self.opened = True
            field.closed -= 1
            if self.bomb:
                self.image = self.images[6]
                self.destroyed = True
                field.endGame()
            elif self.count > 0:
                self.image = self.images[self.count + 7]
            elif self.count == 0:
                nearest = getNearest(self.index)
                for nearRow in nearest:
                    for nearTile in nearRow:
                        if -1 in nearTile or field.width == nearTile[1] or field.height == nearTile[0]:
                            continue
                        try:
                            field.buttons[nearTile[0]][nearTile[1]].click_left(field, False)
                        except RecursionError:
                            return

        elif self.opened and real:
            nearest = getNearest(self.index)
            for nearRow in nearest:
                for nearTile in nearRow:
                    if -1 in nearTile or field.width == nearTile[1] or field.height == nearTile[0] or nearTile == self.index:
                        continue
                    button = field.buttons[nearTile[0]][nearTile[1]]
                    if not button.opened and not button.flagged:
                        button.click_left(field, False)

    def preclick(self, field):
        if not self.flagged and not self.opened:
            self.image = self.images[1]
            self.preclicked = True
        elif self.opened and self.count > 0:
            nearest = getNearest(self.index)
            for nearRow in nearest:
                for nearTile in nearRow:
                    if -1 in nearTile or field.width == nearTile[1] or field.height == nearTile[0]:
                        continue
                    field.buttons[nearTile[0]][nearTile[1]].prepreclick()

    def prepreclick(self):
        if not self.flagged and not self.opened:
            self.image = self.images[1]
            self.preclicked = True

    def open(self, win=False, field=None):
        if self.opened:
            return
        self.opened = True
        if self.flagged:
            if self.bomb:
                return
            elif not self.bomb:
                self.image = self.images[7]
        elif self.bomb:
            if win:
                self.image = self.images[2]
                self.flagged = True
                field.bomb_meter -= 1
            else:
                self.image = self.images[5]
        elif self.count == 0:
            self.image = self.images[1]
        elif self.count > 0:
            self.image = self.images[self.count + 7]
