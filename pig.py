from itertools import count
import numpy as np
import cv2 as cv

count = 105
cap = cv.VideoCapture('C:/Users/user/Documents/GraduationProject/videos/tobepork.mp4')
success = True

while success:
    cap.set(cv.CAP_PROP_POS_MSEC,((count - 105)*1000))
    success, image = cap.read()
    print('Read a new frame: ', success)
    cv.imwrite('C:/Users/user/Documents/GraduationProject/Img/tobepork/frame%d.jpg' %count, image)
    count += 1

cap.release()
cv.destroyAllWindows()
