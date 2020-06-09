import cv2
import threading
import time


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

i = 0
t_end = time.time() + 60
while True:
    ret, frame = capture.read()
    frame = cv2.rectangle(frame, (120, 40), (520, 440), (0, 0, 0), 2)
    cv2.imshow("video", frame)
    
    k = cv2.waitKey(1) & 0xFF  
        
    if k == ord('n'):
        time.sleep(1)
        cv2.imwrite('C:/Users/HP NOTE/Desktop/train/5/{}.jpg'.format(i), frame)
        print("n을 누르면 저장됩니다.")
        time.sleep(2)
        i = i+1
        
    elif k == ord('q'): break


capture.release()
cv2.destroyAllWindows()