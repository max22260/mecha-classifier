import cv2
import numpy as np
from keras.models import load_model


class Mecha_classifier():

    
    def __init__(self,model_path):
        
        self.classifier = load_model(model_path)
        self.size =150

    def predict_image(self ,image_path):
        image = cv2.imread(image_path)
        image = cv2.resize(image, (self.size, self.size), interpolation = cv2.INTER_AREA)
        image = image.astype('float32')
        image /= 255
        input_im = image
        input_im = input_im.reshape(1,150,150,3) 
        
        pred =  str(self.classifier.predict_classes(input_im, 1, verbose = 0)[0])

        if pred == "0":
            return "HBP"
        if pred == "1":
            return"cooler"
        if pred == "2":
            return"Turbo" 


    def load_image(self,image_path):
        image = cv2.imread(image_path)  
        image = cv2.resize(image, (self.size, self.size), interpolation = cv2.INTER_AREA)
        image = image.astype('float32')
        image /= 255
        image = image.reshape(1,150,150,3)
        
        return image


    def show_Image_prediction(self,name, pred, input_im):
       # imageL = cv2.resize(input_im, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
        cv2.imshow("Test Image", input_im)
        BLACK = [0,0,0]  
        expanded_image = cv2.copyMakeBorder(input_im, 0, 0, 0,imageL.shape[0] ,cv2.BORDER_CONSTANT,value=BLACK)
        #expanded_image = cv2.cvtColor(expanded_image, cv2.COLOR_GRAY2BGR)
        cv2.putText(expanded_image, str(pred), (252, 70) , cv2.FONT_HERSHEY_COMPLEX_SMALL,4, (0,255,0), 2)
        cv2.imshow(name, expanded_image)    


