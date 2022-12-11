import tkinter as tk
from tkinter import ttk

from .protocols import PokeConCore


class SelectCaptureFrame(ttk.Frame):

    def __init__(self, master: tk.Misc, controller: PokeConCore):
        super().__init__(master, padding=16)

        self.__capture = controller.capture

        label = ttk.Label(self, text='capture_id')

        self.__id = tk.StringVar()
        self.__id.set(str(self.__capture.capture_id))
        entry = ttk.Entry(self, textvariable=self.__id)

        button = ttk.Button(
            self,
            text='Change',
            command=self.__change_capture_id
        )

        label.pack(side=tk.LEFT)
        entry.pack(side=tk.LEFT)
        button.pack(side=tk.LEFT)

    def __change_capture_id(self):
        temp = self.__id.get()
        if not temp.isnumeric() or not float(temp).is_integer():
            return
        self.__capture.capture_id = int(temp)
