#! usr/bin/env python3

import cv2 as cv


class Image_reader():
    def __init__(self):

        self.img = cv.imread("/home/aecgabriel/Downloads/taok.jpeg")

    def show_img(self):

        cv.imshow("BIROLIRO", self.img)

    def modify_img(self):

        font = cv.FONT_ITALIC
        cv.putText(self.img, "NO", (10, 200), font, 3, (1, 1, 1), 2, cv.LINE_AA)

    def save_img(self):

        cv.imwrite("/home/aecgabriel/Downloads/taok2.png", self.img)
        new_img = cv.imread("/home/aecgabriel/Downloads/taok2.png")
        cv.imshow("New img", new_img)


if __name__ == "__main__":

    run = Image_reader()

    while True:
        run.show_img()
        run.modify_img()
        run.save_img()
        cv.waitKey(3000)
        cv.destroyAllWindows()
        break
