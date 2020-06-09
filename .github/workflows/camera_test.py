import argparse
import datetime
import time
import cv2
import numpy as np
import copy

#3 frame당 한 번씩 모션체크


ap = argparse.ArgumentParser()
ap.add_argument("-v","--video", help="path to the videio file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

count = 0

if args.get("video", None) is None:
    camera = cv2.VideoCapture(0)
    
    time.sleep(0.25)
    camera.set(cv2.CAP_PROP_FPS, 15)
    
else:
    camera = cv2.VideoCapture(args["video"])
    

firstFrame = None

while True:
    count = count + 1
    (grabbed, frame) = camera.read()
    text = "Unoccupied"
    
    if not grabbed:
        break
    
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    
    fps = camera.get(cv2.CAP_PROP_FPS)
    print(fps)
    
    if firstFrame is None:
        firstFrame = gray
        continue
    
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts, _) = cv2.findContours(copy.copy(thresh), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    count2 = 0
    texted = 'ㄱ'
    if (count % 5 == 0):
        for c in cnts:
            count2 = count2 + 1
            if cv2.contourArea(c) < args["min_area"]:
                continue
            
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0 , 255, 0), 2)
            img_trim = frame[y:y + h, x: x + w]
            cv2.imwrite("C:/Users/HP NOTE/.spyder-py3/test/test_images/text1_%d.jpg" %(count), img_trim)
            text = "Occupied"
            
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I: %M: %S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF #'q' 누르면 quit
    
    if key == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()
    
