from tkinter import *
from .MenuFrame1 import Frame1
from .MenuFrame2 import Frame2
import tkinter.messagebox as msgbox


class Menu(Tk):
    def __init__(self, cfg):
        super().__init__()

        self.cfg = cfg

        self.resizable(width=False, height=False)
        self.geometry('400x200')
        self.iconbitmap('res/images/icon_mini.png')
        self.title('K-Minesweeper. Выбор сложности')

        self.frame = 1
        self.mode = cfg['default_mode']
        self.fr = Frame1(self, self.new_frame, self.set_preset)
        self.fr.pack(expand=True, fill=X)
        self.mainloop()

    def set(self, width, height, bombs):
        if 3 > width > 100 or 3 > height > 100 or bombs > (width * height - 9):
            msgbox.showerror('Ошибка данных', 'Введённые данные некорректны')
        else:
            self.mode = [width, height, bombs]
            self.destroy()

    def set_preset(self, preset):
        preset = self.cfg['modes'][preset]
        self.set(preset[0], preset[1], preset[2])

    def new_frame(self):
        if self.frame == 1:
            self.geometry('400x260')
            self.fr.pack_forget()
            self.fr = Frame2(self, self.new_frame, self.set)
            self.fr.pack(expand=True, fill=X)
            self.frame = 2
        elif self.frame == 2:
            self.geometry('400x200')
            self.fr.pack_forget()
            self.fr = Frame1(self, self.new_frame, self.set_preset)
            self.fr.pack(expand=True, fill=X)
            self.frame = 1
