'''
This function generates 2d arrays from the 1d arrays. This is necessary for it to be plugged into the model.
'''
import numpy as np
def array_2d_generator(final_list):
    print(len(final_list))
    feature_matrix = np.array([])
    position_matrix = np.array([])
    feature = list()
    position = list()
    for i, element in enumerate(final_list):
        a = final_list[i][0]
        b = final_list[i][1]
        # print(b)
        feature.append(a)
        position.append(b)
        # np.append(feature_matrix, a)
    feature_matrix = np.vstack(feature)
    position_matrix = np.vstack(position)
    # print(feature_matrix)
    # print(position_matrix)

    return feature_matrix, position_matrix