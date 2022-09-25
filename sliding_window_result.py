import imutils
import keras
import numpy as np
from helpers import sliding_window
from matplotlib import pyplot as plt
import time
import cv2
import os

files = os.listdir(path="dataset2")
Q = len(files)
i = 0

neural_network = keras.models.load_model("model_mini2.h5")
x_good = []
y_good = []
while i < Q:
    image = cv2.imread("dataset2/" + str(i) + ".jpg")
    (winW, winH) = (10, 10)
    image = imutils.resize(image, width=50, height=50)
    max_predict = 0
    max_ind = [0, 0]

    for (x, y, window) in sliding_window(image, stepSize=10, windowSize=(winW, winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        clone = image.copy()
        cv2.imwrite("tmp_picture.jpg", clone[y: y + winH, x: x + winW])
        predict = neural_network.predict(np.array([plt.imread("tmp_picture.jpg")]))

        if(predict[0][1] >= max_predict):
            max_predict = predict[0][1]
            max_ind = [x, y]

    for (x, y, window) in sliding_window(image, stepSize=10, windowSize=(winW, winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        valid = 0
        if (x == max_ind[0] and y == max_ind[1]):
            valid = 1
        if (valid):
            if (max_predict >= 0.6):
                cv2.imwrite("tmp_picture.jpg", clone[y: y + winH, x: x + winW])
                cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
                cv2.imshow("Window", clone)
                cv2.waitKey(1)
                x_good.append(x+(winW/2))
                y_good.append(y+(winH/2))
                time.sleep(3)
            else:
                x_good.append(0)
                y_good.append(0)
    i += 1

print(x_good, y_good)
