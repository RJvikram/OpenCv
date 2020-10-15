import cv2

path = "test.jpg"

img = cv2.imread(path)
print(img.shape)
cv2.imshow("Cropped", img)
width, height = 300, 400
reSizeImg = cv2.resize(img, (width, height), 0)
print(reSizeImg.shape)
imgCropped = img[99:530, 175:820]
reSizing = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))

cv2.imshow("ResizeImage", reSizeImg)
cv2.imshow("Cropped Image", imgCropped)
cv2.imshow("resize", reSizing)
cv2.waitKey(0)