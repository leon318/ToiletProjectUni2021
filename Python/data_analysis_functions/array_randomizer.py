import numpy as np


def array_randomizer_and_tupple_generator(feature_matrix, position_matrix, input_integer):
    shuffler = np.random.permutation(len(feature_matrix))
    feature_matrix = feature_matrix[shuffler]
    position_matrix = position_matrix[shuffler]
    rounded_index = int(round(input_integer * .01 * int(len(feature_matrix)), 0))
    # print(len(feature_matrix))
    print(f" This is it {rounded_index}")
    training_feature, test_feature = feature_matrix[:rounded_index], feature_matrix[rounded_index:]
    training_position, test_position = position_matrix[:rounded_index], position_matrix[rounded_index:]

    training_tuple = (training_feature, training_position)
    testing_tuple = (test_feature, test_position)

    # print(len(testing_tuple))

    return training_tuple, testing_tuple
