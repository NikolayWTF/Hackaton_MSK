import imutils
import keras
import numpy as np
from helpers import sliding_window
from matplotlib import pyplot as plt
import time
import cv2
import os
import csv

files = os.listdir(path="bears")
Q = len(files)
#9, 10, 12, 16, 21, 24, 26, 28
i = 0
j = 0
first_x_good = []
first_y_good = []
neural_network = keras.models.load_model("model8.h5")
while i < Q:
	image = cv2.imread("bears/" + str(i) + ".jpg")
	(winW, winH) = (50, 50)
	image = imutils.resize(image, width=1000, height=1000)
	max_predict = 0
	second_predict = 0
	third_predict = 0
	max_ind = [0, 0]
	sec_ind = [0, 0]
	third_ind = [0, 0]
	for (x, y, window) in sliding_window(image, stepSize=40, windowSize=(winW, winH)):
		if window.shape[0] != winH or window.shape[1] != winW:
			continue
		clone = image.copy()
		cv2.imwrite("tmp_picture.jpg", clone[y : y + winH , x : x + winW])
		predict = neural_network.predict(np.array([plt.imread("tmp_picture.jpg")]))
		if(predict[0][1] >= third_predict):
			if(predict[0][1] >= second_predict):
				if(predict[0][1] >= max_predict):
					third_predict = second_predict
					second_predict = max_predict
					max_predict = predict[0][1]
					third_ind = [sec_ind[0], sec_ind[1]]
					sec_ind = [max_ind[0], max_ind[1]]
					max_ind = [x, y]
				else:
					third_predict = second_predict
					second_predict = predict[0][1]
					third_ind = [sec_ind[0], sec_ind[1]]
					sec_ind = [x, y]
			else:
				third_predict = predict[0][1]
				third_ind = [x, y]

	for (x, y, window) in sliding_window(image, stepSize=40, windowSize=(winW, winH)):
		if window.shape[0] != winH or window.shape[1] != winW:
			continue
		valid = 0
		if (x == third_ind[0] and y == third_ind[1]) or (x == sec_ind[0] and y == sec_ind[1]) or (x == max_ind[0] and y == max_ind[1]):
			valid = 1
		if (valid):
			clone = image.copy()
			cv2.imwrite("tmp_picture.jpg", clone[y: y + winH, x: x + winW])
			cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
			cv2.imshow("Window", clone)
			cv2.waitKey(1)
			cv2.imwrite("dataset2/" + str(j) + ".jpg", clone[y: y + winH, x: x + winW])
			first_x_good.append(x)
			first_y_good.append(y)
			time.sleep(0.01)
			j += 1
	i += 1




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

L = len(x_good)
i = 0
NAME = []
X = []
Y = []
while i < L:
	if x_good[i] > 0:
		NAME.append(str(i) + ".jpg")
		X.append(str(int((first_x_good[i] + x_good[i]) * 4.288)))
		Y.append(str(int((first_y_good[i] + y_good[i]) * 2.848)))
		print (str(i) + ".jpg", str(int((first_x_good[i] + x_good[i]) * 4.288)), str(int((first_y_good[i] + y_good[i]) * 2.848)))
	i += 1

with open("Forest_Group.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(NAME)
    file_writer.writerow(X)
    file_writer.writerow(Y)


