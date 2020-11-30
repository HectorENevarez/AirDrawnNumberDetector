import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist #28x28 images of hand-written digits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizing data between 0 and 1. Normalizing leads to more efficient neural network thus better predictive model
x_train, x_test = x_train / 255, x_test / 255

#There are a couple different ways to do this however we will be using the model.add method
model = keras.Sequential(name="MNIST_Model") #Standard model type that connects all Neurons
model.add(layers.Flatten(input_shape=(28,28))) #go from 28 x 28 to 784 x 1
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.save('DRAW_MODEL.model')