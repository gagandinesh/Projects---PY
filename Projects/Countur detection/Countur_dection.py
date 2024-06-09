# import openCV
# import numpy

import cv2

img = cv2.imread("C:\Python(pract)\Projects\Countur detection\Teng.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# to find the threshold

ret, thresh = cv2.threshold(imgray, 127, 255, 0)

# to find the Counturs
Contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours =" + str(len(Contours)))
print(Contours[0])

# to join all the conturs
# in this -1(all the Countres ),and 3 is the (thickness)
cv2.drawContours(img, Contours, 5, (0, 255, 0), 3)


cv2.imshow("image", img)
cv2.imshow("image_gray", imgray)
cv2.waitKey(0)
cv2.destroyAllWindows
