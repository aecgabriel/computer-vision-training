#! usr/bin/env python3

import cv2
import numpy as np


class Classification():
    def __init__(self):

        self.img = cv2.imread("/home/teo/Downloads/digits.png")
        self._train = 0
        self._test = 0

    def data(self):

        # Convert the data to gray scale
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # Split the image to 5000 cells, each 20x20
        cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
        # Make it into Numpy array. It size will be (50,100,20,20)
        x = np.array(cells)
        # Now we prepare train_data and test_data.
        self._train = x[:, :50].reshape(-1, 400).astype(np.float32)  # Size = (2500, 400)
        self._test = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # Size = (2500, 400)

    def method(self):

        # Create labels for train and test data
        k = np.arange(10)
        train_labels = np.repeat(k, 250)[:, np.newaxis]
        test_labels = train_labels.copy()
        # Initiate kNN, train the data, then test it with test data for k=1
        knn = cv2.ml.KNearest_create()
        knn.train(self._train, cv2.ml.ROW_SAMPLE, train_labels)
        _ret, result, neighbours, dist = knn.findNearest(self._test, k=5)
        # Now we check the accuracy of classification
        # For that, compare the result with test_labels and check which are wrong
        matches = result == test_labels
        correct = np.count_nonzero(matches)
        accuracy = correct*100.0/result.size
        print(accuracy)
        # save the data
        np.savez('knn_data.npz', train=self._train, train_labels=train_labels)


if __name__ == "__main__":

    run = Classification()

    while True:

        run.data()
        run.method()
        break
