"""
Model interface
"""
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

accuracy_store = list()


class RandomForest:
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
        self.num_estimators = config.get('num_estimators', 100)
        self.max_depth = config.get('max_depth', 10)
        self.model = RandomForestClassifier(n_estimators=self.num_estimators,
                                            max_depth=self.max_depth,
                                            random_state=0)

    def train(self, train_data: Tuple[np.array, np.array], test_data: Tuple[np.array, np.array]) -> float:
        """
        Train the model using the train and validation data passed in as two tuples.

        Args:
            train_data (tuple): the training data to be used for the model (first element: features array of shape
            num_samples x num_features, second element: target array of shape num_samples x 1)
            test_data (tuple): the validation data to be used for the model (first element: features array of shape
            num_samples x num_features, second element: target array of shape num_samples x 1)
            config (dict): dictionary containing configuration data
        """

        input_train, target_train = train_data
        input_test, target_test = test_data
        self.model.fit(input_train, target_train)

        # Generate generalization metrics
        score = self.model.score(input_test, target_test)
        print(f'Test accuracy: {score}')

        return score

    def predict(self, x: np.array):
        print(f'The model prediction is {self.model.predict(x)}')


accuracy_store = list()
z = 0
while z < 15:

    model_config = {'num_estimators': 100, 'max_depth': 10}
    num_estimators = [10, 20, 50, 100, 200]
    max_depths = [5, 10, 15, 20, 50]

    scores = np.zeros([len(num_estimators), len(max_depths)])

    for i, num_estimator in enumerate(num_estimators):
        model_config['num_estimators'] = num_estimator
        for j, max_depth in enumerate(max_depths):
            model_config['max_depth'] = max_depth

            classifier = RandomForest(model_config)
            score = classifier.train(training_tuple, testing_tuple)
            scores[i, j] = score
            print(score)

    accuracy = score * 1
    acurracy_store.append(accuracy)
    print(accuracy)
    acurracy_store
    z += 1
    print(z)
