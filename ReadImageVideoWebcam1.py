import cv2

frameWidth = 640
frameHeight = 100

cap = cv2.VideoCapture("test1.webm")

# cap.set(2, frameWidth)
# cap.set(3, frameHeight)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break