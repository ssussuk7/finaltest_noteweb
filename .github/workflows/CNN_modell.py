import os, re, glob
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

'''
categories = ["0","1","2","3","4","5","6","7","8","9",
              "10","11","12","13","14","15","16","17","18","19","20","21","22","23",
              "24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]

categories_id = ["0","1","2","3","4","5","6","7","8","9",
                 "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
                 "ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ","ㅐ","ㅒ","ㅔ","ㅖ","ㅚ","ㅟ","ㅢ"]
'''
  
groups_folder_path = 'C:/Users/HP NOTE/Desktop/train/'
categories = ["10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
 
num_classes = len(categories)
  
image_w = 28
image_h = 28
  
X = []
Y = []
  
for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/'
  
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            print(image_dir+filename)
            img = cv2.imread(image_dir+filename)
            img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
            X.append(img/256)
            Y.append(label)
 
X = np.array(X)
Y = np.array(Y)
 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)

print(X_train.shape)
print(Y_train[:10])
print(X_test.shape)
np.save("C:/Users/HP NOTE/Desktop/train/model_consonant.npy", xy)
