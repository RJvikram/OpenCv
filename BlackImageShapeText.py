import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[:] = 0, 0, 0
print(img)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 2)
# for Rectangle
cv2.rectangle(img, (350, 163), (450, 250), (0, 0, 255), cv2.FILLED)
cv2.rectangle(img, (16, 165), (150, 256), (0, 0, 255), 5)

cv2.circle(img, (100, 430), 50, (0, 250, 0), cv2.FILLED)
cv2.circle(img, (250, 430), 50, (0, 250, 0), 2)

cv2.putText(img, "Welcome To Machine learning", (30, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (250, 250, 250), 1)
print(img.shape)

cv2.imshow("self Image..!", img)
cv2.waitKey(0)