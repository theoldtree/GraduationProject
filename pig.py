from itertools import count
import numpy as np
import cv2 as cv

count=0
cap = cv.VideoCapture('./videos/hallway.mp4')
success = True

while success:
    cap.set(cv.CAP_PROP_POS_MSEC,(count*1000))
    success, image = cap.read()
    print('Read a new frame: ', success)
    cv.imwrite('./Img/hallway/frame%d.jpg' %count, image)
    count += 1

cap.release()
cv.destroyAllWindows()