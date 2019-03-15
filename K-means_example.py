#! usr/bin/env python3

import cv2
import numpy as np 
from matplotlib import pyplot as plot 

class Classification():
    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.z = 0

    def value_get(self):
        print(self.x, self.y, self.z)
        self.x = np.random.randint(25, 100,25)
        self.y = np.random.randint(175, 255, 25)
        self.z = np.hstack((self.x, self.y)
        print(self.x, self.y, self.z)
        self.z = self.z.reshape((50, 1))
        print(self.z)


if __name__ == "__main__":
    



