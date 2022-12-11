from __future__ import annotations
import math
from time import perf_counter

import tkinter as tk

from PIL import Image, ImageTk
import cv2

from .protocols import PokeConCore


class CaptureCanvas(tk.Canvas):

    def __init__(self, master: tk.Misc, controller: PokeConCore):
        super().__init__(master, background="#000000")

        # 1個前の画像の参照を残しておかないと、GCに破棄されてしまい常にちらつく
        # https://stackoverflow.com/questions/20307718/python-tkinter-display-images-on-canvas-it-always-blink
        self.__previous: ImageTk.PhotoImage | None = None

        # __updateにかかるミリ秒数の平均を求める
        self.__sum: int = 0
        self.__count: int = 0

        self.__capture = controller.capture
        self.after_idle(self.__update)

    def __update(self):

        start_time = perf_counter()
        
        try:
            bgr = cv2.resize(self.__capture.current_image, dsize=(
                self.winfo_width(), self.winfo_height()))
            rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
            pil = Image.fromarray(rgb)
            tk = ImageTk.PhotoImage(image=pil)
            self.__previous = tk
            
            self.create_image(0, 0, image=tk, anchor="nw")
        except:
            pass

        # 1000フレームごとに平均をリセット
        # intに大きな数字を格納したくないので
        if 1000 < self.__count:
            self.__sum = 0
            self.__count = 0
        self.__sum += math.ceil((perf_counter() - start_time) * 1000)
        self.__count += 1

        # print(math.ceil(self.__sum / self.__count))
        self.after(math.ceil(self.__sum / self.__count), self.__update)
