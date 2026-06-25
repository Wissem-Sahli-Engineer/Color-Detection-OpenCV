# pyrefly: ignore [missing-import]
import cv2
from utils import get_limits
# pyrefly: ignore [missing-import]
from PIL import Image


webcam = cv2.VideoCapture(0)

while True :

    ret , frame = webcam.read()
    frame = cv2.flip(frame, 1)  # invert Y-Axis (MIRROR EFFECT)

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color Selection - Detect green color
    green = [0, 255, 0] 

    lowerLimit , upperLimit = get_limits( color = green)
    mask = cv2.inRange( hsvImg , lowerLimit , upperLimit)

    # Bounding Box
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0),5)

    cv2.imshow('Live color detecor',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()