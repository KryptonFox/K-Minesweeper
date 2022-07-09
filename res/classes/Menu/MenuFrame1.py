from tkinter import *
import tkinter.ttk as ttk


class Frame1(Frame):
    def __init__(self, root, command, set_command):
        super().__init__(root)
        ttk.Style().configure('TButton', font=('Segoe UI', 16))
        button = ttk.Button(self, command=command, text='Свои настройки')
        hard1 = ttk.Button(self, command=lambda: set_command('beginner'), text='Новичок')
        hard2 = ttk.Button(self, command=lambda: set_command('middle'), text='Любитель')
        hard3 = ttk.Button(self, command=lambda: set_command('pro'), text='Профессионал')

        button.pack(padx=10, fill=X, pady=5, expand=True)
        hard1.pack(pady=5, fill=X, padx=10)
        hard2.pack(pady=5, fill=X, padx=10)
        hard3.pack(pady=5, fill=X, padx=10)
