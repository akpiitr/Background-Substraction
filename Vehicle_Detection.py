import cv2
import numpy as np

def nothing(x):
    pass

def main():
    w_1 = 800
    h_1 = 600

    cap = cv2.VideoCapture('data.mp4')

    cap.set(3,w_1)
    cap.set(4,h_1)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = false

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    #sub =cv2.createBackgroundSubtractorMOG2()
    
    while ret:
        
        #diff = sub.apply(frame1)
        diff = cv2.absdiff(frame1,frame2)
        #diff[0:400,0:1100] = [0,0,0]
        #diff[550:720,0:2100] = [0,0,0]
        cv2.imshow("diff", diff)
        grey = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        #grey[grey==127]=0
        #cv2.imshow("diff", grey)
        blur = cv2.GaussianBlur(grey,(5,5),0)
        #cv2.imshow("diff", blur)
        ret, th = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)
        #cv2.imshow("diff", th)
        dilated = cv2.dilate( th, np.ones((3,3), np.uint8), iterations=10)
        eroded = cv2.erode( dilated, np.ones((3,3), np.uint8), iterations=11)
        #cv2.imshow("eroded", eroded)

        overlay = frame1.copy()
        cv2.rectangle(overlay,(0,400),(2100,550),(0,252,124),-1)
        opacity = 0.4
        cv2.addWeighted(overlay, opacity, frame1, 1 - opacity, 0, frame1)
        
        img, contours, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.putText(frame1,'No. of Vehicle Detected =',(10,40),0,1.5,(0,0,0))
        for pass_contour in contours:
            area = cv2.contourArea(pass_contour)

            if area > 3000:
                #cv2.drawContours(frame1, pass_contour, -1, (0,255,255),2)
             
                rect = cv2.boundingRect(pass_contour)
                
                if rect[2] < 2 and rect[3] < 2:
                    continue
                x,y,w,h = rect
                cv2.rectangle(frame1,(x,y),(x+w-30,y+h-30),(0,255,0),2)
                pt_x= round(x+w/2-20)
                pt_y= round(y+h/2-20)
                cv2.circle(frame1,(pt_x,pt_y), 3, (0,0,255), -1)
                cv2.putText(frame1,'Vehicle Detected',(x,y-6),0,0.5,(0,255,0))
                
        #for c in contours:
           # rect = cv2.boundingRect(c)
            #if rect[2] < 100 or rect[3] < 100:
            #    continue
           # print (cv2.contourArea(c))
            #x,y,w,h = rect
            #cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.putText(frame1,'Moth Detected',(x+w+10,y+h),0,0.3,(0,255,0))
        
        #cv2.imshow("Original", frame2)
        #cv2.imshow("Output", frame1)
        
        if cv2.waitKey(20) ==27:
            break

        frame1 = frame2
        ret, frame2 = cap.read()
        
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()
