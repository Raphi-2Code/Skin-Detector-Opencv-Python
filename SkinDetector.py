import cv2 #install it via pip install opencv-python command (extra modules: pip install opencv-python-contrib)
import numpy as np
cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    into_hsv = cv2.cvtColor(frame, cv2.COLOR_LAB2RGB)
    L_limit = np.array([0, 0, 0])
    U_limit = np.array([140, 100, 100])
    b_mask = cv2.inRange(into_hsv, L_limit, U_limit)
    blue = cv2.bitwise_and(frame, frame, mask=b_mask)
    cv2.imshow('Original', frame)
    cv2.imshow('Skin Detector', blue)
    if cv2.waitKey(1) == 27:
        break
cap.release()

cv2.destroyAllWindows()
