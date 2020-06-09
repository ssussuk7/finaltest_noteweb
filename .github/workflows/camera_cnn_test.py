import cv2
import threading
import time
import os, re, glob
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2


categories = ["0","1","2","3","4","5","6","7","8","9",
              "10","11","12","13","14","15","16","17","18","19","20","21","22","23",
              "24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]

categories_id = ["0","1","2","3","4","5","6","7","8","9",
                 "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
                 "ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ","ㅐ","ㅒ","ㅔ","ㅖ","ㅚ","ㅟ","ㅢ"]

categories_number = ["0","1","2","3","4","5","6","7","8","9"] #숫자 array (0 ~ 9)
categories_consonant = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"] #자음 array ( 10 ~ 23)
categoires_vowel = ["ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ","ㅐ","ㅒ","ㅔ","ㅖ","ㅚ","ㅟ","ㅢ"] #모음 array (24 ~ 40)


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def Dataization(img_path):
    image_w = 28
    image_h = 28
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)
 

test = []
test_output = []
image_dir = 'C:/Users/HP NOTE/Desktop/train/test/'
i = 0
num = 0
model = load_model('C:/Users/HP NOTE/Desktop/train/Gersang.h5')

blackboard_width = 400
blackboard_height = 600
text_x_title = 30
text_x_exp = 30
text_x_main = 30
text_y_title = 30
text_y_exp = 60
text_y_main = 90

img = np.zeros((400,800,3),np.uint8)
#step1 화면 띄우기

while True:
    ret, frame = capture.read()
    frame = cv2.rectangle(frame, (120, 40), (520, 440), (255, 255, 255), 2)
    
    cv2.imwrite('C:/Users/HP NOTE/Desktop/train/test/test_{}.jpg'.format(i), frame)
    src = cv2.imread('C:/Users/HP NOTE/Desktop/train/test/test_{}.jpg'.format(i), cv2.IMREAD_COLOR)
    
    dst = src.copy()
    cut = dst[40:440, 120:520]
    cv2.imwrite('C:/Users/HP NOTE/Desktop/train/test/test_{}.jpg'.format(i), cut)
    
    test.append(Dataization('C:/Users/HP NOTE/Desktop/train/test/test_{}.jpg'.format(i)))
    test = np.array(test)
    predict = model.predict_classes(test)
    
    
    cv2.imshow("video", frame)


    b,g,r,a = 255,255,255,0
    fontpath = "C:/Users/HP NOTE/Desktop/train/Cafe24Shiningstar.ttf"
    font = ImageFont.truetype(fontpath, 30)
    font_predict= ImageFont.truetype(fontpath, 50)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((text_x_title, text_y_title),  "네모 박스 안에 번역하고자하는 수화를 입력하세요 !", font=font, fill=(b,g,r,a))
    draw.text((text_x_exp, text_y_exp),  "1.=숫자 / 2=자음 / 3=모음 / 4=단어 / n=기록 / r = 리셋/ x = 다음 줄 / q = 종료", font=font, fill=(b,g,r,a))
    img = np.array(img_pil)

    cv2.imshow("res", img)
    
    predict_black = np.zeros((200,300,3), np.uint8)
    img_pil_pre = Image.fromarray(predict_black)
    draw_pre = ImageDraw.Draw(img_pil_pre)
    draw_pre.text((80,80),  'Predict :' + str(categories_id[predict[num]]), font=font_predict, fill=(b,g,r,a))
    predict_black = np.array(img_pil_pre)
    
    cv2.imshow("Predict", predict_black)    
    
 
    test = []
    i = i+1
    
    k = cv2.waitKey(1) & 0xFF  
    if i == 5 :
        i = 0
        
    if k == ord('1'): #숫자
        categories_id = []
        categories_id= categories_number.copy()
        model = 0
        model = load_model('C:/Users/HP NOTE/Desktop/train/model_number.h5')
        
    if k == ord('2'): #자음
        categories_id = []
        categories_id = categories_consonant.copy()       
        model = 0
        model = load_model('C:/Users/HP NOTE/Desktop/train/model_consonant.h5')
        
    if k == ord('3'): #모음
        model = load_model('C:/Users/HP NOTE/Desktop/train/Gersang.h5')
        
    
    if k == ord('n'):
        data = str(categories_id[predict[0]])
        draw.text((text_x_main, text_y_main), data , font=font, fill=(b,g,r,a)) #기록하기
        img = np.array(img_pil)
        text_x_main = text_x_main + 30
        
             
    if k == ord('x'):
        text_x_main = 30
        text_y_main = text_y_main + 30 #한 줄 띄우기(엔터)
        img = np.array(img_pil)
    
    if k == ord('r'):
        img = np.zeros((blackboard_width, blackboard_height,3),np.uint8)
        text_x_main = 30
        text_y_main = 90
        
    
    if k == ord('q'): break

   
capture.release()
cv2.destroyAllWindows()