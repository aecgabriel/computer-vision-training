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

        self.corners = cv2.cornerHarris(self.gray, 2, 3, 0.06)
        self.corners = cv2.dilate(self.corners, None)
        self.img[self.corners > 0.01*self.corners.max()] = [0, 0, 255]
        cv2.imwrite("/home/teo/Imagens/checkerboard2.png", self.img)


if __name__ == "__main__":
    run = Ident_corners()

    while True:
        run.value_atrib()
        run.method()
        break
