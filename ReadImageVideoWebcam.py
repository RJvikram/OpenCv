import cv2

img = cv2.imread("test.jpg")

cv2.imshow("Original", img)

cv2.waitKey(1000)