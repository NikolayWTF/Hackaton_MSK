import time

import imutils
from helpers import sliding_window
import cv2
j = 0
i = 0
(winW, winH) = (100, 100)
while j < 141:
	image = cv2.imread("dataset2/" + str(j) + ".jpg")
	image = imutils.resize(image, width=500, height=500)

	for (x, y, window) in sliding_window(image, stepSize=100, windowSize=(winW, winH)):
		if window.shape[0] != winH or window.shape[1] != winW:
			continue

		clone = image.copy()
		cv2.imwrite("small_bears_dataset2/picture" + str(i) + ".jpg", clone[y: y + winH, x: x + winW])
		i += 1
		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
		cv2.imshow("Window", clone)
		cv2.waitKey(1)
		time.sleep(0.3)
	j += 1

# while j < 50:
# 	image = cv2.imread("no_bears/" + str(j-35) + ".jpg")
# 	image = imutils.resize(image, width=1000, height=1000)
#
# 	for (x, y, window) in sliding_window(image, stepSize=40, windowSize=(winW, winH)):
# 		if window.shape[0] != winH or window.shape[1] != winW:
# 			continue
# 		clone = image.copy()
# 		i += 1
# 		cv2.imwrite("small_bears/picture" + str(i) + ".jpg", clone[y: y + winH, x: x + winW])
# 		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
# 		cv2.imshow("Window", clone)
# 		cv2.waitKey(1)
# 	j += 1




# image = cv2.imread("bears/"+ str(j) + ".jpg")
# image = imutils.resize(image, width=1000, height=1000)
# i = 3840
#
# for (x, y, window) in sliding_window(image, stepSize=40, windowSize=(winW, winH)):
# 	if window.shape[0] != winH or window.shape[1] != winW:
# 		continue
#
# 	clone = image.copy()
#
# 	i += 1
# 	cv2.imwrite("small_bears/picture" + str(i) + ".jpg", clone[y: y + winH, x: x + winW])
# 	cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
# 	cv2.imshow("Window", clone)
# 	cv2.waitKey(10)