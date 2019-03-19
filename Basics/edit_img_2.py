#! usr/bin/env python3

import cv2 
import numpy as np

class Rotate_img():
    def __init__(self):

        self.img = cv2.imread("/home/teo/Downloads/taok.jpg")

    def show_img(self):

        cv2.imshow("BIROLIRO", self.img)

    def rotate_img(self):
        
        rows,cols,_ = self.img.shape
        image_center = ((rows/2,cols/2))
        rot_mat = cv2.getRotationMatrix2D(image_center, 90, 1)
        self.result = cv2.warpAffine(self.img, rot_mat,(rows,cols), flags=cv2.INTER_LINEAR)
        cv2.imshow('sapoha',self.result)
    
    def save_img(self):

        cv2.imwrite("/home/teo/Downloads/taok_rot.jpg",self.result)

if __name__ == "__main__":

    run = Rotate_img()
    
    while True:
        run.show_img()
        run.rotate_img()
        run.save_img()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break