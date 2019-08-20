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

Firt of all let's execute the "mobilenet_test.py" script: this simple code imports all the needed libraries and initialize the pre-trained keras model and test it on a sample image. If your evironment has been correctly configured you should see something like this:
(Note that this step may that some time to process, depending on your pc and GPU configurations)
<img src="https://drive.google.com/uc?id=1N-gGAXOa3CjbYn2mM2fOfpQ-FbUjh0Au"> 

If everything is working fine, we can start with to apply the transfer learning. We want to re-train the top layers of our NN in order to recognize two different pokemon instead of the real animals. In order to do so, we need some images: for this reason I've included a script that allows you to download and store some pictures from google images.You can find the complete documentation for the package <a href="https://github.com/hardikvasa/google-images-download"> here </a>, while to run the script you need to install the module using the command 
<q> pip install google_images_download </q>



# Refrences 
- https://keras.io/applications/#mobilenet
- https://towardsdatascience.com/transfer-learning-using-mobilenet-and-keras-c75daf7ff299
- https://machinelearningmastery.com/transfer-learning-for-deep-learning/
- https://www.instructables.com/id/Transfer-Learning-With-Sipeed-MaiX-and-Arduino-IDE/
- https://www.sipeed.com/
