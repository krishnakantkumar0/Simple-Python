import numpy as np
import cv2

cap = capture =cv2.VideoCapture('C2.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
