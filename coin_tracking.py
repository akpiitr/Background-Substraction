import cv2
import numpy as np

video = cv2.VideoCapture("Coin.mp4")

_,unresized0 = video.read()
frame1 = cv2.resize(unresized0, (720,500))

x=245
y=160
width = 130
height = 130

while True:
    term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 50, 10)

    ret, unresized = video.read()
    frame2 = cv2.resize(unresized, (720,500))

    d = cv2.absdiff(frame1,frame2)
    grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),0)
    ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate( th, np.ones((3,3), np.uint8), iterations=70)
    eroded = cv2.erode( dilated, np.ones((3,3), np.uint8), iterations=60)
    img, c, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame2, c, -1, (0,0,255),2)

    _,track_window = cv2.meanShift(eroded, (x, y, width, height), term_criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Output", frame2)
    #cv2.imshow("Output1", eroded)
        
    if cv2.waitKey(800) == 27:
        break
        
           #frame1 = frame2
           #ret, frame2 = video.read()
        
cv2.destroyAllWindows()
video.release()


