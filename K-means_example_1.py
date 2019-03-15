#! usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plot


class Classification():
    def __init__(self):

        self.x = 0
        self.y = 0
        self.z = 0

    def value_atrib(self):

        self.x = np.random.randint(25, 100, 25)
        self.y = np.random.randint(175, 255, 25)
        self.z = np.hstack((self.x, self.y))
        self.z = self.z.reshape((50, 1))
        self.z = np.float32(self.z)
        plot.hist(self.z, 256, [0, 256]), plot.show()

    def method(self):

        # Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

        # Set flags (Just to avoid line break in the code)
        flags = cv2.KMEANS_RANDOM_CENTERS

        # Apply KMeans
        compactness, labels, centers = cv2.kmeans(self.z, 2, None, criteria, 10, flags)

        A = self.z[labels == 0]
        B = self.z[labels == 1]

        # Now plot 'A' in red, 'B' in blue, 'centers' in yellow
        plot.hist(A, 256, [0, 256], color='r')
        plot.hist(B, 256, [0, 256], color='b')
        plot.hist(centers, 32, [0, 256], color='y')
        plot.show()


if __name__ == "__main__":

    run = Classification()

    while True:

        run.value_atrib()
        run.method()
        break
