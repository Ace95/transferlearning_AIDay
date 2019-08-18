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

# Example 1: TL applied on MobileNet to train a custom model for the MaixPy AI board
For the first example we are going to re-train a MobileNet in order to obtain a real pokedex that can recognize Pikachu and Charizard insted of real animals. I decided to use this type of CNN because it's the most suitable for mabile and IoT applications. More informations about MobileNets can be found in the paper folder, while the NNs available through Keras can be found <a href="https://keras.io/applications/#mobilenet"> here </a>.

<div style="text-align: middle"> 
<img src="https://www.diregiovani.it/wp-content/uploads/2016/07/pokemon-go-list.jpg"> 
</div>

# Refrences 
- https://keras.io/applications/#mobilenet
- https://towardsdatascience.com/transfer-learning-using-mobilenet-and-keras-c75daf7ff299
- https://machinelearningmastery.com/transfer-learning-for-deep-learning/
- https://www.instructables.com/id/Transfer-Learning-With-Sipeed-MaiX-and-Arduino-IDE/
- https://www.sipeed.com/
