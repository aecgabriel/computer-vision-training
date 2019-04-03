#! usr/bin/env python3

import cv2
import numpy as np


class Ident_corners():
    def __init__(self):

        self.img = cv2.imread('/home/teo/Imagens/checkerboard.png')

    def value_atrib(self):

        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.gray = np.float32(self.gray)

    def method(self):

        self.corners = cv2.goodFeaturesToTrack(self.gray, 100, 0.20, 10)
        self.corners = np.int0(self.corners)
        for corner in self.corners:
            x, y = corner.ravel()
            cv2.circle(self.img, (x, y), 3, 255, -1)
        cv2.imwrite("/home/teo/Imagens/checkerboard1.png", self.img)


if __name__ == "__main__":
    run = Ident_corners()

    while True:
        run.value_atrib()
        run.method()
        break
