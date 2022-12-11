import tkinter as tk

from .capture_canvas import CaptureCanvas
from .select_capture_frame import SelectCaptureFrame
from .protocols import PokeConCore


class MainWindow:
    def __init__(self, controller: PokeConCore):
        root = tk.Tk()
        root.title("tiny-pokecon")

        SelectCaptureFrame(root, controller).pack()
        CaptureCanvas(root, controller).pack(expand=True, fill=tk.BOTH)

        self.__root = root

    def start(self):
        self.__root.mainloop()
