"""
Solution stub for Question 2 (Neural Networks).

Fill in the implementations of the `mlp2` and `cnn` functions.

See https://www.tensorflow.org/tutorials for a Tensorflow tutorial.
"""
from __future__ import print_function
import numpy as np
import tensorflow as tf

# These should be the only tensorflow classes you need:
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv2D, MaxPooling2D

# get_data returns (train_x, train_y), (test_x, test_y)
# argument determines whether images are shifted to top-left or bottom-right
# X values are an array of 30x30 images
# Y values are an array of 10 one-hot encoded labels
from cnn_utils import get_data

# show_examples creates an image that shows some example data from two datasets
# side by side
from cnn_utils import show_examples


def mlp1(train_x, train_y, test1_x, test1_y, test2_x, test2_y):
    """
    Train and evaluate a feedforward network with a single hidden layer.
    """
    model = Sequential([
      Flatten(input_shape=(30, 30)), # Need to flatten before Dense layers
      Dense(512, activation='relu'),
      Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_x, train_y, epochs=5)

    print("Evaluating MLP1 on test set 1")
    model.evaluate(test1_x, test1_y)
    print("Evaluating MLP1 on test set 2")
    return model.evaluate(test2_x, test2_y)

def mlp2(train_x, train_y, test1_x, test1_y, test2_x, test2_y):
    """
    Train and evaluate a feedforward network with two hidden layers.
    """
    # First layer will need argument `input_shape=(30,30)`
    model = Sequential([
        # TODO: add your implementation here
        Flatten(input_shape = (30, 30)), # Need to flatten before Dense layers
        Dense(128, activation = 'relu'),
        Dense(64, activation = 'relu'),
        Dense(10, activation = 'softmax'),
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_x, train_y, epochs=5)

    print("Evaluating MLP2 on test set 1")
    model.evaluate(test1_x, test1_y)
    print("Evaluating MLP2 on test set 2")
    return model.evaluate(test2_x, test2_y)

def cnn(train_x, train_y, test1_x, test1_y, test2_x, test2_y):
    """
    Train and evaluate a feedforward network with two hidden layers.
    """
    # Add a single "channels" dimension at the end
    trn_x = train_x.reshape([-1, 30, 30, 1])
    tst1_x = test1_x.reshape([-1, 30, 30, 1])
    tst2_x = test2_x.reshape([-1, 30, 30, 1])

    # First layer will need argument `input_shape=(30,30,1)`
    model = Sequential([
        # TODO: add your implementation here
        #A layer of 32 convolutional units with a kernel size of 5 × 5 and a stride of 1, 1.
        Conv2D(32, (5, 5), strides = (1, 1), input_shape = (30, 30, 1)),
        #A max-pooling layer with a pool size of 2 × 2 and a stride of 2, 2.
        MaxPooling2D((2, 2), strides = (2, 2)),
        #A layer of 64 convolutional units with a kernel size of 5 × 5 and the default stride.
        Conv2D(64, (5, 5)),
        #A max-pooling layer with a pool size of 2 × 2 and the default stride.
        MaxPooling2D((2, 2), (1, 1)),
        #A Flatten layer (to reshape the image from a 2D matrix into a single long vector)
        Flatten(),
        #A layer of 512 fully-connected relu units
        Dense(512, activation = 'relu'),
        #A layer of 10 fully-connected softmax units (the output layer)
        Dense(10, activation = 'softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(trn_x, train_y, epochs=5)

    print("Evaluating CNN on test set 1")
    model.evaluate(tst1_x, test1_y)
    print("Evaluating CNN on test set 2")
    return model.evaluate(tst2_x, test2_y)

def main():
    (train1_x, train1_y), (test1_x, test1_y) = get_data('top_left')
    (train2_x, train2_y), (test2_x, test2_y) = get_data('bottom_right')

    # Left column is images from top_left dataset
    # Right column is corresponding images from bottom_right dataset
    show_examples(test1_x, test1_y, test2_x, test2_y, 'examples.png')

    mlp1(train1_x, train1_y, test1_x, test1_y, test2_x, test2_y)
    mlp2(train1_x, train1_y, test1_x, test1_y, test2_x, test2_y)
    cnn(train1_x, train1_y, test1_x, test1_y, test2_x, test2_y)


if __name__ == '__main__':
    main()
