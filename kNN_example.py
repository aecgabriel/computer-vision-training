#! usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plot


class Classification():
    def __init__(self):

        self.traindata = 0
        self.responses = 0

    def data(self):

        # Feature set containing (x,y) values of 25 know/training data
        self.traindata = np.random.randint(0, 100, (25, 2)).astype(np.float32)

        # Labels each one either Red or Blue with numbers 0 and 1
        self.responses = np.random.randint(0, 2, (25, 1))

    def method(self):

        # Take Red families and plot them
        red = self.traindata[self.responses.ravel() == 0]
        plot.scatter(red[:, 0], red[:, 1], 80, 'r', 'x')

        blue = self.traindata[self.responses.ravel() == 1]
        plot.scatter(blue[:, 0], blue[:, 1], 80, 'b', 'o')

        newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
        plot.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

        knn = cv2.ml.KNearest_create()
        knn.train(self.traindata, cv2.ml.ROW_SAMPLE, self.responses)
        ret, results, neighbours, dist = knn.findNearest(newcomer, 5)

        print("result: ", results, "\n")
        print("neighbours: ", neighbours, "\n")
        print("distance: ", dist)

        plot.show()


if __name__ == "__main__":

    run = Classification()

    while True:
        run.data()
        run.method()
        break
