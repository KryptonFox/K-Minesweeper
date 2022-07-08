from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox


class Frame2(Frame):
    def __init__(self, root, command, set_command):
        super().__init__(root)
        self.set_command = set_command

        ttk.Style().configure('TButton', font=('Segoe UI', 16))
        ttk.Style().configure('TEntry', font=('Segoe UI', 16))
        button = ttk.Button(self, command=command, text='Готовые настройки')
        button.pack(padx=10, pady=10, fill=X, expand=True)

        fr = Frame(self)
        Label(fr, text='Ширина:', font=('Segoe UI', 16)).pack(side=LEFT)
        self.inp1 = ttk.Entry(fr, font=('Segoe UI', 16))
        self.inp1.pack(side=RIGHT, pady=5)
        fr.pack(expand=True, fill=X, padx=10)

        fr = Frame(self)
        Label(fr, text='Высота:', font=('Segoe UI', 16)).pack(side=LEFT)
        self.inp2 = ttk.Entry(fr, font=('Segoe UI', 16))
        self.inp2.pack(side=RIGHT, pady=5)
        fr.pack(expand=True, fill=X, padx=10)

        fr = Frame(self)
        Label(fr, text='Бомбы:', font=('Segoe UI', 16)).pack(side=LEFT)
        self.inp3 = ttk.Entry(fr, font=('Segoe UI', 16))
        self.inp3.pack(side=RIGHT, pady=5)
        fr.pack(expand=True, fill=X, padx=10)

        ttk.Button(self, text='Подтвердить', command=self.button).pack(side=BOTTOM, fill=X, padx=10, pady=10)

    def button(self):
        try:
            self.set_command(int(self.inp1.get()), int(self.inp2.get()), int(self.inp3.get()))
        except:
            msgbox.showerror('Ошибка данных', 'Введённые данные некорректны')
