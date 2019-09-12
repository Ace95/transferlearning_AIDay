import numpy as np
import keras 
from keras import backend as K 
from keras.preprocessing import image
from keras.models import load_model
import cv2

# Image pre-processing (MobileNet accepts 224x224 images as input)
labels = ['charizard', 'pikachu']

def prepare_image(file):

    img_path = './images/'
    img = image.load_img(img_path + file, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)

    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

model = load_model('./models/new_model_pokemon.h5')
preprocessed_image = prepare_image('/charizard/2.61IbcCuJ3sL._SX425_.jpg')
predictions = model.predict(preprocessed_image)

if predictions[0][0] > predictions[0][1]:
    text = 'Charizard: ' + str(predictions[0][0])
    poke = cv2.imread('./images/charizard.jpeg')
    cv2.imshow(text,poke)
    cv2.waitKey()
else:
    text = 'Pikachu: ' + str(predictions[0][1])
    poke = cv2.imread('./images/pikachu.jpeg')
    cv2.imshow(text,poke)
    cv2.waitKey()