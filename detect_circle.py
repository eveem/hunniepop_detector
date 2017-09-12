import cv2
import numpy as np

inner_blue = np.array([205, 138, 56])
outer_blue = np.array([163, 93, 18])

inner_purple = np.array([220, 217, 118])
outer_purple = np.array([206, 192, 95])

inner_yellow = np.array([91, 200, 229])
outer_yellow = np.array([103, 196, 207])

inner_pink = np.array([56, 73, 225])
outer_pink = np.array([48, 48, 187])

inner_green = np.array([93, 202, 167])
outer_green = np.array([54, 184, 133])

inner_lblue = np.array([200, 73, 160])
outer_lblue = np.array([216, 113, 190])

inner_orange = np.array([93, 202, 167])
outer_orange = np.array([67, 179, 134])

inner_red = np.array([83, 92, 236])
outer_red = np.array([58, 58, 191])

img = cv2.imread('ex2.png', 0)

cimg = cv2.imread('ex2.png')

# hsv = cv2.cvtColor(cimg, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(cimg, outer_green, inner_green)
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