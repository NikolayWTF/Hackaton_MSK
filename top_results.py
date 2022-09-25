import imutils
import keras
import numpy as np
from helpers import sliding_window
from matplotlib import pyplot as plt
import time
import cv2

import os

files = os.listdir(path="bears")
Q = len(files)


image = cv2.imread("bears/1.jpg")
(winW, winH) = (50, 50)
image = imutils.resize(image, width=1000, height=1000)
neural_network = keras.models.load_model("model7.h5")
neural_network2 = keras.models.load_model("model8.h5")
x_good = []
y_good = []
for (x, y, window) in sliding_window(image, stepSize=40, windowSize=(winW, winH)):
	if window.shape[0] != winH or window.shape[1] != winW:
		continue
	clone = image.copy()
	cv2.imwrite("tmp_picture.jpg", clone[y : y + winH , x : x + winW])
	predict = neural_network.predict(np.array([plt.imread("tmp_picture.jpg")]))
	if (predict[0][1] >= 0.95):
		# x_good.append(x)
		# y_good.append(y)
		predict2 = neural_network2.predict(np.array([plt.imread("tmp_picture.jpg")]))
		if (predict[0][1] >= 0.96):
			cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
			cv2.imshow("Window", clone)
			cv2.waitKey(1)
			time.sleep(1)



	#for (x, y, window) in sliding_window(resized, stepSize=10, windowSize=(winW, winH)):
	# 		# if the window does not meet our desired window size, ignore it
	# 		if window.shape[0] != winH or window.shape[1] != winW:
	# 			continue
	#
	# 		clone = resized.copy()
	# 		# i += 1
	# 		cv2.imwrite("tmp_picture.jpg", clone[y : y + winH , x : x + winW])
	# 		# cv2.imwrite("image/picture" + str(i) + ".jpg", clone[y: y + winH, x: x + winW])
	# 		# predict = neural_network.predict(np.array([plt.imread("tmp_picture.jpg")]))
	# 		# if(predict[0][1] >= 0.5):
	#
	# 		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
	# 		cv2.imshow("Window", clone)
	# 		cv2.waitKey(1)
			# time.sleep(0.01)

