#! usr/bin/env python3

import cv2 
import numpy as np

class Rotate_img():
    def __init__(self):

        self.img = cv2.imread("/home/teo/Downloads/taok.jpg")

    def show_img(self):

        cv2.imshow("BIROLIRO", self.img)

    def rotate_img(self):

        image_center = tuple(np.array(self.img.shape))
        

if __name__ == "__main__":

    run = Rotate_img()
    
    while True:
        run.show_img()
        run.rotate_img()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break