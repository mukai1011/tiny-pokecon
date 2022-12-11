from typing_extensions import Protocol

import cv2


class Capture(Protocol):
    @property
    def capture_id(self) -> int:
        pass

    @capture_id.setter
    def capture_id(self, value: int):
        pass

    @property
    def current_image(self) -> cv2.Mat:
        pass


class PokeConCore(Protocol):
    @property
    def capture(self) -> Capture:
        pass
