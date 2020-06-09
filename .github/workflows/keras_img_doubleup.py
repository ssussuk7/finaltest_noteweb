import numpy as np
from numpy import expand_dims
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import cv2
 
categories = ["0","1","2","3","4","5","6","7","8","9",
              "10","11","12","13","14","15","16","17","18","19","20","21","22","23",
              "24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]

categories_id = ["0","1","2","3","4","5","6","7","8","9",
                 "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
                 "ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ","ㅐ","ㅒ","ㅔ","ㅖ","ㅚ","ㅟ","ㅢ"]
 
np.random.seed(3)
 
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
 
 
data_datagen = ImageDataGenerator(rescale=1./255)
 
data_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=20, 
                                   shear_range=5.5,  
                                   width_shift_range=0.1,
                                   height_shift_range=0.1,
                                   zoom_range=0.5,
                                   horizontal_flip=True,
                                   vertical_flip=False,
                                   fill_mode='nearest') 
'''
rotation_ range = 회전율
shear_range = 밀림강도
width _shift_range = 수평방향 이동
height_shift _range = 수직방향 이동
zoom_range = 확대/축소
horizontal_flip = 수평방향 뒤집기
vertical_flip = 수직방향 뒤집기
'''

folder = 10
num = 4

while True:
    img = load_img('C:/Users/HP NOTE/Desktop/train/{}/{}.jpg'.format(folder,num))
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in data_datagen.flow(x, batch_size=1, save_to_dir='C:/Users/HP NOTE/Desktop/train/{}/'.format(folder), save_format='jpg', save_prefix=num):
        i += 1
        if i > 30:
            num = num + 1
            if num == 6:
                num = 0
                folder = folder + 1
                print('{} 로 넘어갑니다.'.format(categories_id[folder]))
            break
    if folder == 24:break
    
print("finish !!")
