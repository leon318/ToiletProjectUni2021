"""
Model interface
"""
from typing import Tuple
import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as tfl
import matplotlib.pyplot as plt

accuracy_store = list()


class NeuralNetwork:
    """
    Abstract model class that acts as an interface for training and evaluating machine learning models.
    Specific models inherit and implement the abstract methods of this class. The objective is to remove the dependency
    on specific frameworks (e.g., sklearn, pytorch, tensorflow) and make code shareable.
    """

    def __init__(self, config: dict):
        """
        Initialize a new model object, according to the configurations passed in

        Args:
            config: dictionary containing the configuration parameters specific to the model
        """

        # Model parameters
        self.config = config
        self.input_layer = config['input_layer']
        self.hidden_layers = config['hidden_layers']
        self.hidden_layers_activations = config['hidden_layer_activations']
        self.output_layer = config['output_layer']
        self.output_layer_activation = config['output_layer_activations']
        # Error handling - input/...

        self.model = self.build()

    def build(self):
        # Model definition via TF Functional API
        inputs = tf.keras.Input(shape=self.input_layer)
        length = len(self.hidden_layers)
        temp = inputs

        if length == 0:  # Logistic regression
            last_hidden_layer = inputs
        else:  # Deep neural network with at least 1 hidden later
            h_l = list()
            for i in range(length):
                h_l.append(tfl.Dense(units=self.hidden_layers[i], activation=self.hidden_layers_activations[i])(temp))
                temp = h_l[i]
            last_hidden_layer = h_l[-1]

        outputs = tfl.Dense(units=self.output_layer, activation=self.output_layer_activation)(last_hidden_layer)
        model = tf.keras.Model(inputs=inputs, outputs=outputs)

        return model

    def train(self, train_data: Tuple[np.array, np.array], test_data: Tuple[np.array, np.array], config: dict) -> None:
        """
        Train the model using the train and validation data passed in as two tuples.

        Args:
            train_data (tuple): the training data to be used for the model (first element: features array of shape
            num_samples x num_features, second element: target array of shape num_samples x 1)
            test_data (tuple): the validation data to be used for the model (first element: features array of shape
            num_samples x num_features, second element: target array of shape num_samples x 1)
        """
        input_train, target_train = train_data
        input_test, target_test = test_data

        optimizer = config['optimiser']
        loss = config['loss']
        metrics = config['metrics']
        epochs = config['epochs']
        batch_size = config['batch_size']
        # num_folds = config['num_of_folds']
        # verbosity = config['verbosity']

        # Compile the model
        model = self.model
        self.model.compile(loss=loss,
                           optimizer=optimizer,
                           metrics=metrics)

        # Fit data to model
        history = self.model.fit(input_train, target_train,
                                 batch_size=batch_size,
                                 epochs=epochs,
                                 verbose=0)

        # Generate generalization metrics
        score = self.model.evaluate(input_test, target_test, verbose=0)
        print(f'Test loss: {score[0]} / Test accuracy: {score[1]}')

        # print(history.history)

        # Visualize history
        # Plot history: Loss
        plt.plot(history.history['loss'])
        plt.title('Training loss history')
        plt.ylabel('Loss value')
        plt.xlabel('No. epoch')
        plt.show()

        # Plot history: Accuracy
        if metrics[0] == 'accuracy':
            plt.plot(history.history[metrics[0]])
            plt.title('Training accuracy history')
            plt.ylabel('Accuracy value (%)')
            plt.xlabel('No. epoch')
            plt.show()

        # Plot history: Mean squared error
        if metrics[0] == 'mean_squared_error':
            plt.plot(history.history[metrics[0]])
            plt.title('Training accuracy history')
            plt.ylabel('Mean squared error')
            plt.xlabel('No. epoch')
            plt.show()

        return score[1]

    def predict(self, x: np.array):
        print(f'The model prediction is {self.model.predict(x)}')


acurracy_store = list()
# print(acurracy_store)
z = 0
while z < 15:
    model_config = dict()
    train_config = {}

    train_config['metrics'] = ['accuracy']
    model_config['input_layer'] = (12)
    model_config['hidden_layers'] = []
    model_config['hidden_layer_activations'] = []
    # Relu
    model_config['output_layer'] = 14
    model_config['output_layer_activations'] = 'softmax'
    train_config['loss'] = 'categorical_crossentropy'

    optimiser = ['adam']
    print(type(optimiser))
    epochs = [1000]
    batch_size = [32]
    scores = np.zeros([len(optimiser), len(epochs), len(batch_size)])

    for i, _ in enumerate(optimiser):
        train_config['optimiser'] = optimiser[i]
        for j, _ in enumerate(epochs):
            train_config['epochs'] = epochs[j]
            for k, _ in enumerate(batch_size):
                train_config['batch_size'] = batch_size[k]
                sitting_classifier = ModelDNN(model_config)
                sitting_classifier.model.summary()
                score = sitting_classifier.train(training_tuple, testing_tuple, train_config)
                scores[i, j, k] = score
                print(score)
    #             print(score)
    accuracy = score * 1
    acurracy_store.append(accuracy)
    print(accuracy)
    acurracy_store
    z += 1
    print(z)
