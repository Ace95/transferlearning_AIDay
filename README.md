# Transfer Learning: Adapting Models for Custom Applications
This repository contains the main arguments and papers with some useful links used in the homonymous session during the 2019 AI Day in Rome promoted by Microsoft and organized by the local .Net community. If you would like to improve this repo with more exemples, cases or papers; please feel free to post your opinions or to contact me.

For the practical example I re-trained a MobileNet NN and converted it into a kmodel for the Sipeed MaixPy AI Board. You can buy the board for about 20€, but I'm open to implement new examples on different devices (I'm also working on the Nvidia JatsonNano and the Raspberry Pi 3)

# Set up your environment 
We need to set up a linux system for the conversion from keras model to kmodel supported by the MaixPy. I Recommend Ubuntu 16+ (you can also run it on a virtual machine). Once the machine is ready, we install <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html"> Miniconda </a>. After that we have to run the following commands


``` bashrc
$ conda create -n ml python=3.6 tensorflow=1.12 keras pillow numpy
$ conda activate ml
```
NOTE - Linux is only needed for the final part, you can run all the other scrips in any OS with python and tensorflow installed.

# Why should you use transfer learning?
- Difficulties in the creation of the datasets
- Lack of computational power 
- Faster training
- Possibility to obtain better results 

# Example 1: Sipeed MaixPy Bit AI board
For the first example, we are going to re-train a MobileNet in order to obtain a real-life pokedex that can recognize Pikachu and Charizard instead of actual animals. I decided to use this type of CNN because it's the most suitable for mobile and IoT applications. More informations about MobileNets can be found in the paper folder, while the NNs available through Keras can be found <a href="https://keras.io/applications/#mobilenet"> here </a>.
<ul>
  <li><b> Test the mobilenet </b></li>
  
First of all let's execute the "mobilenet_test.py" script: this simple code imports all the needed libraries and the pre-trained keras model to test it on a sample image. If your environment has been correctly configured you should see something like this:

(Note that this step may take some time depending on your pc and GPU configurations)

<img src="https://drive.google.com/uc?id=1rhcL-7tAdnWJt4Bow6j8EmB5f4-POtvY"> 

<li><b> Prepare your dataset </b></li>

If everything is working fine, we can start to apply the transfer learning. We want to re-train the top layers of our NN in order to recognize two different pokemon instead of real animals. In order to do so, we need some images: for this reason I've included a script that allows you to download and store some pictures from google images. You can find the complete documentation for the package <a href="https://github.com/hardikvasa/google-images-download"> here </a>, while to run the script you need to install the module using the command 

``` bashrc
$ pip install google_images_download 
```
Now we are ready to run the "TL_mobilenet.py" script.


<li><b> Re-train the top layers and save your new model </b></li>

Let's give a look at the re-training script included in this repo. After importing all the modules, we initialize the starting model: the code has been set up to use the MobileNet NN provided in Keras without the top layer - the top layer is the one responsible for the final classification, so we can take advantage of pre-trained weights obtained on the ImageNet dataset while we are going to classify our custom objects. In order to do so, we need to define a new top for our NN by creating some layers to use as top, including a dropout layer to prevent overfitting. 

```
x = starting_model.output 
x = GlobalAveragePooling2D()(x)
x = Dense (1024,activation='relu')(x)
x = Dropout(0.5)(x) 
x = Dense (1024,activation='relu')(x)
x = Dense (512,activation='relu')(x)
preds = Dense(2,activation='softmax')(x)
model = Model(inputs=starting_model.input,outputs=preds)
```

Note that number of neurons in the last layer, "preds", depends on the number of classes you want to detect.
After doing that we set the all the layers but the top ones as non-trainable and finally we can re-train our top layers and save our model as "new_pokemon_model.h5".


```
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
```

<li><b> Test your new model </b></li>

The last script,"test_newmodels.py", is very similar to the first one used to test the mobilenet but this time the new pokemon model is loaded and tested on an image. If everything is working fine you should see a window opening with an image and a probability score, like this :


<img src="https://drive.google.com/uc?id=1rhcL-7tAdnWJt4Bow6j8EmB5f4-POtvY">


<li><b>Convert Keras model to kmodel </b></li>
the last step we need to complete is the conversion of our keras model (saved in the format .h5) into a kmodel, the type of NN that the MaixPy Bit board supports. In order to do so, we need to set up linux machine. I personally recommend using <a href="https://www.ubuntu-it.org/download"> Ubuntu16+ </a>, but you shouldn't find any difficulties with other Linux releases. Once the machine is ready, virtual or not, we need to clone the <a href="https://github.com/sipeed/Maix_Toolbox"> Maix toolbox repository </a>.

```bashrc
$ git clone https://github.com/sipeed/Maix_Toolbox <directory>
```
Now we are ready to convert our model. First we need to convert the keras model in a tflite model, then we can convert the tflite model into the final kmodel using the tool provided by Sipeed.

```bashrc
$ tflite_convert  --output_file=poke_model.tflite --keras_model_file=new_pokemon_model.h5
$ ./tflite2kmodel.sh poke_model.tflite
```

<li><b>Final result </b></li>
After flashing the obtained model and the "detect.py" on an SD card and uploaded the MaixPy firmware on the board, we should be able to run our model on the board. The final result should be something similar to this:

<img src="https://drive.google.com/uc?id=1D7Su34vobOd8kwXlRReE_QiAcJAzfM-M">

</ul>


# Example 2: Transfer Learning with ML.NET

During the past year I got some occasions to re-present my session in different conferences and during these I've been aske many times how you could implement this kind of application in the .NET framework. The answer? Simply by using ML.NET! The new ML and AI dedicate Microsoft framework for the .NET world. You can find <a href="https://github.com/dotnet/machinelearning-samples/tree/master/samples/csharp/getting-started/DeepLearning_ImageClassification_TensorFlow"> here </a> the step-by-step guided on how to implement a pre-trained TensorFlow model in a .NET application for Image Classification. (Note: I'm not goint to copy-paste their work here, so just check out the official Microsoft repository and ask there for any issue you may found!). If yuo would like to try this out, you need:

  - Visual Studio 2017+
  - ML.NET extention 
  - A bit of knowledge of C#


# References 
- https://keras.io/applications/#mobilenet
- https://towardsdatascience.com/transfer-learning-using-mobilenet-and-keras-c75daf7ff299
- https://machinelearningmastery.com/transfer-learning-for-deep-learning/
- https://www.instructables.com/id/Transfer-Learning-With-Sipeed-MaiX-and-Arduino-IDE/
- https://www.sipeed.com/
- https://github.com/dotnet/machinelearning-samples/tree/master/samples/csharp/getting-started/DeepLearning_ImageClassification_TensorFlow
