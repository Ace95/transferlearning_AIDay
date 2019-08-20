# Transfer Learning: Adapting Models for Custom Applications
This repository contains the main arguments and papers with some usefull links used in the homonymous session during the 2019 AI Day in Rome promoted by Microsoft and organized by the local .Net community. If you wold like to improve this repo with more exemples, cases or papers; please feel free to post your opinions or to contact me.

For the practical exemple I re-trained a MobileNet NN and converted it into a kmodel for the Sipeed MaixPy AI Board. You can buy the board for about 20€, but I'm open to implement new examples on different devices (I'm also working on the Nvidia JatsonNano and the Raspeberry Pi)

# Environment requirements
- Linux system for the conversion from keras model to kmodel supported by the MaixPy. I Recommend Ubutu 16+(you can also run it on a virtual machine)
- Python 3.5+
- Latest TensorFlow and Keras for Python releases 

# Why do you should use transfer learning?
- Difficulties in the creation of the datasets
- Lack of computational power 
- Faster training
- Possibility to obtain better results 

# Example 1: Sipeed MaixPy Bit AI board
For the first example we are going to re-train a MobileNet in order to obtain a real pokedex that can recognize Pikachu and Charizard insted of real animals. I decided to use this type of CNN because it's the most suitable for mabile and IoT applications. More informations about MobileNets can be found in the paper folder, while the NNs available through Keras can be found <a href="https://keras.io/applications/#mobilenet"> here </a>.
<ul>
  <li> Test the mobilenet </li>
  
Firt of all let's execute the "mobilenet_test.py" script: this simple code imports all the needed libraries and initialize the pre-    trained keras model and test it on a sample image. If your evironment has been correctly configured you should see something like this:

(Note that this step may take some time depending on your pc and GPU configurations)

<img src="https://drive.google.com/uc?id=1N-gGAXOa3CjbYn2mM2fOfpQ-FbUjh0Au"> 


<li> Preprare your dataset </li>

If everything is working fine, we can start to apply the transfer learning. We want to re-train the top layers of our NN in order to recognize two different pokemon instead of real animals. In order to do so, we need some images: for this reason I've included a script that allows you to download and store some pictures from google images. You can find the complete documentation for the package <a href="https://github.com/hardikvasa/google-images-download"> here </a>, while to run the script you need to install the module using the command <q> pip install google_images_download </q>. Now we are ready to run the "TL_mobilenet.py" script.


<li> Re-train the top layers and save your new model </li>

Let's give a look at the re-training script include in this repo. After importing all the modules, we initialize the starting model: the code has been set up to use the MobileNet NN provided in Keras without the top layer - the top layer is the one responsable for the final classification, so in this way we can take adavantage of pre-trained weights obtained on the ImageNet dataset while we will classify our custom objects. Now we need to define a new top for our NN, so we create some layers to use as top, including a dropout layer to prevent overfitting. (Note that number of neurons in the last layer, "preds", depends on the number of classes you want to detect!). After doing that we set the all the layers but the top ones as non-trainable and finally we can re-train our top layers and save our model as "new_pokemon_model.h5".


<li> Test your new model </li>

The last script,"test_newmodels.py", is very similar to the first one used to test the mobilenet but this time the new pokemon model is load and tested on a random image. If everything is working fine you should see a window opening with an image and a probability score, like this :


<img src="https://drive.google.com/uc?id=1rhcL-7tAdnWJt4Bow6j8EmB5f4-POtvY">
</ul>


# Refrences 
- https://keras.io/applications/#mobilenet
- https://towardsdatascience.com/transfer-learning-using-mobilenet-and-keras-c75daf7ff299
- https://machinelearningmastery.com/transfer-learning-for-deep-learning/
- https://www.instructables.com/id/Transfer-Learning-With-Sipeed-MaiX-and-Arduino-IDE/
- https://www.sipeed.com/
