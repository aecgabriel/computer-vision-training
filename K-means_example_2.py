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

        self.x = np.random.randint(25, 50, (25, 2))
        self.y = np.random.randint(60, 85, (25, 2))
        self.z = np.vstack((self.x, self.y))
        self.z = np.float32(self.z)

    def method(self):

        # Define the criteria and apply k-means
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret, label, center = cv2.kmeans(self.z, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Separete the data
        A = self.z[label.ravel() == 0]
        B = self.z[label.ravel() == 1]

        # Plot the data
        plot.scatter(A[:, 0], A[:, 1])
        plot.scatter(B[:, 0], B[:, 1], c='r')
        plot.scatter(center[:, 0], center[:, 1], s=80, c='y', marker='s')
        plot.xlabel('Height'), plot.ylabel('Weight')
        plot.show()


if __name__ == "__main__":

    run = Classification

    while True:
        run.value_atrib()
        run.method()
        break
