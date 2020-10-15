# for Simple Image Access
# import cv2

# path = 'Lenna.png'
# img = cv2.imread(path)
# print(img)
# cv2.imshow("original", img, )
# cv2.waitKey(0)
###############################################

# for Original image accessing..!
# import cv2
#
# path = 'Lenna.png'
# img = cv2.imread(path)
#
# cv2.imshow('Original', img)
# cv2.waitKey(0)

# For Gray Image..!
# import cv2
# path = 'Lenna.png'
# img = cv2.imread(path)
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('Gray Image..!', img)
# cv2.waitKey(0)

import cv2
path = "Lenna.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY, 0)
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
print(imgBlur)
cv2.imshow("Blur Image..!", imgBlur)
cv2.waitKey(0)