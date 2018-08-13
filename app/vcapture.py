import cv2
import sys, pygame, time
from pygame.locals import *
from PIL import ImageEnhance, ImageDraw


cap = cv2.VideoCapture(0)

while True:
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()