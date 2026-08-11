# Task-1: Image Classification Project

AI/ML Internship Task — Digital Bhem

## Overview
Trains a Convolutional Neural Network (CNN) to classify images from the
CIFAR-10 dataset (10 classes: airplane, automobile, bird, cat, deer, dog,
frog, horse, ship, truck).

## Tech Stack
- TensorFlow / Keras
- CIFAR-10 dataset (built into `tensorflow.keras.datasets`)

## Setup
```bash
pip install -r requirements.txt
```

## Train
```bash
python train.py
```
This trains the CNN for 10 epochs, prints test accuracy, saves the model as
`image_classifier_model.h5`, and saves an accuracy plot as
`training_accuracy.png`.

## Predict
```bash
python predict.py path/to/image.jpg
```

## Results
Update this section with your final test accuracy once training completes.

## Credits
- Dataset: CIFAR-10 (https://www.cs.toronto.edu/~kriz/cifar.html)
- Reference: https://www.tensorflow.org/tutorials/images/classification
