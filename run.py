#!/usr/bin/env python3
import pafy
import cv2

url = 'https://www.youtube.com/watch?v=zIKxshOqlAc'
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="webm")

#start the video
cap = cv2.VideoCapture(play.url)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 1080,720)
while (True):
    ret,frame = cap.read()
    """
    your code here
    """
    try:
        cv2.imshow('image',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    except:
        break

cap.release()
cv2.destroyAllWindows()
