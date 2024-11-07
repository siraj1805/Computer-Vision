import cv2
import numpy as np
cap = cv2.VideoCapture('D:/Movies/Arjun_Reddy_&_40_2017&_41_720p_Telugu_Proper_HDRip_x264_MP3_900MB_ESub.mp4')
if(cap.isOpened()==False):
    print("Error ")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        if(cv2.waitKey(250)& 0xFF == ord('q')):
           break
    else:
        break
cap.release()
cv2.destroyAllWindows()
