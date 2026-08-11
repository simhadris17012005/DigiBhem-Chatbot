"""
Task-1: Image Classification Project
Digital Bhem AI/ML Internship

Trains a CNN on CIFAR-10 using TensorFlow/Keras.
"""

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt


def load_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)


def build_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ])
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def plot_history(history):
    plt.plot(history.history["accuracy"], label="train_accuracy")
    plt.plot(history.history["val_accuracy"], label="val_accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend(loc="lower right")
    plt.savefig("training_accuracy.png")
    print("Saved plot to training_accuracy.png")


def main():
    (x_train, y_train), (x_test, y_test) = load_data()
    model = build_model()
    model.summary()

    history = model.fit(
        x_train, y_train,
        epochs=10,
        validation_data=(x_test, y_test),
    )

    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
    print(f"\nTest accuracy: {test_acc:.4f}")

    model.save("image_classifier_model.h5")
    print("Model saved as image_classifier_model.h5")

    plot_history(history)


if __name__ == "__main__":
    main()
