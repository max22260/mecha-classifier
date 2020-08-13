from mecha_classifier import Mecha_classifier

model =  Mecha_classifier('Trained Models/model_V3.h5')

name = model.predict_image("DataSet/Cooler84.jpg")
image = model.load_image("DataSet/Cooler84.jpg")

#model.show_Image_prediction(name="cooler",pred=name,input_im=image)

print("the prediction name : "+ name)