import numpy as np
import keras 
from keras import backend as K 
from keras.layers.core import Dense, Activation, Dropout
from keras.optimizers import Adam 
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.applications import imagenet_utils, MobileNet
from keras.applications.mobilenet import preprocess_input

# Applying TranserLearning, we freeze the base layer and retrain the one o nthe top

starting_model = MobileNet(weights="imagenet",include_top=False) # this line imports the mobilenet model trained on imagenet dataset and discard the last 1000 neurons layer 

x = starting_model.output 
x = GlobalAveragePooling2D()(x)
x = Dense (1024,activation='relu')(x)
x = Dropout(0.5)(x) 
x = Dense (1024,activation='relu')(x)
x = Dense (512,activation='relu')(x)
preds = Dense(2,activation='softmax')(x)  # Note that number of neurons in the last layer depends on the number of classes you want to detect
model = Model(inputs=starting_model.input,outputs=preds)

# We want to use the pre-trained weights, only the last 20 layers will be re-trained 

for layer in model.layers[:20]:
    layer.trainable = False

for  layer in model.layers[20:]:
    layer.trainable = True   

train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
train_generator = train_datagen.flow_from_directory('./images',
                                                    target_size=(224,224),
                                                    color_mode='rgb',
                                                    batch_size = 32,
                                                    class_mode = 'categorical',
                                                    shuffle= True)

# Lets re-traing the top layers, this step may require some time depending on yor PC/GPU 

model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])
step_size_train = train_generator.n//train_generator.batch_size
model.fit_generator(generator=train_generator,steps_per_epoch=step_size_train,epochs=10)

model.save('./models/new_model_pokemon.h5')


