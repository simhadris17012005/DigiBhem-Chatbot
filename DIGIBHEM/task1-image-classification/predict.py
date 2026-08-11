"""
Task-1: Image Classification Project
Load the trained model and predict a single image.

Usage:
    python predict.py path/to/image.jpg
"""

import sys
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck",
]


def predict(image_path, model_path="image_classifier_model.h5"):
    model = tf.keras.models.load_model(model_path)

    img = image.load_img(image_path, target_size=(32, 32))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = float(np.max(predictions))

    print(f"Predicted class: {predicted_class} ({confidence * 100:.2f}% confidence)")
    return predicted_class, confidence


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py path/to/image.jpg")
        sys.exit(1)
    predict(sys.argv[1])
