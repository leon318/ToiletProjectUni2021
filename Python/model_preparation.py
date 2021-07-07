import numpy as np
from Python.data_analysis_functions.feature_position_tuple_list_generator import tuple_list_generator
from Python.data_analysis_functions.array2d_generator import array_2d_generator
from Python.data_analysis_functions.array_randomizer import array_randomizer_and_tupple_generator
final_list, input_integer, encoded, position_and_person = tuple_list_generator()
# print(final_list)
feature_matrix, position_matrix = array_2d_generator(final_list)

# character_matrix = np.concatenate((encoded,position_matrix),axis=1)
# print(character_matrix)

num_rows1, num_cols1 = feature_matrix.shape
num_rows2, num_cols2 = position_matrix.shape
# print("feature matrix", num_rows1)
# print("feature matrix", num_cols1)
# print("position matrix", num_rows2)
# print("postion matrix", num_cols2)

training_tuple, testing_tuple = array_randomizer_and_tupple_generator(feature_matrix, position_and_person, input_integer)
# print(testing_tuple)
#
#
#
#
# # print(test)







# np.random.shuffle(feature_matrix)
#
# print(f" {test} \n")
# print(training)


# with open("datafile.txt", "rb") as f:
#     data = f.read().split('\n')
#
# random.shuffle(data)
#
# train_data = data[:80]
# test_data = data[19:]