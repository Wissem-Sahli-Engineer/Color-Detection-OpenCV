# pyrefly: ignore [missing-import]
import cv2

webcam = cv2.VideoCapture(0)

while True :

    ret , frame = webcam.read()

    frame = cv2.flip(frame, 1)  # invert Y-Axis (MIRROR EFFECT)

    cv2.imshow('Live color detecor',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.desctroyAllwindows()