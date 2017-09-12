import cv2
import numpy as np

lower_blue = np.array([205, 138, 56])
upper_blue = np.array([163, 93, 18])

lower_lblue = np.array([206, 192, 95])
upper_lblue = np.array([220, 217, 118])

# inner_yellow = np.array([91, 200, 229])
# outer_yellow = np.array([103, 196, 207])

lower_green = np.array([54, 184, 133])
upper_green = np.array([93, 202, 167])

# lower_orange = np.array([80, 97, 232])
# upper_orange = np.array([92, 92, 205])

upper_red = np.array([83, 92, 236])
lower_red = np.array([58, 58, 191])

lower_pink = np.array([158, 62, 203])
upper_pink = np.array([196, 120, 237])

img = cv2.imread('ex2.png', 0)

cimg = cv2.imread('ex2.png')

# hsv = cv2.cvtColor(cimg, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(cimg, lower_orange, upper_orange)
res = cv2.bitwise_and(cimg, cimg, mask= mask)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, np.array([]), 1, 73, 20, 50)
circles = np.uint16 (np.around (circles))

for i in circles [0, :]:
	cv2.circle(cimg, (i[0], i[1]), i[2], (0, 0, 0), 3)
	cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()