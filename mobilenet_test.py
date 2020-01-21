import numpy as np
import keras 
from keras import backend as K 
from keras.preprocessing import image
from keras.applications import imagenet_utils, MobileNet
from keras.applications.mobilenet import preprocess_input

# Importing MobileNet keras model
mobile = keras.applications.mobilenet.MobileNet()

# Image pre-processing (MobileNet accepts 224x224 images as input)

def prepare_image(file):

    img_path = './images/'
    img = image.load_img(img_path + file, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)

    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

preprocessed_image = prepare_image('German_Shepherd.jpeg')
predictions = mobile.predict(preprocessed_image)
results = imagenet_utils.decode_predictions(predictions)
print(results)