import cv2
import threading
import time

categories = ["0","1","2","3","4","5","6","7","8","9",
              "10","11","12","13","14","15","16","17","18","19","20","21","22","23",
              "24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]

categories_id = ["0","1","2","3","4","5","6","7","8","9",
                 "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
                 "ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ","ㅐ","ㅒ","ㅔ","ㅖ","ㅚ","ㅟ","ㅢ"]


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

i = 4
num = 10
t_end = time.time() + 60
while True:
    ret, frame = capture.read()
    frame = cv2.rectangle(frame, (120, 40), (520, 440), (255, 255, 255), 2)
    cv2.imshow("video", frame)
    
    k = cv2.waitKey(1) & 0xFF  
        
    if k == ord('n'):
        time.sleep(2)
        cv2.imwrite('C:/Users/HP NOTE/Desktop/train/{}/{}.jpg'.format(num, i), frame)
        src = cv2.imread('C:/Users/HP NOTE/Desktop/train/{}/{}.jpg'.format(num, i), cv2.IMREAD_COLOR)
        dst = src.copy()
        cut = dst[40:440, 120:520]
        cv2.imwrite('C:/Users/HP NOTE/Desktop/train/{}/{}.jpg'.format(num, i), cut)
        print('{}/{}.jpg 저장완료'.format(categories_id[num], i))
        i = i+1
        if i == 6 :
            i = 4
            print('{}로 넘어갑니다.'.format(categories_id[num +1]))
            num = num+1
        
    elif k == ord('q'): break


capture.release()
cv2.destroyAllWindows()