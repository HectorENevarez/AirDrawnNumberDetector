from AirDraw import drawImage
from tensorflow import keras
import cv2
import numpy as np
import argparse
import os

def predictNumber():
    img_array = cv2.imread("Drawnimage.png", cv2.IMREAD_GRAYSCALE)
    IMG_SIZE = 28
    new_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
    model = keras.models.load_model("Draw_Model.model")
    image_processed = new_array.reshape(1, IMG_SIZE, IMG_SIZE, -1)

    prediction = np.argmax(model.predict(image_processed), axis=-1)
    print("The predicted number is: ", int(prediction), sep='')

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--predictnumber", type=bool, default=False)
args = vars(ap.parse_args())


drawImage()

if args['predictnumber'] == True:
    predictNumber()