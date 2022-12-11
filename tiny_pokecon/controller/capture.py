from typing import cast

import cv2


class Capture:
    def __init__(self) -> None:
        self.__capture_id = 0
        self.__capture = cv2.VideoCapture(self.__capture_id)
        if not self.__capture.isOpened():
            raise IOError()

    def __del__(self):
        self.__capture.release()

    @property
    def capture_id(self):
        return self.__capture_id

    @capture_id.setter
    def capture_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError()

        self.__capture_id = value
        self.__capture.release()
        self.__capture = cv2.VideoCapture(self.__capture_id)
        if not self.__capture.isOpened():
            raise IOError()

    @property
    def current_image(self):
        _, mat = cast("tuple[bool, cv2.Mat]", self.__capture.read())
        return mat
