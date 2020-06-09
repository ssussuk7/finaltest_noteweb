from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.models import load_model
import cv2
import numpy as np
 
'''
categories = ["0","1","2","3","4","5","6","7","8","9",
              "10","11","12","13","14","15","16","17","18","19","20","21","22","23",
              "24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]

categories_id = ["0","1","2","3","4","5","6","7","8","9",
                 "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
                 "ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ","ㅐ","ㅒ","ㅔ","ㅖ","ㅚ","ㅟ","ㅢ"]
'''

X_train, X_test, Y_train, Y_test = np.load("C:/Users/HP NOTE/Desktop/train/model_consonant.npy")
categories = ["10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
 
num_classes = len(categories)
 
model = Sequential()
model = Sequential()
model.add(Convolution2D(16, 3, 3, border_mode='same', activation='relu',
                        input_shape=X_train.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Convolution2D(64, 3, 3,  activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
 
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation = 'softmax'))

model.summary()
model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=32, nb_epoch=1)
 
model.save('C:/Users/HP NOTE/Desktop/train/model_consonant.h5')